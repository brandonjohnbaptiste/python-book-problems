import random


# standard guessing game
def guessing_game():
    rand_num = random.randint(0, 100)

    # Loop until number found
    while True:
        guess = int(input('Enter Your Guess: '))

        if guess == rand_num:
            print(f'{guess} is the correct guess!')
            break
        elif guess < rand_num:
            print('Guess too Low')
        else:
            print('Guess too High')


def guess_game_max_guess(max_guesses):
    count = 0
    rand_num = random.randint(0, 100)

    # loop until the number is guessed or user runs out of guesses
    while count < max_guesses:
        guess = int(input('Enter Your Guess: '))

        # TODO: check guesses are left, then run game logic
        if guess == rand_num:
            print(f'{guess} is the correct guess!')
            break
        elif guess < rand_num:
            count += 1
            print('Guess too Low')
            print(f'You have {max_guesses - count} guesses left')
        else:
            count += 1
            print('Guess too High')
            print(f'You have {max_guesses - count} guesses left')

    print('Maximum guesses reached you loose!')


if __name__ == '__main__':
    guess_game_max_guess(3)
