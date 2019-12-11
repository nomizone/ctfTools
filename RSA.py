from Crypto.Util.number import long_to_bytes

c = 0x1afe93e83137e76d2226d97c40512040
d = 31337
n = 0x50618b968b8603e9e870e7d878e866e3 #106844723640410863741046875242417907427

plain = pow(c, d, n)
print(long_to_bytes(plain))
