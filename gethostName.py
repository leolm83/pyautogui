from socket import *
target = input("digite a URL")
nome = gethostbyname(target)
print(nome)
