m = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for i in plaintext:
        if i in m:
            index = m.index(i)
            ciphertext += m[(index+shift)%len(m)]
        elif i in b:
            index = b.index(i)
            ciphertext += b[(index+shift)%len(b)]
        else:
            ciphertext += i
    return ciphertext
def decrypt_caesar(ciphertext:str, shift: int = 3) -> str:
    plaintext = ""
    for i in ciphertext:
        if i in m:
            index = m.index(i)
            plaintext += m[(index-shift)%len(m)]
        elif i in b:
            index = b.index(i)
            plaintext += b[(index- shift)%len(b)]
        else:
            plaintext += i
    return plaintext

print(encrypt_caesar(input()))
print(decrypt_caesar(input()))

