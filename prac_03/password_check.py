MIN_LENGTH = 5


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print('*' * len(password))


def get_password():
    password = input("Enter a Password {} characters long: ".format(MIN_LENGTH))
    while len(password) < MIN_LENGTH:
        password = input("Enter a Password {} characters long: ".format(MIN_LENGTH))
    return password


main()
