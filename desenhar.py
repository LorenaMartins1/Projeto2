print('#'*8,"RETÃNGULO",'#'*8)
largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

print('=' * largura)

for _ in range(altura-2):
    print('|' + ' ' * (largura-2) + '|')

print('=' * largura)
