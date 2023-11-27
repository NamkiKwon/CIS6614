import os

password = input("Enter your password: ")
os.system(f'echo {password} > password.txt')
