def get_non_empty_input(prompt, field_name):
    while True:
        value = input(f"{prompt}: ").strip()
        if value == "":
            print(f"{field_name} cannot be empty. Try again.")
        else:
            return value
        
def check_username_taken(username,users):
    for user in users:
        if user["username"].lower() == username.lower():
            return True
    return False
    
def get_unique_username(users):
    while True:
        username = input("Enter Username: ").strip()
        if username == "":
            print("Username cannot be empty. Please try again")
        elif check_username_taken(username,users):
            print("Username already taken. Please try a different one")
        else:
            return username
        

def get_password():
    while True:
        password1 = input("Enter Password: ").strip()
        password2 = input("Re-enter Password: ").strip()
        if password1 == "" or password2 == "":
            print("Password field cannot be empty. Please try again")
        if password1 != password2:
            print("Passwords do not match. Please try again")
        else:
            return password1
        
def display_user_summary(username, last_name, first_name, password):
    masked = '*' * len(password) 
    print(f"Proposed User Account: Username: {username}, Name : {last_name} , {first_name}, Password: {masked}")


def main():
    users = []
    
    while True:
        first_name = get_non_empty_input("Enter First Name: ","First Name")
        last_name = get_non_empty_input("Enter Last Name: ", "Last Name")
        username = get_unique_username(users)
        password = get_password()

        display_user_summary(username, last_name, first_name, password)

        accept = input("Accept? (y/n): ").strip().lower()
        if accept == 'y':
            user = {"username": username, "first_name": first_name, "last_name": last_name, "password": password}
            users.append(user)
            print("Account Accepted and added")
        elif accept == 'n':
            print("Account Discarded")
        else:
            print("Enter either Y or N")

        quit_choice = input("Quit? (q/Q to exit, any other key to continue):").strip().lower()
        if quit_choice == 'q':
            for u in users:
                masked_pwd = '*' * len(u["password"])
                print({ "username": u["username"], "first_name": u["first_name"], "last_name": u["last_name"], "password": masked_pwd })
            break

if __name__ == "__main__":
    final_users = main()
