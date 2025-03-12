import random

# def fortune():
#     random_fortune = random.randint(0, 7)
#     if (random_fortune == 1):
#         print(f'Vc terá sucesso! {random_fortune}')
#     elif (random_fortune == 2):
#         print(f'Vc terá fama {random_fortune}')
#     elif (random_fortune == 3):
#         print(f'Vc terá dinheiro {random_fortune}')
#     elif (random_fortune == 4):
#         print(f'Vc terá amores {random_fortune}')
#     elif (random_fortune == 5):
#         print(f'Vc terá filhos {random_fortune}')
#     elif (random_fortune == 6):
#         print(f'Vc terá orgulho {random_fortune}')
#     else:
#         print(f'Vc terá tudo de bom! {random_fortune}')
# fortune()

options = [
  'Dont pursue happiness – create it.',
  'All things are difficult before they are easy.',
  'The early bird gets the worm, but the second mouse gets the cheese.',
  'If you eat something and nobody sees you eat it, it has no calories.',
  'Someone in your life needs a letter from you.',
  'Dont just think. Act!',
  'Your heart will skip a beat.',
  'The fortune you search for is in another cookie.',
  'Help! Im being held prisoner in a Chinese bakery!'
]


def fortune():
    random_fortune = random.randint(0, len(options) - 1)
    print(options[random_fortune])


fortune()
fortune()
