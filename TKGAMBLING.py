# GAMBLING
import random
import customtkinter as tk

ves = {'🍰':100000,'🍒':50000,'🍀':10000,'🍉':5000,'🍇':1000,'🍊':500,'🍋':100,'🥜':0}
money = 10000

app = tk.CTk()
app.geometry("350x350")
app.resizable(False,False)
app.title("NICKEL")
app.wm_iconbitmap('favicon.ico')

money_var = tk.IntVar(value=money)

def slots():
        luck = random.randrange(0,10)
        if luck > 7:
            luck = 7
        for i in range(7):
            match luck:
                case i:
                    symbol = list(ves.keys())[i]
        return symbol

def rewards(visual):
        for key in ves:
            if visual.count(key) == 3:
                win = ves[key]
                break
            elif visual.count(key) == 4:
                win = ves[key] * 3
                break
            elif visual.count(key) == 5:
                win = ves[key] * 7
                break
            else:
                win = 0
        return win 

def spin():
    mult = value_inside.get()
    mult = int(mult.replace('X',''))
    global money
    money -= 100 * mult
    money_var.set(money)

    visual = f'| {slots()} | {slots()} | {slots()} | {slots()} | {slots()} |'
    win = rewards(visual)
    tk.CTkLabel(app,text=visual,height=30,font=("Arial", 25)
            ).place(relx=0.38,rely=(0.3),anchor='center')
    if win != 0:
        money += win * mult + (100 * mult)
        money_var.set(money)
        tk.CTkLabel(app,text=f'WON: ${win * mult} ' + ' '*20,text_color='green'
            ).place(relx=0.05,rely=(0.17),anchor='w')
    else:
        tk.CTkLabel(app,text=' '*40,
            ).place(relx=0.05,rely=(0.17),anchor='w')
    
def labels():
    tk.CTkLabel(app,text='BALANCE:       $',height=30,
                ).place(relx=0.05,rely=0.075,anchor='w')
    mmon = tk.CTkLabel(app,textvariable=money_var,height=30
                ).place(relx=0.3,rely=0.075,anchor='w')
    tk.CTkLabel(app,text=f'SPIN = $100'
                ).place(relx=0.85,rely=(0.175),anchor='center')
    tk.CTkLabel(app,text='''FUN FACTS:
-99% of gamblers quit before the big win'''
                ).place(relx=0.65,rely=(0.62),anchor='center')
    tk.CTkLabel(app,text='''-You can only lose 100% ,
                    but you can win more than 200%'''
                ).place(relx=0.535,rely=(0.75),anchor='center')
    tk.CTkLabel(app,text='''-“The better the gambler, 
                        the better the man.” - Jesus Christ'''
                ).place(relx=0.535,rely=(0.90),anchor='center')
    tk.CTkLabel(app,text=f'4x * 3     5x * 7',text_color='yellow'
                ).place(relx=0.38,rely=(0.52),anchor='w')

labels() 

for i,key in enumerate(ves):
    tk.CTkLabel(app,text=f'3x{key} : ${ves[key]}',text_color='yellow').place(relx=0.05,rely=(0.52+(i*0.06)),anchor='w')

value_inside = tk.StringVar(app)
value_inside.set("X1")

tk.CTkButton(app,text='SPIN',command=lambda:spin(),
             width=75,fg_color='red',hover_color='yellow',text_color='black'
             ).place(relx=0.85,rely=(0.075),anchor='center')

tk.CTkOptionMenu(app, variable=value_inside, values=["X1", "X10", "X100", "X1000", "X10000"],
                 fg_color='gray',text_color='black',button_color='gray',width=90,
                 ).place(relx=0.83,rely=(0.50),anchor='center')

app.mainloop()