def EncryptAffine(plantext, key1, key2):
    dictt={"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8,"j":9,
           "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19,
           "u":20, "v":21, "w":22, "x":23, "y":24, "z":25
           }
    ciphertext = ""
    for x in plantext :
        sum = ((dictt[x] * key1) + key2) %26
        for v,k in dictt.items():
            if sum == k :
                ciphertext = (ciphertext + v).upper()
    print(ciphertext)


def DecryptAffine(ciphertext, key1, key2, n):
    dictt={"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8,"j":9,
           "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19,
           "u":20, "v":21, "w":22, "x":23, "y":24, "z":25
           }
    plaintext = ""
    ciphertext = ciphertext.lower()
    key_1 = BEucliedes(key1, n)
    for x in ciphertext :
        sum = ((dictt[x] - key2) * key_1) %26
        for v,k in dictt.items():
            if sum == k :
                plaintext = plaintext + v
    print(plaintext)