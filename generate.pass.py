import random, string, os
from termcolor import colored, cprint
import tkinter as tk



setting={
    "upper":True,
    "lower":True,
    "symbols":True,
    "numbers":True,
    "space":False,
    "lenght":8
}

def return_True(options, defualt):
    while True:
        user_input=input(f"Incloud {options} (DEFUALT:{defualt})? "
                         f"(y: yes n:no enter:{defualt}): ").lower()
        
        if user_input in ["n","y",""]:
            if user_input == "":
                return defualt
                        
            if user_input in ["y", "n"]:
                return user_input=="y"

        else:    
            print("Invalid input. (choose from (y, n, ""))")
            print("please try again")

MAX_LENGHT_PASS=20
Min_LENGHT_PASS=4

def get_lenght(options, defualt):
    while True:
        user_lenght=(input(f"enter your lenght: (defualt is {defualt}): "))
        if user_lenght=="":
            return defualt
        
        if user_lenght.isdigit() and Min_LENGHT_PASS<int(user_lenght)<MAX_LENGHT_PASS:
            
                return int(user_lenght)
        else:
            print(f"Invalid input. "
                f"number should be between {Min_LENGHT_PASS} and {MAX_LENGHT_PASS}")


def get_setting(settings):
    settings=setting.copy()
    for options, defualt in settings.items():

        if options != "lenght":
           settings[options]=return_True(options, defualt)

        else:
            settings[options]=get_lenght(options, defualt)
    return settings

            
def pass_generate(words):
    word=random.choice(words)

    if word=="upper":
        return random.choice(string.ascii_uppercase)
    elif word=="lower":
        return random.choice(string.ascii_lowercase)
    elif word=="symbols":
        return random.choice("""!@#$%^&*()?"`~><""")
    elif word=="numbers":
        return random.choice("1234567890")
    elif word=="space":
        return random.choice(" ")
        

def list_of_settings(settings):
    final_password=""
    user_list=(list(filter(lambda x: settings[x]==True, settings.keys())))
    for _ in range(settings["lenght"]):
        final_password += pass_generate(user_list)
    return final_password

def change_setting():
    while True:
        user_input=input("Do you want change setting: (y: yes n: no enter:yes)").lower()
        if user_input in ["y", "n", ""]:
            if user_input in ["n"]:
                return False
            user1=get_setting(setting)
            print("-"*20,"setting changed","-"*20, sep="")
            print()
            password_generator_loop(user1)
            return
        else:
            print("Invalid input. choose from (y, n, enter)")
            
def ask_user_to_generate_another_password():
    while True:
        user_input=input("Do you want another pass with this settings: "
                          "(y: yes n: no enter:yes)").lower()
        if user_input in ["y", "n", ""]:
            if user_input == "n":
                return False
            return True
            
        else:
            print("Invalid input. please choose from (y, n, enter)")
    

    
def password_generator_loop(settings):
    while True:
        print("-"*20)
        passwrod=(f"{list_of_settings(settings)}")
        word=("Password generate:") 
        print(colored(word,"green"),colored(passwrod, "red"))
        with open("practice.txt", "a") as append:
            append.write(f"{word} {passwrod} \n")
        if ask_user_to_generate_another_password()==False:
            change_setting()
            return
            
    

def run():
    os.system("cls")
    os.system("color")
    user1=get_setting(setting)
    password_generator_loop(user1)
    print("-"*20)
    cprint(colored("Thank you for choosing us!", "green"))

run()


