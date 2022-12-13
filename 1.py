# import random

# freq_1 = 0
# freq_2 = 0
# freq_3 = 0
# freq_4 = 0
# freq_5 = 0
# freq_6 = 0

# for i in range(6_000_000):
#     face = random.randrange(1, 7)
#     if face == 1:
#         freq_1 += 1
#     elif face == 2:
#         freq_2 += 1
#     elif face == 3:
#         freq_3 += 1
#     elif face == 4:
#         freq_4 += 1
#     elif face == 5:
#         freq_5 += 1
#     elif face == 6:
#         freq_6 += 1
# print(f'Face{"Frequency":>13}')
# print(f'{1:>4}{freq_1:>13}')
# print(f'{2:>4}{freq_2:>13}')
# print(f'{3:>4}{freq_3:>13}')
# print(f'{4:>4}{freq_4:>13}')
# print(f'{5:>4}{freq_5:>13}')
# print(f'{6:>4}{freq_6:>13}')


# import random


# def roll_dice():
#     die1 = random.randrange(1, 7)
#     die2 = random.randrange(1, 7)
#     return (die1, die2)


# def display_dice(dice):
#     die1, die2 = dice
#     print(f'player rolled {die1} + {die2} = {sum(dice)}')


# # first roll

# die_values = roll_dice()
# display_dice(die_values)


# sum_of_dice = sum(die_values)
# if sum_of_dice in (7, 11):
#     game_status = 'WON'
# elif sum_of_dice in (2, 3, 12):
#     game_status = 'LOST'
# else:
#     game_status = 'CONTINUE'
#     target = sum_of_dice
#     print('target is', target)

# while game_status == 'CONTINUE':
#     input('Press Enter to continue...')

#     die_values = roll_dice()
#     display_dice(die_values)
#     sum_of_dice = sum(die_values)
#     if sum_of_dice == target:
#         game_status = 'WON'
#     elif sum_of_dice == 7:
#         game_status = 'LOST'

# if game_status == 'WON':
#     print('Player wins')

# else:
#     print('Player loses!')


# def myfunc():
#     return "hi"


# print(myfunc())
toatl = 0
for i in range(6):
    toatl += i

print(toatl)
