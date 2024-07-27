# import random
# list_of_chance=["r","p","s"]

# dict1={
#     "r":"Rock",
#     "s":"Scissors",
#     "p":"Paper"
# }
# user_score=0
# ai_score=0
# i=0
# finall_round=int(input("enter your round: "))
# while i != finall_round:
#     user_input=input("please enter from Rock,Scissors,paper(r,s,p): ").casefold()
#     ai_input=random.choice(list_of_chance)

#     if user_input in list_of_chance:
#         print(f"your choice is {dict1[user_input]} ai choice is {dict1[ai_input]}")
#         if user_input==ai_input:
#             print("tie")
#         elif user_input == "r" and ai_input=="s":
#             print("user+1")
#             user_score+=1
            
#         elif user_input == "s" and ai_input=="p":
#             print("user+1")
#             user_score+=1
#         elif user_input == "p" and ai_input=="r":
#             print("user+1")
#             user_score+=1
            
#         else:
#             print("ai+1")
#             ai_score +=1
            
#     else:
#         print("invalid input")
#         i-=1
#     i +=1

#     print(f"user_score is {[user_score]} ai_score is {[ai_score]}")
#     print("\n",15*"*","\n")

# if user_score>ai_score:
#     print(f"user won! with score {[user_score]}")
# elif user_score<ai_score:
#     print(f"ai won! with score {[ai_score]}")
# else:
#     print("tied")





import random
import tkinter as tk

list_of_chance=["r","p","s"]

dict1={
    "r":"Rock",
    "s":"Scissors",
    "p":"Paper"
}

def running():
    user_score=0
    ai_score=0
    while True:
        try:
            finall_score=int(input("enter your finall_score: "))
            break
        except ValueError:
            print("you should input an integer number please try agian")
            continue
    while True:
        user_input=input("please enter from Rock,Scissors,paper(r,s,p): ").casefold()
        ai_input=random.choice(list_of_chance)

        if user_input in list_of_chance:
            print(f"your choice is {dict1[user_input]} ai choice is {dict1[ai_input]}")
            if user_input==ai_input:
                print("tie")
            elif user_input == "r" and ai_input=="s":
                print("user+1")
                user_score+=1
                
            elif user_input == "s" and ai_input=="p":
                print("user+1")
                user_score+=1
            elif user_input == "p" and ai_input=="r":
                print("user+1")
                user_score+=1
                
            else:
                print("ai+1")
                ai_score +=1
                
        else:
            print("invalid input")
        
        print(f"user_score is {[user_score]} ai_score is {[ai_score]}")
        print("\n",15*"*","\n")
        if user_score==finall_score or ai_score==finall_score:
            return user_score, ai_score
        
def add_result_file(word,user_score,ai_score,i):  
    with open("result.txt","a") as results:
                results.write(f"The result of round {i}: (user_score is {[user_score]}) and "
                            f"(ai_score is {[ai_score]}) so {word} WIN!!\n")



def ask_user_run_again(i):
    
    while True:
            user_again=input("do you want play again: (y:yes/n:no/enter:yes) ").lower()


            if user_again in ["", "yes"]:
                user_scoree, ai_scoree=running()
                i += 1
                return user_scoree, ai_scoree,i

            if user_again == "n":
                    with open("result.txt","a") as results:
                            
                            results.write(f'{30*"-"} This Match END!! ----{30*"-"}\n\n')
                           

                    print("-"*10)
                    print("Thank you for choosing us!")
                    
                    return False

            else:
                try:
                    raise ValueError
            
                except ValueError:
                    print("please choose again from (y:yes/n:no/enter:yes)")
                    print("-"*10)
                    continue
            
def show_result(user_score, ai_score, i):      
    word=""
    if user_score>ai_score:
        word="user"
        print(f"{word} won! with score {[user_score]}")
        
    else:
        word="ai"
        print(f"{word} won! with score {[ai_score]}")

    add_result_file(word,user_score,ai_score,i)

    rrrr=ask_user_run_again(i)
    if rrrr == False:
         return
    usersc, aisc, x =rrrr
    show_result(usersc, aisc, x)
    
    

user_score, ai_score=running()
show_result(user_score, ai_score, i=1)


                
    

# for i in range(1,11):
#     print()
#     for x in range(1,11):
#         print(f"{i*x:3}", end=" ")
    