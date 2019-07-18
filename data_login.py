from hashlib_test import pass_hasher


class Information(object):

    # assign value(s) to other attributes (except self) if  you don't want to write parameters when calling this method.
    # define values whatever you want
    def __init__(self, org="", website="", email="", username=""):

        self.org = org
        self.website = website
        self.email = email
        self.username = username

    # work on this   
    def __str__(self):

        return self.org
        _website = self.website
        _email = self.email

        
# work on these
class Add(Information):

    def add_new_data(self):

        print("You are {} a NEW information/data.".format("[ADDING]"))

        info = Add(input('    Name of Organization: '),
                   input('    Website/Domain: '),
                   input('    Email: '),
                   input('    Username: '))


        pass_hasher(input('    Password: '))

    def add_data(self):

        print("You are {} an information/data.".format("[ADDING]"))

        info = Add(input('    Name of Organization: '),
                   input('    Website/Domain: '),
                   input('    Email: '),
                   input('    Username: '))

        pass_hasher(input('    Password: '))


class Del(Information):
    print("JUST WORKED...")
    pass

# =====================================
# work on this; delete after use
class Add_or_remove:
    
    def __bool__(self):
        pass
    def rmdata(self):
        self.on= True

adh=Add_or_remove()
help(adh.rmdata())
# =====================================

# # uncomment methods below soon
# def main():

#     print("Welcome...")

#     if adddata==True:
#         _add = Add()
#         _in = input("Add [NEW] OR add [EXISTING]: [Y/n] ")
#         if _in == "y" or _in == "Y":
#             # initialize, always, for good
#             _add.add_new_data()
#         elif _in == "n" or _in == "N":
#             _add.add_data()
#         else:
#             print("K")
#             pass
#     else:
#         # initialize, always, for good
#         _del = Del()
#         _del

# if __name__ == '__main__':
#     main()
    
