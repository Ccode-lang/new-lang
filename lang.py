import os
import sys
from math import *
variables = {}

while True:
    # debug
    #print(variables)
    try:
        if not sys.argv[1] == "-c":
            inp = input(">>").lstrip()
        else:
            inp = input().lstrip()
        variable_assigned = False
        
        # replace variable names with values
        for var_name, var_value in variables.items():
            inp = inp.replace(f"{var_name}$", var_value)
        
        # variable handler
        if ":=" in inp:
            var_name, *var_value = inp.split(":=")
            var_name, var_value = var_name.strip(), ':='.join(var_value)
            if ' ' not in var_name and var_value:
                variables[var_name] = var_value
                variable_assigned = True
        
        inp = inp or "No content"
        keyword = inp.split(" ")[0]
        # commands
        if inp == "exit":
            if not sys.argv[1] == "-c":
                print("Exiting.")
            break
            
        elif keyword == "print":
            print(inp[6:])
            
        elif inp == "ls":
            directories = [f for f in os.listdir('.') if not os.path.isfile(f)]
            files = [f for f in os.listdir('.') if os.path.isfile(f)]
            for d in directories:
                print(f'{d}/')
            for f in files:
                print(f)
                
        elif keyword == "ls" and inp.strip() != "ls" :
            targetdirectory = inp[3:]
            try:
                directories = [f for f in os.listdir(targetdirectory) if not os.path.isfile(f)]
                files = [f for f in os.listdir(targetdirectory) if os.path.isfile(f)]
                for d in directories:
                    print(f'{d}/')
                for f in files:
                    print(f)
            except:
                print(f'Unable to locate directory to {targetdirectory}. Check if the directory exist?')
        
        elif inp == "pwd" :
            print(os.getcwd())
                
        elif keyword == "cd":
            targetdirectory = inp[3:]
            try:
                os.chdir(targetdirectory if targetdirectory else os.path.expanduser("~"))
                print("Directory changed to %s" % os.getcwd())
            except:
                print(f'Unable to change directory to {targetdirectory}. Does the directory exist?')
        
        elif keyword == "calc" :
            expr = inp[5:]
            print(expr, "=", eval(expr))
        
        elif not variable_assigned:
            print(f"syntax error - ({inp})")
        
        print("-"*25)
    except:
        print("Correct usage 'python3 lang.py -c'")
        break
