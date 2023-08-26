import subprocess

#TODO create more things with this


def open_rps():
    subprocess.run(["python", "rpsgame.py"]) #this can be any python file, just be sure to name it correctly

user_input = input("Enter a command: ")
if user_input.lower() == "rps": #choose a term for your python file, with this example, it will open the file "rpsgame.py" by simply typing rps in the terminal
    open_rps()
