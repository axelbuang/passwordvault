from hashlib import *


def username(username):

    str(username)


def pass_hasher(password):

    hash_algo1 = md5(password.encode('utf-8')).hexdigest()
    hash_algo2 = sha1(password.encode('utf-8')).hexdigest()
    hash_algo3 = sha256(password.encode('utf-8')).hexdigest()
    print('MD5     : ' + hash_algo1)  # DEPRECATED: EXISTING COLLISION
    print('SHA-1   : ' + hash_algo2)  # DEPRECATED: EXISTING COLLISION
    print('SHA-256 : ' + hash_algo3)
