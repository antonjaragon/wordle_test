#%%
import json
import numpy as np
ROUNDS = 6
WORD_LENGTH = 5
N = 100
won_games = 0

for i in range(N):
    # print(i+1)
    
    # dictionary = json.load(open('words_dictionary.json')).keys()
    dictionary = json.load(open('common.json'))["commonWords"]
    

    dictionary = [word for word in dictionary if len(word) == WORD_LENGTH]

    # delete random 10% from dictionary
    # dictionary = np.random.choice(dictionary, int(len(dictionary)*0.9), replace=False)
    
    # daily_word = 'happy'
    daily_word = np.random.choice(dictionary,1,replace=False)[0]
    # print(daily_word in dictionary)


    round_i = 0

    # color_matrix = []
    # letters_matrix = []

    contains = {}
    not_contains = []
    known_letters = {}
    known_letters_not_in_position = {}

    while round_i < ROUNDS:
        # guess = input(f"Round {round_i+1}:")
        # select five random indices from dictionary
        guesses = np.random.choice(dictionary, 5)
        # print(guesses)
        # guess is the word in guesses with a bigger number of different letters and then the word with the max number of vowels
        guess = guesses[np.argmax([len(set(guesses[i])) for i in range(len(guesses))])]
        # print(guess)
                        
        # print(f"Round {round_i+1}: {guess}")
        # if len(guess) != 5 or guess not in dictionary:
        #     pass
            # print("Invalid word")
        if daily_word == guess:
            won_games += 1

            # print(f"You won! The word was {daily_word}")
            break
        else:
            # print(f"wrong guess")
            round_i += 1

            for letter in guess:
                if letter in daily_word:
                    appereances_guess = guess.count(letter)
                    appereances_daily_word = daily_word.count(letter)
                    # print(appereances_guess)
                    # print(appereances_daily_word)
                    if appereances_guess <= appereances_daily_word:
                        contains[letter] = appereances_guess
                    else:
                        contains[letter] = appereances_daily_word
                    if daily_word.index(letter) == guess.index(letter):
                        known_letters[letter] = daily_word.index(letter)
                    else:
                        known_letters_not_in_position[letter] = daily_word.index(letter)
                else:
                    not_contains.append(letter)

            # print(f"Contains: {contains}")
            # print(f"Known letters: {known_letters}")

            # filter dictionary by letters in contains, >= than number of appereances for each letter
            dictionary = [word for word in dictionary if all([word.count(letter) >= contains[letter] for letter in contains])]
            # filter dictionary by letters is not contains
            dictionary = [word for word in dictionary if all([letter not in word for letter in not_contains])]            
            # filter dictionary by known letters positions
            dictionary = [word for word in dictionary if all([word[known_letters[letter]] == letter for letter in known_letters])]
            # filter dictionary by known letters not in position
            dictionary = [word for word in dictionary if all([word[known_letters_not_in_position[letter]] == letter for letter in known_letters_not_in_position])]


            # print(len(dictionary))

    if round_i == ROUNDS:
        print(f"{i+1}: Lost")
    else:
        print(f"{i+1}: Victory")

print(f"Victory percentage: {won_games/N}")
# %%
