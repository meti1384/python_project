import random

def get_input():
    user_round=int(input("enter your round: "))
    list_of_words=[]
    while True:
        user_input=input("enter your guess list, Your guess must be isalpha: ")
        if "," in user_input:
            
            for word in user_input.split(","):
                if word.isalpha():
                    list_of_words.append(word)
                else:
                    print(f"this {word} not alpha.so this not exist in list")
        
        else:
            print("please split your word with \",\"")
            continue
        return list_of_words, user_round

def exist_word_in_list(word_list):
    user_input=input("enter your words: ").lower()
    while user_input not in word_list:
        print("this word not in list")
        print("please try again gussing")
        user_input=input("enter your words again: ")

    return user_input

def say_welcome(word_list):
    print("-"*15)
    print("welcom to guess game")
    print(f"All words: {word_list}")
    print("start guessing...")
    print("-"*15)

def run_game(word_list, round):
    flag=round
    say_welcome(word_list)

    ai_choice=random.choice(word_list)

    for _ in range(round):
        if exist_word_in_list(word_list)==ai_choice:
            print("-"*14)
            print("YOU WON!")
            return
        
        else:
            print("you guessed wrong! ")
            round -=1
            if round!=0:
                print("please try again")
            print("-"*14)
            

    
    print("YOU LOSE!")
    print(f"the correct word is: {ai_choice}")

list_words,round=get_input()
run_game(list_words,round)





