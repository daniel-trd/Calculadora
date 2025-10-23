tentativas = 5

def cadastro():
    user = input('Cadastre seu usuario: ')
    password = input('Cadasre sua senha: ')
    print('Conta cadastrada com sucesso!')
    return user, password

user, password = cadastro()

while tentativas > 0:
    usuario = input('Usuário: ')
    senha = input('Senha: ')

    if user == usuario and password == senha:
        print('Login Efetuado com sucesso. Bem vindo!')
        break

    else:
        tentativas -= 1
        print(f'Credenciais invalidas tente novamente. Você ainda possui {tentativas}.')
