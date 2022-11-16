try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
#excetp é para demonstrar o erro por excessão e pode ser utilizados quantos except forem necessários.
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:#Se der certo, acontece. É opcional
    print(f'O resultado foi {r}')
finally:#Vai acontecer sempre independentemente do resultado, porém finally é opcional
    print('Volte sempre! Muito obrigado!')
