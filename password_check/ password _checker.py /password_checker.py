def check_password(password: str) :
    with open('password.txt', 'r') as file:
        common_password: list [str] = file.read().splitlines()

    for i, common_password in enumerate(common_password, start=1):
        if password == common_password:
            print(f'{password}: Not good a common one :x:   (#{i})')
            return

    print(f'{password}: good (unige)')

def main():
    user_password = input('Enter your password: ')
    check_password(user_password)

if __name__ == '__main__':
    main()
