import tkinter as tk


window=tk.Tk()





lbl_show=tk.Label(
    master=window,
    text="0",
    height=3
    
    
    
)
lbl_show.grid(row=0, column=0, columnspan=4)


def is_desimal(current):  
    for l in current[::-1]:
        if l == ".":
            return True
        if l in ["-", "+", "*"]:
            return False
    return False



def show_result(btn_input):
    current=lbl_show['text']
    if len(current) == 1 and btn_input == "=" :
        pass
    elif current == "0":
        lbl_show["text"] = btn_input
    elif btn_input == "=":
        lbl_show['text']=str(round(eval((current)),2))
    elif btn_input == "C":
        lbl_show["text"]="0"
        
    elif btn_input=="." and not is_desimal(current) :
        lbl_show["text"] += btn_input

    else:
        if btn_input in ["-", "+", "*"] and current[-1] in ["-", "+", "*"] :
            lbl_show["text"]=current[:-1]+btn_input
        elif not current[-1] in ["-", "+", "*"]:
            lbl_show["text"] += btn_input
        else:
            lbl_show["text"] += btn_input

    

calc_keys=[
    {
        "text":"7",
        "command":lambda: show_result(("7"))
    },
    {
        "text":"8",
        "command":lambda: show_result("8")
    },
        {
        "text":"9",
        "command":lambda: show_result("9")
    },
        {
        "text":"+",
        "command":lambda: show_result("+")
    },
        {
        "text":"4",
        "command":lambda: show_result(("4"))
    },
        {
        "text":"5",
        "command":lambda: show_result(("5"))
    },
        {
        "text":"6",
        "command":lambda: show_result(("6"))
    },
        {
        "text":"-",
        "command":lambda: show_result("-")
    },
        {
        "text":"1",
        "command":lambda: show_result(("1"))
    },
        {
        "text":"2",
        "command":lambda: show_result(("2"))
    },
        {
        "text":"3",
        "command":lambda: show_result("3")
    },
        {
        "text":"*",
        "command":lambda: show_result("*")
    },
        {
        "text":".",
        "command":lambda: show_result(".")
    },
        {
        "text":"0",
        "command":lambda: show_result(("0"))
    },
        {
        "text":"C",
        "command":lambda: show_result(("C"))
    },
        {
        "text":"=",
        "command":lambda: show_result(("="))
    }
]


list_keys=[]
for calc_key in calc_keys:
    btn_nums=tk.Button(
        master=window,
        text=calc_key['text'],
        command=calc_key["command"],
        width=7,
        height=3
    )
    list_keys.append(btn_nums)


for i, calc_obj in enumerate(list_keys):
    calc_obj.grid(row=(i//4)+1 , column=i%4)


window.mainloop()