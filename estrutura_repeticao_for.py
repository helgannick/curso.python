texto = input('Informe um texo: ')
VOGAIS = 'AEIOU'

for letras  in texto:
    if letras.upper() in VOGAIS:
        print(letras, end='')

print() #adicionar uma quebra de linha