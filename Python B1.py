def insecure_function(password):
    assert password != '', "Password should not be empty"

password = input("Enter your password: ")
insecure_function(password)
