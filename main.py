def encrypt(plain, key):
    # type: (str, int) -> str

    message = ""
    for letter in plain:
        if letter.isalpha():
            num = ord(letter) + key
            if letter.isupper():
                if num > 90:
                    num -= 25
            else :
                 if num > 122:
                     num += 25
            message += chr(num)
   
    return message
    pass


def decrypt(encrypted, key):
    # type: (str, int) -> str

    message = ""
    for letter in encrypt:
        if letter.isalpha():
            num = ord(letter) - key
            if letter.isupper():
                if num < 65:
                    num += 25
            else :
                 if num < 97:
                     num -= 25
            message += chr(num)
   
    return message
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
