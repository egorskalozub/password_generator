import os.path
from random import randrange
password = ''


def genPass():
    global password
    while True:
        lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
        upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = '0123456789'
        signs = '!@#$%^&*()'
        try:
            l = int(input("What is the length of the password?"))
            what_pass = input("What is the password for?")
            while l > 0:
                l -= 1
                choice = randrange(4)
                if choice == 0:
                    password += lower_alphabet[randrange(len(lower_alphabet))]
                elif choice == 1:
                    password += upper_alphabet[randrange(len(upper_alphabet))]
                elif choice == 2:
                    password += numbers[randrange(len(numbers))]
                elif choice == 3:
                    password += signs[randrange(len(signs))]
                else:
                    print('There is something wrong with the password')
            return [password, what_pass]
        except ValueError:
            print('Invalid length')


def viewPassword():
    try:
        with open('pass.txt') as f:
            print(f.readlines())
    except IOError:
        print("Error: file not accessible")


def addPassword():
    file_exists = os.path.exists('pass.txt')
    there_is = False
    with open('pass.txt') as f:
        old_pass = f.read()
    if old_pass == '':
        there_is = False
    else:
        there_is = True
    new_pass, what_pass = genPass()
    if file_exists == True and there_is == True:
        with open('pass.txt', 'a') as f:
            if not old_pass.endswith('\n'):
                f.write('\n')
            f.write(f'{what_pass}:{new_pass}')
    else:
        with open('pass.txt', 'a') as f:
            if not old_pass.endswith('\n'):
                f.write(f'{what_pass}:{new_pass}\n')


def deletePassword():
    try:
        with open('pass.txt') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                a = lines[i]
                a = a.split(':')
                a = a[0]
                print(f'{i+1}.{a}')
        choice = int(input('what do you want to delete?'))
        with open("pass.txt", 'w') as f:
            for number, line in enumerate(lines):
                if number != choice-1:
                    f.write(line)
                else:
                    print(f'deleted: {line}')

    except IOError:
        print("Error: file not accessible")


def welcomeText():
    print('Hello, this is  a password generator')
    print('Here is options:')


def main():
    welcomeText()
    while True:
        print('======================')
        print('1. View my passwords')
        print('2. Create a new password')
        print('3. delete a password')
        print('4. exit')
        print('======================')
        a = int(input(': '))
        try:
            if a == 1:
                viewPassword()
            elif a == 2:
                addPassword()
            elif a == 3:
                deletePassword()
            elif a == 4:
                print('Thank you for using the password generator')
                break
            else:
                print('Out of range')
        except ValueError:
            print('ValueError')


if __name__ == "__main__":
    main()
