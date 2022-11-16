n = int(input('\033[35mMe diga um número qualquer:\033[m '))
r = n % 2
if r == 0:
    print('\033[1;37mO número {} é\033[m \033[34mPAR.\033[m'.format(n))
else:
    print('\033[1;37mO número {} é\033[m \033[32mÍMPAR\033[m'.format(n))
