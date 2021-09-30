# import json
import json
import os


class program:

    def user_inputs(self):
        # self.FIRST_NAME = FIRST_NAME
        # self.PASSWORD = PASSWORD
        # self.USERNAME = USERNAME
        path = os.path.getsize('userdata.json')
        if path == 0:
            print('"\n==========SIGN IN============"')
            FIRST_NAME = input('"\nEnter first_name"')
            PASSWORD = input('"\nEnter password"')
            USERNAME = input('"\nEnter username"')

            with open('userdata.json', 'r+') as file:
                data = json.load(file)
                if USERNAME in data.keys():
                    print('username already exist')
                elif FIRST_NAME in data.keys():
                    print('name already exist choose another name')
                elif len(PASSWORD) < 10:
                    print('password too short')
                else:
                    data[FIRST_NAME] = [PASSWORD, "ADMIN"]
                    file.seek(0)
                    json.dump(data, file)
                    file.truncate()

                    print("Account created successfully!")

        elif path > 0:
            print('"\n==========LOGIN============"')
            USERNAME = input('enter your username')
            PASSWORD = input('enter your password')
            with open('userdata.json', 'r') as file2:
                data2 = json.load(file2)
                if USERNAME not in data2.keys():
                    print("An account of that name doesn't exist.\nPlease create an account first.")
                elif PASSWORD != data2.keys():
                    print('please check your password')
                else:
                    json.dump(data2, file2)
                    print('Welcome Back')

cls = program()
cls.user_inputs()

# user = []


# def logout():
#    name = input('enter name')
#    password = input('enter password')
#    with open('userdata.json', 'r+') as f:
#        try:
#            data = json.load(f)
#            file = json.load(data)
#            json.dump(**data, **file)
#            if password == data.keys['password']:
#                pass
#
#            else:
#                print(f'this {password} is not the password of this {name}')
#        except:
#            print('not ok')


# global user
# if len(user) == 0:
#     print("You are already logged out.")
# else:
#     user = []
#     print("You have been logged out successfully.")
