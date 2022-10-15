print("hello")
participante = {'name':'Gabriele','country':'Brasil'}
print(participante)
if 3>2:
    print('funciona!')
if 5 > 2: 
        print('5 é maior que 2')
else:
        print('5 não é maior que 2')
name = 'Sonja'
if name == 'Ola':
    print('Olá Ola!')
elif name == 'Sonja':
    print('Olá Sonja!')
else:
    print('Olá estranho!')  
# esse codigo verifica o volume   
volume = 87
if volume < 20: 
    print("Está um pouco baixo")
elif 20 <= volume < 40: 
    print("Está bom para música ambiente")
elif 40 <= volume < 60: 
    print("Perfeito, posso ouvir todos os detalhes")
elif 60 <= volume < 80: 
    print("Ótimo para festas!")
elif 80 <= volume < 100: 
    print("Está muito alto!")
else: 
    print("Meus ouvidos doem! :(")
def hi():
    print('olá')
    print('tudo bem')
hi()
hi()
def hi(name):
    if name == 'Ola':
        print('Olá Ola!')
    elif name == 'Sonja':
        print('Olá Sonja!')
    else:
        print('Olá estranho!')

hi('Ola')
hi('Sonja')
def hi(name):
    print('Olá ' + name + '!')
hi('Gabriele')
girls = ['Gabriele', 'Andressa', 'Grazi', 'Isabela']
for name in girls:
    hi(name)
    print('proxima')
for i in range(1, 6):
    print(i)





