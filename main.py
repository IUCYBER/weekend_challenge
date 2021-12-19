def encrypt(plain: str, key: int):
    # type: (str, int) -> str

    # TODO your code will be here
    encryptedMsg = ""
    for char in plain:
        encryptedMsg += chr((ord(char) - 32 + key) % 95 + 32)
    return encryptedMsg
    pass


def decrypt(encrypted: str, key: int):
    # type: (str, int) -> str

    # TODO your code will be here
    decryptedMsg = ""
    for char in encrypted:
        decryptedMsg += chr((ord(char) - 32 - key) % 95 + 32)
    return decryptedMsg
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
