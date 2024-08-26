# print("hi")
# word_list=['apple','beautiful','potato']
import random
import hangman
import words_list
lives = 5
choosen_word = random.choice(words_list.words)
print(choosen_word)
dash_lines=[]
for letter in choosen_word:
    dash_lines +='_'
print(dash_lines)
game_over = False
while not game_over:

    user_guss = input("guess the letter: ").lower()
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == user_guss:
            dash_lines[position]=user_guss
    print(dash_lines)
    if user_guss not in choosen_word:
        lives= lives-1
        if lives == 0:
            game_over = True
            print("you loose")
    if '_' not in dash_lines:
        game_over = True
        print("you win !!")
    print(hangman.stages[lives])
