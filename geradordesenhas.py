import secrets
print('### Gerador de Senhas ###\n')

lista_palavras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lista_numeros = ['1','2','3','4','5','6','7','8','9']
lista_simbolos = ['@', '!', '$', '&', '#', '%', '?']
senha_embaralhada = []
senha_ordenada = []

for cont in (lista_palavras, lista_numeros, lista_simbolos):
    for cont2 in range(5):
        senha_ordenada.append(secrets.choice(cont)) 

for cont in senha_ordenada:
    senha_embaralhada.append(secrets.choice(senha_ordenada))
    
print('Sua Senha é: ', ''.join(senha_embaralhada))


