def leiaint(msg):
    while True:
        try:
            i = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return i


def leiafloat(msg):
    while True:
        try:
            f = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return f


#programa principal
i = leiaint('Digite um inteiro: ')
f = leiafloat('Digite um real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {f}.')
