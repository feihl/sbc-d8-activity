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