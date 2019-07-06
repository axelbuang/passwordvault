# This file will save all of my username, but password are converted into hash code.
# Please use SHA256 or later to avoid collisions.
# Import the HASHLIB package.

import sys
from hashlib_test import *


pre_title = 'Welcome to axel password vault. Please log in your username in plaintext.'
vault_ver = '1.0'
py_ver = sys.version

print(pre_title, 'Vault version: ' + vault_ver)

username(input('USERNAME: '))
pass_hasher(input('PASSWORD: '))



