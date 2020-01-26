import string

st = input()
to_un_hex = []

# ------------------------------------dehexing------------------------------------------
for i in range(0, len(st), 2):
    to_un_hex.append(st[i] + st[i + 1])
uhex = []
for i in range(len(to_un_hex)):
    new = bytearray.fromhex(to_un_hex[i]).decode()
    uhex.append(new)
strin = ""
for ele in range(len(uhex)):
    strin += (str(uhex[ele]))
retap = []
# ===============================undoingtheoperation(XOR)==============================================================
for op in range(len(strin)):
    neardone = chr(ord(strin[op]) ^ 10)
    retap.append(neardone)

# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,shifting,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
for i in range(len(retap)):
    if retap[i].isupper() is True:
        pos = upper.index(retap[i])
        retap[i] = upper[(pos - 3)]
    if retap[i].islower() is True:
        pos = lower.index(retap[i])
        retap[i] = lower[(pos - 3)]
    if retap[i].isdigit() is True:
        pos = digits.index(retap[i])
        retap[i] = digits[(pos - 3)]
needed = ""
for d in range(len(retap)):
    needed += retap[d]
print(needed)