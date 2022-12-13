import random
NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''
    Pico : one digit is correct but not in correct position,
    Fermi: one digit is correct and in correct place,
    Bagel: No digit is correct
    ''')
    while True:
        secret_num = get_secrect_number()
        print('game started!')
        print(f'you have {MAX_GUESSES} times to guess!')

        num_guesses = 1

        while num_guesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('enter valid number')
                guess = input('> ')

            # hint = get_hint(guess, secret_num)
            # print(hint)
            num_guesses += 1


def get_secrect_number():
    numbers = list('0123456789')
    random.shuffle(numbers)
    sec_num = ''.join(numbers[:NUM_DIGITS])
    # another way :
    # sec_num = ''
    # for i in range(NUM_DIGITS):
    #     sec_num += numbers[i]
    return sec_num


if __name__ == "__main__":
    main()
