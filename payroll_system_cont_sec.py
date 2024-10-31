import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror, showwarning
from typing import Dict, Optional
import shelve
import logging
import re
from datetime import datetime
from decimal import Decimal
from dataclasses import dataclass

# Configure logging with more detail
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='payroll.log'
)
logger = logging.getLogger(__name__)

@dataclass
class DeductionRates:
    """Configurable deduction rates"""
    paye: Decimal = Decimal('250')
    development_levy: Decimal = Decimal('100')
    bank_charges: Decimal = Decimal('54')

class InputValidation:
    """Input validation methods"""
    @staticmethod
    def validate_phone(phone: str) -> bool:
        return bool(re.match(r'^\d{11}$', phone))
    
    @staticmethod
    def validate_account(account: str) -> bool:
        return bool(re.match(r'^\d{10}$', account))
    
    @staticmethod
    def validate_bvn(bvn: str) -> bool:
        return bool(re.match(r'^\d{11}$', bvn))
    
    @staticmethod
    def validate_nin(nin: str) -> bool:
        return bool(re.match(r'^\d{11}$', nin))

class Person:
    def __init__(
        self,
        name: str,
        days_worked: int = 30,
        phone_number: str = '',
        account_number: str = '',
        home_address: str = '',
        bank_name: str = '',
        gross_pay: Decimal = Decimal('0'),
        iou: Decimal = Decimal('0'),
        location: str = 'General',
        bvn: str = '',
        nin: str = '',
        deduction_rates: Optional[DeductionRates] = None
    ):
        # Input validation
        if not name:
            raise ValueError("Name cannot be empty")
        if not InputValidation.validate_phone(phone_number):
            raise ValueError("Invalid phone number format")
        if not InputValidation.validate_account(account_number):
            raise ValueError("Invalid account number format")
        if not InputValidation.validate_bvn(bvn):
            raise ValueError("Invalid BVN format")
        if not InputValidation.validate_nin(nin):
            raise ValueError("Invalid NIN format")
        
        self.name = name
        self.iou = iou
        self.location = location
        self.days_worked = days_worked
        self.account_number = account_number
        self.bank_name = bank_name
        self.phone_number = phone_number
        self.bvn = bvn
        self.nin = nin
        self.home_address = home_address
        self.monthly_gross = gross_pay
        self.pay_per_day = self.monthly_gross / Decimal('30')
        self.deduction_rates = deduction_rates or DeductionRates()
        
    def deductions(self) -> Decimal:
        """Calculate total deductions"""
        return (
            self.iou +
            self.deduction_rates.paye +
            self.deduction_rates.development_levy +
            self.deduction_rates.bank_charges
        )
    
    def gross_pay(self) -> Decimal:
        """Calculate gross pay based on days worked"""
        return self.pay_per_day * Decimal(str(self.days_worked))
    
    def net_pay(self) -> Decimal:
        """Calculate net pay"""
        return self.gross_pay() - self.deductions()
    
    def generate_payslip(self) -> str:
        """Generate a formatted payslip"""
        return f"""
CONTINENTALS SECURITY SERVICES
PAYSLIP FOR {datetime.now().strftime('%B %Y')}

Employee: {self.name}
Location: {self.location}
Days Worked: {self.days_worked}

EARNINGS
Gross Pay: ₦{self.gross_pay():,.2f}

DEDUCTIONS
PAYE Tax: ₦{self.deduction_rates.paye:,.2f}
Development Levy: ₦{self.deduction_rates.development_levy:,.2f}
Bank Charges: ₦{self.deduction_rates.bank_charges:,.2f}
IOU: ₦{self.iou:,.2f}
Total Deductions: ₦{self.deductions():,.2f}

NET PAY: ₦{self.net_pay():,.2f}

Bank: {self.bank_name}
Account: {self.account_number}

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

class ContinentalsGUI:
    variables = (
        'name', 'location', 'days_worked', 'account_number', 'bank_name',
        'home_address', 'phone_number', 'bvn', 'nin', 'iou', 'monthly_gross'
    )
    
    def __init__(self, db_name: str = 'ContinentalsSecuritytest'):
        self.data_base = shelve.open(db_name)
        self.entries: Dict[str, tk.Entry] = {}
        
        self.window = tk.Tk()
        self.window.title('Continentals Security - Payroll Management')
        self.window.geometry('800x600')
        self.create_widgets()
        
    def create_widgets(self):
        """Create and arrange the GUI objects with improved layout"""
        # Main container
        main_frame = ttk.Frame(self.window, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Entry fields frame
        entry_frame = ttk.LabelFrame(main_frame, text="Employee Details", padding="5")
        entry_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Create Labels and Entry fields with validation
        for idx, label in enumerate(('key',) + self.variables):
            ttk.Label(entry_frame, text=label.replace('_', ' ').title()).grid(
                row=idx // 2, column=idx % 2 * 2, sticky=tk.W, padx=5, pady=2
            )
            entry = ttk.Entry(entry_frame)
            entry.grid(row=idx // 2, column=idx % 2 * 2 + 1, padx=5, pady=2, sticky=tk.EW)
            self.entries[label] = entry
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        # Create buttons
        buttons = [
            ('Fetch', self.fetch_record),
            ('Update', self.update_record),
            ('Clear', self.clear_fields),
            ('Generate Payslip', self.generate_payslip),
            ('Salary Schedule', self.generate_salary_schedule),
            ('Quit', self.quit_app)
        ]
        
        for text, command in buttons:
            ttk.Button(button_frame, text=text, command=command).pack(side=tk.LEFT, padx=5)
        
        # Add results text area
        self.results_text = tk.Text(main_frame, height=15, width=60)
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    def fetch_record(self):
        """Fetch and display employee record"""
        key = self.entries['key'].get().strip().lower()
        if not key:
            showwarning('Warning', 'Please input key or name')
            return
            
        try:
            record = self.data_base[key]
            self.clear_fields()
            self.entries['key'].insert(0, key)
            
            for value in self.variables:
                self.entries[value].insert(0, str(getattr(record, value)))
                
        except KeyError:
            showerror('Key Error', f'No record found for key: {key}')
        except Exception as e:
            logger.error(f'Error fetching record: {e}')
            showerror('Error', f'Error fetching record: {str(e)}')
    
    def update_record(self):
        """Update or create new employee record"""
        key = self.entries['key'].get().strip().lower()
        if not key:
            showerror('Error', 'Please input a key')
            return
            
        try:
            values = {
                'name': self.entries['name'].get().strip(),
                'location': self.entries['location'].get().strip(),
                'days_worked': int(self.entries['days_worked'].get().strip()),
                'account_number': self.entries['account_number'].get().strip(),
                'bank_name': self.entries['bank_name'].get().strip(),
                'home_address': self.entries['home_address'].get().strip(),
                'phone_number': self.entries['phone_number'].get().strip(),
                'bvn': self.entries['bvn'].get().strip(),
                'nin': self.entries['nin'].get().strip(),
                'iou': Decimal(self.entries['iou'].get().strip()),
                'gross_pay': Decimal(self.entries['monthly_gross'].get().strip())
            }
            
            new_instance = Person(**values)
            self.data_base[key] = new_instance
            showinfo('Success', 'Record stored successfully')
            
        except ValueError as e:
            showerror('Value Error', str(e))
        except Exception as e:
            logger.error(f'Error updating record: {e}')
            showerror('Error', f'Error updating record: {str(e)}')
    
    def generate_payslip(self):
        """Generate and display payslip"""
        key = self.entries['key'].get().strip().lower()
        if not key:
            showwarning('Warning', 'Please fetch an employee record first')
            return
            
        try:
            employee = self.data_base[key]
            payslip = employee.generate_payslip()
            self.results_text.delete('1.0', tk.END)
            self.results_text.insert('1.0', payslip)
        except Exception as e:
            logger.error(f'Error generating payslip: {e}')
            showerror('Error', f'Error generating payslip: {str(e)}')
    
    def generate_salary_schedule(self):
        """Generate and display salary schedule for all employees"""
        try:
            schedule = "CONTINENTALS SECURITY SERVICES\n"
            schedule += f"SALARY SCHEDULE - {datetime.now().strftime('%B %Y')}\n\n"
            schedule += f"{'Name':<30}{'Location':<15}{'Days':<8}{'Gross':<15}{'Net':<15}\n"
            schedule += "-" * 83 + "\n"
            
            total_gross = Decimal('0')
            total_net = Decimal('0')
            
            for key, employee in self.data_base.items():
                schedule += (
                    f"{employee.name:<30}"f"{employee.location:<15}"
                    f"{employee.days_worked:<8}"
                    f"₦{employee.gross_pay():>13,.2f}"
                    f"₦{employee.net_pay():>13,.2f}\n"
                )
                total_gross += employee.gross_pay()
                total_net += employee.net_pay()
            
            schedule += "-" * 83 + "\n"
            schedule += f"{'TOTALS:':<53}₦{total_gross:>13,.2f}₦{total_net:>13,.2f}\n"
            
            self.results_text.delete('1.0', tk.END)
            self.results_text.insert('1.0', schedule)
            
        except Exception as e:
            logger.error(f'Error generating salary schedule: {e}')
            showerror('Error', f'Error generating salary schedule: {str(e)}')
    
    def clear_fields(self):
        """Clear all entry fields"""
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.results_text.delete('1.0', tk.END)
    
    def quit_app(self):
        """Safely close the database and quit"""
        try:
            self.data_base.close()
            self.window.quit()
        except Exception as e:
            logger.error(f'Error closing application: {e}')
    
    def run(self):
        """Start the application"""
        self.window.mainloop()

def main():
    app = ContinentalsGUI('employee_database_test0')
    app.run()

if __name__ == '__main__':
    main()
