import subprocess

#get the pathway from the user
work_dir = input('Input working directory: ')
#getting file name
file_name=input('input file name: ')

#capture the output, for linux
text=subprocess.run(['ls','-l'], capture_output= True, text = True, cwd=work_dir)

#store output
plan=open(file_name,'w')
plan.write(text.stdout)
plan.close()


