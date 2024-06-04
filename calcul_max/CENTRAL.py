import os


print('\n\n\n')

# modelando a tabela de apresentação...
print('+','-'*60,'+')
print("| Aqui é uma 'central' que unifica as calculadoras")
print("|")
print("| As regras são as seguintes:")
print("|")

#instrução de navegação
print("| para navegar entre as opções será usada:\n|\n| 0 - para voltar\n| 1 - para selecionar\n|")
print("| Na central de opções, para selecionar\n| a opção digite o numero do lado da opção.")
print('+','-'*60,'+')

#sistema para proseguir | primeira interação com o usuario...
x = False
while x == False:

    p = str(input('\npodemos proseguir? sim = y  não = n : '))
    
    if p == 'y':
        break
    elif p == 'n':
        continue

os.system('cls')

#outra modelagem
print('+','-'*60,'+')
print("| CENTRAL DE OPÇÕES")
print("| ")
print("| 1 - raiz quandrada")
print("| 2 - EM BREVE....\n\n")

selc = int(input("seleção: "))

while True:

    match selc:
        case 1:
            os.system('cls')
            from cal1 import*
        case 2:
            print('Não esta pronto, reinicie o programa')
            break