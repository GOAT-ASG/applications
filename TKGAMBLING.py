# GAMBLING
import random
import customtkinter as tk

def start():
    global app
    # Define slot machine symbols and their corresponding values
    ves = {'🍰':100000, '🍒':50000, '🍀':10000, '🍉':5000, '🍇':1000, '🍊':500, '🍈':100, '🥜':0}
    money = 10000  # Initial amount of money
    lablity = [None] * 8  # List to hold labels for payout information

    # Initialize the main application window
    app = tk.CTk()
    app.geometry(f"350x350+{(app.winfo_screenwidth() - 350)//2}+{(app.winfo_screenheight() - 350)//2}")
    app.resizable(False, False)
    app.title("NICKEL")
    # Unused: app.wm_iconbitmap('Gambling Machine_favicon.ico')

    # Create frames for layout
    chart = tk.CTkFrame(app, width=335, height=180, fg_color='brown')
    chart.place(relx=0.5, rely=0.72, anchor='center')
    sidepanel = tk.CTkFrame(app, width=85, height=150, fg_color='brown')
    sidepanel.place(relx=0.857, rely=0.2275, anchor='center')
    wallet = tk.CTkFrame(app, width=245, height=40, fg_color='chocolate')
    wallet.place(relx=0.3675, rely=0.07, anchor='center')
    visor = tk.CTkFrame(app, width=245, height=105, fg_color='navy')
    visor.place(relx=0.3675, rely=0.295, anchor='center')

    money_var = tk.IntVar(value=money)  # Variable to track the player's money
    trma = tk.BooleanVar(value=False)  # Variable to track if TRMA mode is enabled

    def slots():
        """
        Simulate spinning the slot machine by randomly selecting a symbol.
        """
        luck = random.randrange(0,10)
        if luck > 7:
            luck = 7
        for i in range(7):
            match luck:
                case i:
                    symbol = list(ves.keys())[i]
        return symbol

    def rewards(visual):
        """
        Calculate winnings based on the visual result of the spin.

        Args:
            visual (str): The result of the spin.

        Returns:
            int: The amount won.
        """
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

    def tm():
        """
        Handle the display logic for the TRMA (Total Random Mode Activated) feature.
        """
        if random.randrange(1, 11) == 1:
            button.place(relx=0.5, rely=(0.34), anchor='center')
            button_all.place(relx=0.5, rely=(0.125), anchor='center')

    def setup(allmode, money):
        """
        Set up the betting parameters and update the money based on the entered bet amount or default values.

        Args:
            allmode (str): Mode of operation ("no" for normal, "yes" for ALL IN).
            money (int): Current amount of money.

        Returns:
            tuple: (multiplier, updated money)
        """
        if allmode == 'no':
            mult = entry.get()
            if mult == 'TRMA':
                trma.set(True)
            if not mult.isnumeric():
                return

            if int(mult) < 100:
                return

            mult = int(mult)
            money -= mult
            money_var.set(int(money))
        else:
            mult = 3

        if trma.get():
            button.place(relx=0.5,rely=(0.13),anchor='center')
            button_all.place(relx=0.5,rely=(0.34),anchor='center')
            tm()

        if allmode == 'no':
            for i, key in enumerate(ves):
                lablity[i].configure(text=f'3x{key} : ${int((mult/100) * ves[key])}')

        return mult, money

    def spin(allmode='no'):
        """
        Handle the spinning logic, calculate the result, update the display, and adjust the money based on winnings or losses.

        Args:
            allmode (str): Mode of operation ("no" for normal, "yes" for ALL IN).
        """
        nonlocal money
        try:
            mult, money = setup(allmode, money)
        except:
            return

        visual = f'| {slots()} | {slots()} | {slots()} | {slots()} | {slots()} |'
        win = rewards(visual)
        screen.configure(app, text=visual, height=30, font=("Arial", 25))
        
        if win != 0:
            if allmode == 'no':
                money += win * mult / 100
                money_var.set(int(money))
                winnings.configure(text=f'WON: ${int(win * mult / 100)}', text_color='green')
            elif allmode == 'yes':
                money *= mult
                money_var.set(int(money))
                winnings.configure(text=f'WON: ${int(money)}', text_color='green')
        elif win == 0 and allmode == 'yes':
            money -= money * 2
            money_var.set(int(money))
        else:
            winnings.configure(text='')
        if money < 0:
            button.configure(state='disabled')
            button_all.configure(state='disabled')
            entry.configure(state='disabled')
            screen.configure(text='BANKRUPT', text_color='red', font=("Arial", 40, 'bold'))
            button_restart.configure(state='normal')
        
    def labels():
        """
        Create and place labels on the GUI to display information such as balance, game instructions, and slot machine results.

        Returns:
            tuple: (winnings label, screen label)
        """
        tk.CTkLabel(wallet, text='BALANCE:  $', height=30, font=("Arial", 14, 'bold'), text_color='black').place(relx=0.03, rely=0.5, anchor='w')
        tk.CTkLabel(wallet, textvariable=money_var, height=30, font=("Arial", 14, 'bold'), text_color='black').place(relx=0.375, rely=0.5, anchor='w')
        tk.CTkLabel(chart, text='FUN FACTS:').place(relx=0.65, rely=(0.25), anchor='center')
        tk.CTkLabel(chart, text='''-99% of gamblers quit before the big win
                    
-You can only lose 100% , 
but you can win more than 1000%
                    
-“The better the gambler, 
the better the man.” - Jesus Christ''', justify='left'
                    ).place(relx=0.64, rely=(0.35), anchor='n')
        tk.CTkLabel(chart, text=f'4x * 3     5x * 7' + ' '*18 + 'MIN = $100', text_color='yellow'
                    ).place(relx=0.38, rely=(0.1), anchor='w')
        tk.CTkLabel(sidepanel, text='BET', text_color='white', font=("Arial", 14, 'bold')
                    ).place(relx=0.50, rely=(0.7), anchor='center')

        screen = tk.CTkLabel(visor, text=f'| 🍀 | 🍀 | 🍀 | 🍀 | 🍀 |', text_color='white', height=30, font=("Arial", 25))
        screen.place(relx=0.495, rely=(0.48), anchor='center')

        winnings = tk.CTkLabel(visor, text=' ', font=("Arial", 14, 'bold'))
        winnings.place(relx=0.05, rely=(0.17), anchor='w')
        for i, key in enumerate(ves):
            lablity[i] = tk.CTkLabel(chart, text=f'3x{key} : ${ves[key]}', text_color='yellow')
            lablity[i].place(relx=0.02, rely=(0.1+(i*0.115)), anchor='w')
        return winnings, screen

    def interactive():
        """
        Create and place interactive buttons and entry fields for the user to interact with the slot machine.
        """
        global button, button_all, button_restart, entry

        button = tk.CTkButton(sidepanel, text='SPIN', command=lambda: spin(),
                width=75, fg_color='purple', hover_color='yellow', text_color='black',
                border_width=3, border_color='black', font=("Arial", 14, 'bold'))
        button.place(relx=0.5, rely=(0.13), anchor='center')

        button_all = tk.CTkButton(sidepanel, text='ALL IN', command=lambda: spin('yes'),
                width=75, fg_color='purple', hover_color='yellow', text_color='black',
                border_width=3, border_color='black', font=("Arial", 14, 'bold'))
        button_all.place(relx=0.5, rely=(0.34), anchor='center')

        button_restart = tk.CTkButton(sidepanel, text='RESTART', command=refresh,
                width=75, fg_color='purple', hover_color='yellow', text_color='black',
                border_width=3, border_color='black', font=("Arial", 14, 'bold'), state='disabled')
        button_restart.place(relx=0.5, rely=(0.55), anchor='center')

        entry = tk.CTkEntry(sidepanel, placeholder_text='$100', placeholder_text_color='black',
                fg_color='gray', text_color='black', width=75)
        entry.place(relx=0.5, rely=(0.87), anchor='center')

    winnings, screen = labels() 
    interactive()

    app.mainloop()

def refresh():
    """
    Reset the application by destroying the current instance and starting a new one.
    """
    app.destroy()
    start()

start()
