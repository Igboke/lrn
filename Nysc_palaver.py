import random
import string
class NYSC:
    LGA = [''.join(random.choices(string.ascii_letters,k=3)) for i in range(10)]
    def __init__(self,name,age,state_of_origin,state_of_residence,deployed_state,discipline):
        self.name=name
        self.age=age
        self.state_of_deployment = deployed_state
        self.state_of_origin = state_of_origin
        self.state_of_residence = state_of_residence
        self.discipline = discipline

    def get_details(self):
        print(f'Name: {self.name}, State of Deployment: {self.state_of_deployment}, Registration Number: {self.reg_no}, Age:{self.age}, State of Origin: {self.state_of_origin}, State of residence: {self.state_of_residence}')
    
    def reg_number(self):
        self.reg_no = random.randint(1000,10000)
    
    def assign_platoon(self):
        platoon = str(self.reg_no)[-1] if str(self.reg_no)[-1] in [str(i) for i in range(10)] else '10'
        print(f'You are in Platoon {platoon}')
    
    def apply_relocation(self,potential_state,reason):
        if potential_state.lower() in ['lagos','abuja',self.state_of_origin.lower(),self.state_of_residence.lower()] and reason.lower() in ['health']:
            print('Relocation Failed')
        else:
            print('Relocation Successful!!!')
    
    def PPA(self):
        self.LGA= random.choice(NYSC.LGA)
        print(f'Report to {self.LGA} for further instructions')
    
    def itinary_(self):
        self.itinary = {6:'Breakfast',7:'Parade',8:'Parade',9:'Parade',10:'Parade',11:'break',12:'SAED',1:'Lunch'}
    
    def current_task(self,time:int):
        print(self.itinary.get(time,'Sleep'))
    
class Redcross(NYSC):
    def itinary_(self):
        self.itinary = {6:'Breakfast',7:'Redcross',8:'Training',9:'Training',10:'Training',11:'break',12:'SAED',1:'Lunch'}

corp_member_1 = NYSC('Igboke Chibuike Daniel','23','Ebonyi','Lagos','Ogun','Human Physiology')
corp_member_1.reg_number()
corp_member_1.assign_platoon()
corp_member_1.get_details()
corp_member_1.apply_relocation('Ebonyi','health')
corp_member_1.PPA()
corp_member_1.itinary_()
corp_member_1.current_task(8)
corp_member_2=Redcross('Taofeek','23','hombe','lagos','oyo','animal science')
corp_member_2.itinary_()
corp_member_2.current_task(8)
corp_member_2.reg_number()
corp_member_2.assign_platoon()
corp_member_2.get_details()

