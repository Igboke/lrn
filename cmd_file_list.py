import subprocess

# Running a simple command
#list of files from current working directory
drack = open('list_of_files.txt','w')
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
drack.write(result.stdout)
drack.close()