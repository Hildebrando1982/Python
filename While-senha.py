'''
Faça um programa em que se pede uma senha.
Usando a estrutura while 
Enquanto a senha for diferente de '12345seis'
escrever na tele senha incorreta. tente novamente
em caso de acerto da senha, escrever senha corrreta.

''''

senha = input('Digite a sua senha: ') 

while senha != '12345seis':
    print('Senha incorreta. Tente novamente.')
    senha = input('Digite a sua senha: ')
print('Senha correta. Acesso Liberado.')
