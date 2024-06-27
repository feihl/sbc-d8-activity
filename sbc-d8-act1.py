# from random import randint

# def code():
#     return randint(0, 99)


# def dashboard():
#     print(">>>>> Welcome To User Login SYSTEM <<<<<")
#     # change_password()

# def reg():
#     reg = input("Enter Your Name: ")
#     pass_ = input("Enter Your Password: ")
#     con_= input("Re-type Your Password to Confirm: ")
#     if con_ == pass_:
#         data = open("all_account.txt", "a")
#           
#         print(con_, file=data)
#         data.close()
#         dashboard()
#     else:
#         print("Password and Confirm Password is not Match!!!!")
#     reg = input("Enter Your Name: ")

# def login():
#     sample_file = [line.strip() for line in open("sample_text_1.txt")]
#     log = input("Enter Name to LOGIN: ")
#     password = input("Enter your Password: ")
#     ###
#     if log in sample_file:
#         print("Already Exist Registered Name!!")
#         ###
#         file_path = open("all_account.txt", "r")
#         var = file_path.readlines()
#         print(var[2])
#         if password:
#             print("Password Match")
#         else: 
#             print("Password Not Match")
#     else:
#         print("Your Name, Not Register")

# def change_password():
#     file_path = open("all_account.txt", "r")
#     var = file_path.readlines()
#     for i in var:
#         i = "".strip()
#     print("Login Successfully")
#     print("Change Password!!")
#     your_name = input("Enter Your Name: ")
#     old_password = input("Enter your OLD Password: ")
#     new_password = input("Enter your NEW Password: ")
#     ###    
#     if your_name != i:
#         print("Incorrect Name!!!")
#         ###
#         if old_password != var:
#             print("Password Incorrect")
#             option = input("Re-Type Your Name ")
#             pincode = code()
#             print(f"This you Code to Change Password == {pincode}")
#             ###
#             while True:
#                 your_code = input("Enter your CODE: ")
#                 if your_code.isdigit() and int(your_code) == pincode:
#                     break
#                 else:
#                     print("Invalid Code")
#         ###
#         elif old_password == var:
#             print("Password has been Change")
#     elif your_name == var:
#         print("Correct Name!!!")


# while True:
#     first_ = input("1 === Register\n2 === Login\n3 === Change Password\n4 === Cancel\n === ")
#     if first_ == '1':
#         reg()
#     elif first_== '2':
#         login()
#     elif first_ == '3':
#         change_password()
#     elif first_ == '4':
#         print("Cancel")
#         break

def dashboard():
    print(">>>>> Welcome To User Login SYSTEM <<<<<")

def reg():
    print("==== Register ===")
    name = input("Enter Name: ")
    password = input("Enter Password: ")
    def all():
        sample_file = [line.strip() for line in open("username.txt")]
        return sample_file
    if name in all():
        print("User Name Already Exist!!!")
        reg()
    else:
        sample_file = open("username.txt", 'a')
        print(name, "\n", file=sample_file)
        sample_file.close()

        sample_file = open("password.txt", 'a')
        print(password, "\n", file=sample_file)
        sample_file.close()

def log():
    print("=== Login ===")
    name = input("Enter Name: ")
    password = input("Enter Password: ")
    user = [line.strip() for line in open("username.txt")]
    username = user.index(name)
    if username < len(user):
        print("Login Successfully")
    else: 
        print("Account doesn't Exist")

def change():
    print("=== Change Password ===")
    name = input("Enter Name: ")
    password = input("Enter Old Password: ")
    new_password = input("Enter New Password: ")
    users = [line.strip() for line in open("username.txt")]
    pas = [line.strip() for line in open("password.txt")]
    if name in users:
        i = users.index(name)
        if i < len(pas) and pas[i] == password:
            pas[i] == new_password

            with open("password.txt", "w") as l:
                for pa__ in pas:
                    l.write(pa__ + "\n")
            print("Password Updated!!!")
        else:
            print("Invalid Username and Password")
    else:
        print("Invalid Username and Password")

while True:
    print("=== Login ===")
    first_ = input("1 === Register\n2 === Login\n3 === Change Password\n4 === Cancel\n === ")
    if first_ == '1':
        reg()
    elif first_== '2':
        log()
    elif first_ == '3':
        change()
    elif first_ == '4':
        break