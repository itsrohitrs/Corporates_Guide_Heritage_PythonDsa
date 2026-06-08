username = "Rohit"
password = "secure@123"
is_active = True

entered_username = input("Enter Username: ")
entered_password = input("Enter Password: ")

if entered_username == username:
    
    if is_active:
        
        if entered_password == password:
            print("Login Successful")
        else:
            print("Incorrect Password")
            
    else:
        print("Account is Inactive")
        
else:
    print("Username Not Found")