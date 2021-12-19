def modulus(num):
    # type: (int) -> int
    if num < 0:
        num = abs(num) % 95
        num *= -1
    else:
        num %= 95
    return num


def shifter(unshifted, key, isEncrypt):
    # type: (str, int, bool) -> str
    shiftedStr = ""
    if key == 0:
        return unshifted
    else:
        key = modulus(key)
        for chars in unshifted:
            if isEncrypt:
                newOrd = ord(chars) + key
            else:
                newOrd = ord(chars) - key

            if newOrd < 127 and newOrd > 31:
                shiftedStr += chr(newOrd)
            elif newOrd < 32:
                shiftedStr += chr(newOrd + 95)
            else:
                shiftedStr += chr(newOrd - 95)
        return shiftedStr

def encrypt(plain, key):
    # type: (str, int) -> str
    return shifter(plain, key, True)


def decrypt(encrypted, key):
    # type: (str, int) -> str
    return shifter(encrypted, key, False)


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
