import base64
MESSAGE = 'EUIBBxoQEB1CFxANSkIVABwSAUkdEBdUBQkeFxgUAAsWEAoXTQABBhwWGAtVFxwXTQAUFBYBAR0W EAoXTQwcEQsWEQdTXFUQRkVVExobHAtHVV1SBBFVUkNTUhtfXF9UAQAWVVVTUhxQUlJeHhZVUkNT Uh1QVlUQRkVVFBYcUk4LEBdAAwtTVQQ='
KEY = 'jerrysun1007'
out = ""
m = base64.b64decode(MESSAGE)

for i in range(len(m)):
    out += chr(m[i] ^ ord(KEY[i % 12]))

print(out)
