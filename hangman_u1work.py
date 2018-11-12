import random

"""
select word for guessing  - DONE
print word on the screen with not guessed letters and with guessed - DONE
ask for input from user, check that input is correct, use '-" for quit, if '!' - guess all word  = DONE 
put on screen hungman  - DONE
check if letter in "word" - DONE
add letter to list of named letters = DONE
check that user named all letters in 'word'
check that user used all given tries = DONE
define numbers of tries for user = DONE
check if user wants to start new game - DONE
check that user wants still to play:
    check if user wants to quit    = DONE
    user used all tries            = DONE
    user guessed all letters       = DONE

"""

h_pictures = [
    """
   +-----+
         |
         |
         |
         |
         |
         |
=========| 
    """,
    """
   +-----+
   |     |
         |
         |
         |
         |
         |
=========| 
    """,
    """
   +-----+
   |     |
   0     |
         |
         |
         |
         |
=========| 
    """,
    """
   +-----+
   |     |
   0     |
    \    |
         |
         |
         |
=========| 
    """,
    """
   +-----+
   |     |
   0     |
   |\    |
         |
         |
         |
=========| 
    """,
    """
   +-----+
   |     |
   0     |
  /|\    |
         |
         |
         |
=========| 
    """,
    """
   +-----+
   |     |
   0     |
  /|\    |
   |     |
         |
         |
=========| 
    """,
    """
   +-----+
   |     |
   0     |
  /|\    |
   |     |
  /      |
         |
=========| 
    """,
    """
   +-----+
   |     |
   0     |
  /|\    |
   |     |
  / \    |
         |
=========| 
    """,
    """
   +-----+
   |     |
   0     |
  /|\    |
   |     |
  /'\    |
         |
=========| 
   """
]


def select_word():
    text = open('74-0.txt', encoding='UTF-8')
    text = text.read()

    symbols_to_remove = "-!@#*:;%?.'_,/()1234567890"

    for char in symbols_to_remove:
        text = text.replace(char, '')
    text = text.replace('\n', ' ').lower().split(' ')

    li = list()
    words_list = [w for w in text if w not in li and len(w) == 10]
    word = random.choice(words_list).upper()
    return word


def calculate_max_try_number(word):
    count_tries = len(word)
    print("You have total {0} tires to guess the word".format(count_tries), "\n")
    return count_tries


def game_print(h_pictures, missed_letters, correct_letters, word):
    """

    :type h_pictures: object in list by index corresponding to the number of the failed tries
    """
    if len((missed_letters + correct_letters)) > 0:
        print("You already tired following letters: " + missed_letters + correct_letters)

    print(h_pictures[(len(missed_letters) // 2)])

    if len(correct_letters) == 0:
        hidden_letter = '_' * len(word)

    if len(correct_letters) >= 1:
        hidden_letter = ''
        for guessed_letter in word:  # replaces blanks with corectly guessed letters
            if guessed_letter in correct_letters:
                hidden_letter = hidden_letter + guessed_letter
            else:
                hidden_letter = hidden_letter + '_'

    for letter in hidden_letter:  # show the secret word with spaces in between the letters
        print(letter, end=' ')
    print()


def user_input():
    while True:
        guessed_letter = str(input("Please, enter letter, '-' to quit, '+' to start new game, "
                                   "'!' to name all word here: "))
        guessed_letter.upper()
        if guessed_letter == '-':
            print("Your game is over!")
            quit()
        elif guessed_letter == '!':
            guessed_letter = input("Enter whole word, if you know it: ").upper()
            return guessed_letter.upper()
        elif guessed_letter == '+':
            guessed_word = guessed_letter
            return guessed_word
        elif guessed_letter.isalpha() and len(guessed_letter) == 1:
            return guessed_letter.upper()
        else:
            print("Wrong input!!!")


def guessed_word_check(word, guessed_letter, correct_letters):
    if guessed_letter in word:
        guessed_word = ''
        for guessed_letter in word:
            if guessed_letter in correct_letters:
                guessed_word += guessed_letter
                if guessed_word == word:
                    print("Yes, you guessed it! The secret word is: {0}".format(guessed_word))
                    return False


def new_game(guessed_word, word):
    while True:
        if guessed_word == '+':
            print("Starting a new game...")
            main()
        elif guessed_word == word:
            print("Starting a new game...")
            main()
        elif guessed_word == word:
            print("Do you like to continue? y/n")
            decision = input("Do you like to continue? '+' to continue or '-' to end the game.")
            if decision == '+':
                main()
            elif decision == '-':
                main()
            else:
                print("Wrong input!!!")


def main():
    missed_letters = ''
    correct_letters = ''
    word = select_word()
    print(word)
    count = calculate_max_try_number(word)

    while True and count != 0:

        game_print(h_pictures, missed_letters, correct_letters, word)

        guessed_letter = user_input()
        count -= 1

        if guessed_letter == '+':
            guessed_word = guessed_letter
            new_game(guessed_word, word)

        if guessed_letter == word:
            print("Yes, you guessed it! The secret word is: {0}".format(word))
            guessed_word = guessed_letter
            new_game(word, guessed_word)

        if guessed_letter in word and count > 0:
            correct_letters = correct_letters + guessed_letter + ' '
            print("You guessed, {0} is in secret word!".format(guessed_letter))
            guessed_word = guessed_word_check(word, guessed_letter, correct_letters)
            if guessed_word == word:
                new_game(guessed_word, word)

        if guessed_letter not in word or count == 0:

            missed_letters = missed_letters + guessed_letter + ' '

            if count > 0:
                print("Your guess '{}' is not in secret word!".format(guessed_letter))

            if (len(missed_letters) / 2) == len(h_pictures) - 1:
                game_print(h_pictures, missed_letters, correct_letters, word)
                print("You are out of your " + str(len(missed_letters) // 2) + " tires! Your game is over!")
                proceed_game = input("Press '+' to play the game again, or press '-' to exit the game.")
                if proceed_game == '+':
                    guessed_word = proceed_game
                    new_game(guessed_word, word)
                if proceed_game == '-':
                    exit()


if __name__ == "__main__":
    print('H A N G M A N')
    main()
