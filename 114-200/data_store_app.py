def store_data(username, password):
    with open('stored_data.txt', 'a') as file:
        file.write(f"username: {username}\npassword: {password}\n")

def display_data():
    try:
        with open('stored_data.txt', 'r') as file:
            data = file.read()
            print("Stored Data:")
            print(data)
    except FileNotFoundError:
        print("No data stored yet.")

def clear_data():
    with open('stored_data.txt', 'w') as file:
        file.write('')
    print("Data cleared successfully!")

def account_exists(username, password):
    try:
        with open('stored_data.txt', 'r') as file:
            for line in file:
                if 'username' in line:
                    stored_username = line.split(': ')[1].strip()
                if 'password' in line:
                    stored_password = line.split(': ')[1].strip()
                    if username == stored_username and password == stored_password:
                        print("Your account is ready.")
                        return True
    except FileNotFoundError:
        pass  # Handle the case where the file doesn't exist
    return False

if __name__ == "__main__":
    while True:
        log_or_sign_in = input('Create account - c or login - l or see data - data or exit - exit: ')

        if log_or_sign_in == "c":
            user_input = input("Enter username: ")
            user_input2 = input("Enter password: ")
            store_data(user_input, user_input2)
            print("Account created successfully!")
        elif log_or_sign_in == "l":
            print("It is the login page.")
            user_input = input("Enter username: ")
            user_input2 = input("Enter password: ")
            if account_exists(user_input, user_input2):
                # Perform actions when login is successful
                pass
            else:
                print("Login failed. Username or password incorrect.")
        elif log_or_sign_in == "data":
            display_data()
        elif log_or_sign_in == "exit":
            break
        else:
            print("Invalid input. Please try again.")
