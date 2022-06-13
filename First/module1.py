CORRECT_LOGIN = "Вася"
CORRECT_PASS = "333"
pass_count = 3

while pass_count:
    user_login = input("Login:  ")
    user_password = input("Password:  ")
    if user_login == CORRECT_LOGIN and user_password == CORRECT_PASS:
        print("Ok")
        break
    else:
        pass_count -= 1
        print("Wrong credentials")

    if not pass_count:
        print("пипец")
