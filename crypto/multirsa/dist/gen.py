from Crypto.Util.number import getPrime
from random import randint

flag = "Cyberthon{REDACTED}"
flagint = int.from_bytes(flag.encode(), "big")


e = 5

for i in range(e):
    p = getPrime(2048)
    q = getPrime(2048)
    n = p*q
    x = randint(1, 1000000000000)
    flagenc = pow(flagint * x, e, n)
    print(flagenc, x, n)