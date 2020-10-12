# читаем файл по рабоче-крестьянки
file = open("just-file.txt", "rb")

while True:
    bytes = file.read(5)
    print(bytes)
    if bytes == b'': break
file.close()


### читаем файл по питоновски
with open("just-file.txt", "rb") as f:
    bytes = f.read(5)
    while bytes != b'':
        print(bytes)
        bytes = f.read(5)
