import string
import random
import os
import sys
import time
class CloakSDK:
    def delete_file(path):
        if os.path.exists(path):
            os.remove(path)
    def check_path(path):
        if not os.path.exists(path):
            os.makedirs(path)
    def check_file(path):
        if not os.path.exists(path):
            print("File not found")
        else:
            print("File found")
    def create_file(path):
        if os.path.exists(path):
            print("File already exists")
        else:
            open(path, "w").close()
            print("File created")
    def create_folder(path):
        if os.path.exists(path):
            print("Folder already exists")
        else:
            os.makedirs(path)
            print("Folder created")
    def delete_folder(path):
        if os.path.exists(path):
            os.rmdir(path)
            print("Folder deleted")
        else:
            print("Folder not found")
    def change_dir(path):
        os.chdir(path)
        print("Directory changed")
    def find_file(path):
        for root, dirs, files in os.walk(path):
            for name in files:
                print(os.path.join(root, name))
    def make_python_slower():
        return time.sleep(10)
    def password_generator():
        length = int(input("Enter the length of the password: "))
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for i in range(length))
        print("Your password is: ", password)
        return password
    def check_path(path):
        if not os.path.exists(path):
            os.makedirs(path)
    def info():
        print(sys.version)
        print(sys.version_info)
        print(sys.platform)
        print(sys.path)
        print(sys.getdefaultencoding())
        print(sys.argv)
        print(sys.maxsize)
        print(sys.getfilesystemencoding())
        print(sys.getrecursionlimit())
        print(sys.getsizeof())
        print(sys.getcheckinterval())
        print(sys.getdefaultencoding())
        print(sys.getfilesystemencoding())
    def shmell():
        smells = ["Chocolate","Strawberry","Banana","Apple","Watermelon"]
        print("You smell like " + random.choice(smells))
    def tell_a_row():
        # This is joke
        print("Roses is #FF0000")
        print("Banana is #FFFF00")
        print("If you can read this your a nerd")