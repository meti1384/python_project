import tkinter as tk
from tkinter import E,W,N,S,ttk


window=tk.Tk()

window.title("Change Temperature App")


user_fahr=tk.Label(
    master=window,
    text="Fahrenheit",
    
)

user_cels=tk.Label(
    master=window,
    text="Celsius",
     

)

user_show=tk.Label(
    master=window,
    text="Result will be shown here..."

)
user_cels.grid(row=1, column=0,pady=(10,20), padx=(10,20) )



fahren_input=tk.StringVar()

def show_result(*args):
    
    try:
        get_fahr=(fahren_input.get())
        user_show['text']=f"{(float(get_fahr)-32)/1.8}"
    except ValueError:
        if get_fahr=="":
            user_show['text']="Your input empty"
        else:    
            user_show['text']=f"You shold enter a number"

window.bind("<Return>", show_result)

user_input_fahr=ttk.Entry(
    master=window,
    width=50,
    textvariable=fahren_input

    
    
)    



user_fahr.grid(row=0, column=0, padx=(10,20) )
user_input_fahr.grid(row=0, column=1,)






clac_button=ttk.Button(
    master=window,
    text="Calc",
    width=10,
    command=show_result
   
)
clac_button.grid(row=0, column=2, padx=10, pady=10)
user_show.grid(row=1, column=1)

window.mainloop()