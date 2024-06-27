def open_username(mode):
    return open(r"./storage/username.txt", mode)

def open_password(mode):
    return open(r"./storage/password.txt", mode)

def list_usernames():
    return [line.strip() for line in open_username("r")]

def list_passwords():
    return [line.strip() for line in open_password("r")]

def check_username(username):
    return username in list_usernames()

def get_index(username):
    return list_usernames().index(username)

def auth(index, password):
    list = list_passwords()
    return password == list[index]

def register(username, password):
    if not check_username(username):
        file_username, file_password = open_username("a"), open_password("a")
        print(username, file=file_username)
        print(password, file=file_password)
        file_username.close()
        file_password.close()
        return "Registration Successful!"
    else:
        return "Registration Failed!"

def login(username, password):
    if check_username(username) and auth(get_index(username), password):
        return "Login Successfully!"
    else:
        return "Login Failed!"

def change(username, password, new):
    if check_username(username) and auth(get_index(username), password):
        editable = list_passwords()
        editable[get_index(username)] = new
        d = open_password("w")
        d.close()
        for item in editable:
            instance = open_password("a")
            print(item, file=instance)
            instance.close()
        return "Change Successfully!"
    else:
        return "Verification Failed!"

def input_credentials():
    username = input("Username: ")
    password = input("Password: ")
    return {"username": username,
            "password": password}

def main():
    while True:
        command = int(input("[1] Login [2] Register [3] Change Password \n> "))
        if command == 1:
            request = input_credentials()
            print(login(request["username"], request["password"]))
        elif command == 2:
            request = input_credentials()
            print(register(request["username"], request["password"]))
        elif command == 3:
            request = input_credentials()
            new = input("New Password: ")
            print(change(request["username"], request["password"], new))
        else:
            print("Blee!!")

if __name__ == "__main__":
    main()