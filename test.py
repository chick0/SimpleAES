from time import time
from SimpleAES import encrypt
from SimpleAES import decrypt


enc_test = input("enc_test=").encode(encoding="utf-8")

t = time()
e = encrypt(data=enc_test)
print("\n".join([
    "=" * 60,
    f"* Encrypt Result : {e.data}",
    f"* IV             : {e.iv[:8]}...",
    f"* KEY            : {e.key[:8]}...",
    f"* Time           : {time() - t}",
]))

t = time()
d = decrypt(
    key=e.key,
    iv=e.iv,
    data=e.data
)
print("\n".join([
    "=" * 60,
    f"* Decrypt Result : {d}",
    f"* Is same?       : {d == enc_test}",
    f"* Time           : {time() - t}"
]))
