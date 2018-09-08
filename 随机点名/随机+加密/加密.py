import base64

my_secret = '2 欧阳修 6'
#加密
encode_secret = base64.b64encode(my_secret.encode('utf-8'))
#解密
decode_secret = base64.b64decode(encode_secret)
print(encode_secret)
print(decode_secret)
print(decode_secret.decode('utf-8'))
