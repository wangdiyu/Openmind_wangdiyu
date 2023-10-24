while True:
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "admin" and password == "42":
        print("身份验证成功")
        break
    else:
        print("身份验证失败")
