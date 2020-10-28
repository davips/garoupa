from cruipto.linalg import lazydecrypt, lazyhash, lazyencrypt

txt = "ut".encode()
key = "a".encode()

print("text:", txt)
print("hash:", lazyhash(txt))
encoded = lazyencrypt(txt, key)
print("encoded:", len(encoded), encoded)
decoded = lazydecrypt(encoded, key)
print("decoded:", len(decoded), decoded.decode())
