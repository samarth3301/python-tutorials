# username pass create  username | signup | login


class Users:
    def __init__(self):
        self.users = []
    
    
    def register_user(self, username: str, password: str):
        for user in self.users:
            if user["username"] == username:
                print("Username already exists")
                return

        self.users.append({
            "username": username,
            "password": password
        })
        print("User registered")
        return
    
    
    def fetchUsers(self):
        if not self.users:
            print("No user data.")
        for users in self.users:
            print(users)
    
    
    def login(self, username: str, password: str):
        for user in self.users:
            if user["username"] == username and user["password"] == password:
                print("Hello idiot")
                return
        print("Invalid data")
    
            
app = Users()

def fetchUserInputs():
    username = input("Enter your username :")
    password = input("Enter your password :")
    return (username, password)

while True:
    print("[+] Enter your choice:")
    print("[+] Add User")
    print("[+] View Users")
    print("[+] Login")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        app.register_user(*fetchUserInputs())
    if choice == 2:
        app.fetchUsers()
    if choice == 3:
        app.login(*fetchUserInputs())
    if choice not in [1, 2, 3]:
        print("Enter a valid input")
        break