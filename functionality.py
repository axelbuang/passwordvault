# This is for the functionality of the application when run in terminal.

import sys
from datetime import datetime as dt
from data_login import Information

title = "Password Vault 1.0"
day_of_the_year  =   dt.now().strftime("%j")
date_today = dt.now().strftime("%A, %d %B %Y")
time_today = dt.now().strftime("%H : %M : %S")
                                    
what_to_do = '''SYNTAX
        -a, -add : Add new data.
        -r, -rm : Remove existing data.      
MISC
        -V : Print version.
        -help : Go to help.
        -x : Exit.
'''
print(title)
print('Day ' +  day_of_the_year + ":  " + date_today  + ", "  + time_today )
print(what_to_do)
while True:

    i = input('vault@your_stupid_computer~$ ')
        
    if i == "-a" or i == "-add":
#         Information.add_data(info)
        pass
    elif i == "-rm":
        pass      
    elif i == '-x':
        exit()
    elif i == '':
        continue
    else:
        str_i = str(i)
        print("[UNKNOWN]: " + "'" + str_i + "'" + " is not a command.")
        continue
