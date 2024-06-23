import string
import secrets

def contains_uppercase(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True

    return False

def contains_symbol(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True

    return False

def generate_password(length: int, symbol: bool, uppecase: bool) -> str:
    combination : str =  string.ascii_lowercase + string.punctuation

    if symbol:
        combination += string.punctuation
    if uppecase:
        combination += string.ascii_uppercase

    combination_length = len(combination)
    new_password: str = ''

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password

if __name__ == '__main__':
    for i in range(1,10):
        new_password = generate_password(10, symbol=True, uppecase=True)
        specs: str =f'U:{contains_uppercase(new_password)}, S:{contains_symbol(new_password)}'
        print(f'{i}: {new_password} ({specs})')
