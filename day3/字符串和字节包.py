
name = "你真是顶呱呱！"
print(name.encode(encoding="utf-8").decode(encoding="utf-8"))#转换成字节包，再转回来
# name = b'\xe4\xbd\xa0\xe7\x9c\x9f\xe6\x98\xaf\xe9\xa1\xb6\xe5\x91\xb1\xe5\x91\xb1\xef\xbc\x81'
# print(name.decode())