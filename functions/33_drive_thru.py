
def get_item(n):
    if (n == 1):
        print(f'#{n} Você escolheu o Cheeseburger 🍔')
    elif (n == 2):
        print(f'#{n} Você escolheu 🍟 Fries')
    elif (n == 3):
        print(f'#{n} Você escolheu 🥤 Soda')
    elif (n == 4):
        print(f'#{n} Você escolheu 🍦 Ice Cream')
    elif (n == 5):
        print(f'#{n} Você escolheu 🍪 Cookie')
    else:
        print('O número escolhido não é válido!')


def welcome():
    print('Seja bem vindo(a)!')
    print('Aqui está o menu:')
    print('1. 🍔 Cheeseburger')
    print('2. 🍟 Fries')
    print('3. 🥤 Soda')
    print('4. 🍦 Ice Cream')
    print('5. 🍪 Cookie')


welcome()

option = int(input('Qual o seu pedido?'))
print(get_item(option))
