def encrypt(plain, key):
    # type: (str, int) -> str

    # TODO your code will be here
    pass


def decrypt(encrypted, key):
    # type: (str, int) -> str

    # TODO your code will be here
    pass


if __name__ == '__main__':
    plain = "Hello, World!"
    key = 10

    encrypted = encrypt(plain, key)
    decrypted = decrypt(encrypted, key)

    print("plain: %s " % plain)
    print("key:  %d " % key)
    print("encrypted:  %s " % encrypted)
    print("decrypted :  %s " % decrypted)
