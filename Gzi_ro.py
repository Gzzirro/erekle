def signup():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    email = input("Enter your email address: ")
    
 
    if not (8 <= len(username)):
        print("Username must be 8 characters long.")
        return None
    
  
    if not (8 <= len(password)):
        print("Password must be 8 characters long.")
        return None
    

    print("You signed up with:")
    print("Username:", username)
    print("Password:", password)
    print("Email:", email)
    
    return username

# Example usage:
new_user = signup()
if new_user:
    print("Welcome,", new_user)