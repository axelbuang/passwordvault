# This is for the functionality of the application when run in terminal.

import sys
import datetime

opening = "Password Vault 1.0 \n'Put me some Day of the week, DD/MM/YYYY, and timezone' \n"
what_to_do = '''SYNTAX 
    pv -add : Add new data.
    pv -remv: Remove existing data.
    
MISC
    pv -help : Go to help.
    pv -x : Exit.'''

print(opening)
print(what_to_do)