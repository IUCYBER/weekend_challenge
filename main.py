def encrypt(plain, key):
    # type: (str, int) -> str

    # TODO your code will be here
    # this is new comment
    # add comment to test workflow
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

    if encrypted or decrypted is None:
        exit(1)

    print("plain: %s " % plain)
    print("key:  %d " % key)
    print("encrypted:  %s " % encrypted)
    print("decrypted :  %s " % decrypted)
