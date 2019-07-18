# This is for the functionality of the application when run in terminal.

import data_login
from datetime import datetime as dt

title = "Password Vault 1.0"

# will print the weekday, date, month, and year respectively
day_of_the_year = dt.now().strftime("%j")
date_today = dt.now().strftime("%A, %d %B %Y")
time_today = dt.now().strftime("%H : %M : %S")

what_to_do = '''[USAGE]
        -a, -add : Add new data.
             -rm : Remove existing data.
[MISC]
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
        import data_login
        data_login.main()
    elif i == "-rm":
        # pass
        pass
    elif i == '-x':
        exit()
    elif i == '':
        continue
    else:
        str_i = str(i)
        print("[UNKNOWN]: " + "'" + str_i + "'" + " is not a command.")
        continue

