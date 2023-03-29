import tkinter as tk

var = ""

def btn_pressend(item):
    global var
    var = var + str(item)
    input_text.set(var)

def clear():
    global var
    var = ""
    input_text.set(var)

def equal():
    global var
    result = str(eval(var))
    input_text.set(result)
    var = ""

def back_space():
    global var
    var = var[:-1]
    input_text.set(var)

win = tk.Tk()
win.geometry("312x427")
win.resizable(0, 0)
win.title("GUI Calculator")

input_text = tk.StringVar()

#input_field
Frm_input = tk.Frame(master=win, height=50, width=400, highlightbackground="black", highlightcolor="black", highlightthickness=3)
Frm_input.pack(side=tk.TOP)

Ent_input = tk.Entry(master=Frm_input, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
Ent_input.pack(ipady=10)

#Buttons
Frm_Buttons = tk.Frame(master=win, width=312, height=272.5, bg="grey")
Frm_Buttons.pack()

#First row
btn_clear = tk.Button(master=Frm_Buttons, text="C", font=("Gadugi", 10), fg = "black", width = 32, height = 4, bd = 0, bg = "#659EC7", cursor = "hand2", command= lambda:clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
btn_backspace = tk.Button(master=Frm_Buttons, text="<-", font=("Gadugi", 10), fg = "black", width = 10, height = 4, bd = 0, bg = "#659EC7", cursor = "hand2", command= lambda:back_space()).grid(row = 0, column = 3, padx = 1, pady = 1)

#Second row
btn_one = tk.Button(master=Frm_Buttons, text="1", font=("Gadugi", 10), fg = "black", width = 10, height = 4, bd = 0, bg = "#E1D9D1", cursor = "hand2", command= lambda:btn_pressend(1)).grid(row = 1, column = 0, padx = 1, pady = 1)
btn_two = tk.Button(master=Frm_Buttons, text="2", font=("Gadugi", 10), fg = "black", width = 10, height = 4, bd = 0, bg = "#E1D9D1", cursor = "hand2", command= lambda:btn_pressend(2)).grid(row = 1, column = 1, padx = 1, pady = 1)
btn_three = tk.Button(master=Frm_Buttons, text="3", font=("Gadugi", 10), fg = "black", width = 10, height = 4, bd = 0, bg = "#E1D9D1", cursor = "hand2", command= lambda:btn_pressend(3)).grid(row = 1, column = 2, padx = 1, pady = 1)
btn_divide = tk.Button(master=Frm_Buttons, text="/", font=("Gadugi", 10), fg = "black", width = 10, height = 4, bd = 0, bg = "#659EC7", cursor = "hand2", command= lambda:btn_pressend("/")).grid(row = 1, column = 3, padx = 1, pady = 1)

#Third row 
btn_four = tk.Button(master=Frm_Buttons, text="4", font=("Gadugi", 10), fg = "black", width = 10, height = 4, bd = 0, bg = "#E1D9D1", cursor = "hand2", command= lambda:btn_pressend(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
btn_five = tk.Button(master=Frm_Buttons, text="5", font=("Gadugi", 10), fg = "black", width = 10, height = 4, bd = 0, bg = "#E1D9D1", cursor = "hand2", command= lambda:btn_pressend(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
btn_six = tk.Button(master=Frm_Buttons, text="6", font=("Gadugi", 10), fg = "black", width = 10, height = 4, bd = 0, bg = "#E1D9D1", cursor = "hand2", command= lambda:btn_pressend(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
btn_multipy = tk.Button(master=Frm_Buttons, text="*", font=("Gadugi", 10), fg = "black", width = 10, height = 4, bd = 0, bg = "#659EC7", cursor = "hand2", command= lambda:btn_pressend("*")).grid(row = 2, column = 3, padx = 1, pady = 1)

#Forth row
btn_seven = tk.Button(master=Frm_Buttons, text="7", font=("Gadugi", 10), fg = "black", width = 10, height = 4, bd = 0, bg = "#E1D9D1", cursor = "hand2", command= lambda:btn_pressend(7)).grid(row = 3, column = 0, padx = 1, pady = 1)
btn_eight = tk.Button(master=Frm_Buttons, text="8", font=("Gadugi", 10), fg = "black", width = 10, height = 4, bd = 0, bg = "#E1D9D1", cursor = "hand2", command= lambda:btn_pressend(8)).grid(row = 3, column = 1, padx = 1, pady = 1)
btn_nine = tk.Button(master=Frm_Buttons, text="9", font=("Gadugi", 10), fg = "black", width = 10, height = 4, bd = 0, bg = "#E1D9D1", cursor = "hand2", command= lambda:btn_pressend(9)).grid(row = 3, column = 2, padx = 1, pady = 1)
btn_minus = tk.Button(master=Frm_Buttons, text="-", font=("Gadugi", 10), fg = "black", width = 10, height = 4, bd = 0, bg = "#659EC7", cursor = "hand2", command= lambda:btn_pressend("-")).grid(row = 3, column = 3, padx = 1, pady = 1)

#Fifth row
btn_zero = tk.Button(master=Frm_Buttons, text="0", font=("Gadugi", 10), fg = "black", width = 10, height = 4, bd = 0, bg = "#E1D9D1", cursor = "hand2", command= lambda:btn_pressend(0)).grid(row = 4, column = 0, padx = 1, pady = 1)
btn_dot = tk.Button(master=Frm_Buttons, text=".", font=("Gadugi", 10), fg = "black", width = 10, height = 4, bd = 0, bg = "#E1D9D1", cursor = "hand2", command= lambda:btn_pressend(".")).grid(row = 4, column = 1, padx = 1, pady = 1)
btn_equals = tk.Button(master=Frm_Buttons, text="=", font=("Gadugi", 10), fg = "black", width = 10, height = 4, bd = 0, bg = "#F88017", cursor = "hand2", command= lambda:equal()).grid(row = 4, column = 2, padx = 1, pady = 1)
btn_plus =tk.Button(master=Frm_Buttons, text="+", font=("Gadugi", 10), fg = "black", width = 10, height = 4, bd = 0, bg = "#659EC7", cursor = "hand2", command= lambda:btn_pressend("+")).grid(row = 4, column = 3, padx = 1, pady = 1)

win.mainloop()
