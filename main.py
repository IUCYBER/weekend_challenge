alphabet = [chr(i) for i in range(32,127)]

def encrypt(plain, key):
    # type: (str, int) -> str

    # TODO your code will be here
    encrypted_text = ""
    key = key % len(alphabet)
    for i in plain:
        if key + alphabet.index(i) >= len(alphabet):
            new_index = key + alphabet.index(i) - len(alphabet)
        else:
            new_index = key + alphabet.index(i)
        encrypted_text += alphabet[new_index]
    return encrypted_text
    pass


def decrypt(encrypted, key):
    # type: (str, int) -> str

    # TODO your code will be here
    decrypted_text = ""
    key = key % len(alphabet)
    for i in encrypted:
        if key > alphabet.index(i):
            new_index = len(alphabet) + alphabet.index(i) - key
        else:
            new_index = alphabet.index(i) - key
        decrypted_text += alphabet[new_index]
    return decrypted_text
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
