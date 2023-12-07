from tkinter import *

#Establishes the first window
master = Tk()
master.title("User Input for Player")

master.rowconfigure(0,minsize=300, weight=1)
master.columnconfigure(0,minsize=300,weight=1)

#Function creates the second window which determines which stat whill be displayed on the graph
def stat_window():
    window2 = Toplevel(master)
    window2.title("User Input for Stats")

    window2.rowconfigure(0,minsize=300, weight=1)
    window2.columnconfigure(0,minsize=300,weight=1)

    frame = Frame(window2, relief=RAISED)
    frame.grid(row=0, column=0, sticky="ns")

    #Text Box
    text_box = Label(frame,
                    width=60,
                    height=3,
                    text="Which stat would you like to view?",
                    bg="LIGHTBLUE")
    text_box.grid(row=0,columnspan=2)

    #Making each of the buttons
    #Points per game button
    btn_ppg = Button(frame,
                    width=30,
                    height=3,
                    text="Points Per Game")
    btn_ppg.grid(row=1, column=0)

    #Minutes per game button
    btn_mpg = Button(frame,
                    width=30,
                    height=3,
                    text="Minutes Per Game")
    btn_mpg.grid(row=1, column=1)

    #Games played button
    btn_games = Button(frame,
                    width=30,
                    height=3,
                    text="Games Per Season")
    btn_games.grid(row=2, column=0)

    #EFG per season
    btn_efg = Button(frame,
                    width=30,
                    height=3,
                    text="eFG% Per Season")
    btn_efg.grid(row=2, column=1)

    #Free throws per season
    btn_games = Button(frame,
                    width=30,
                    height=3,
                    text="FT% Per Season")
    btn_games.grid(row=3, column=0)

    #Rebounds per game
    btn_rebounds = Button(frame,
                    width=30,
                    height=3,
                    text="Rebounds Per Game")
    btn_rebounds.grid(row=3, column=1)

    #Assists per game
    btn_assists = Button(frame,
                    width=30,
                    height=3,
                    text="Assists Per Game")
    btn_assists.grid(row=4, column=0)

    #Steals per game
    btn_steals = Button(frame,
                    width=30,
                    height=3,
                    text="Steals Per Game")
    btn_steals.grid(row=4, column=1)

    #Turnovers per game
    btn_turnovers = Button(frame,
                    width=30,
                    height=3,
                    text="Turnovers Per Game")
    btn_turnovers.grid(row=5, column=0)

    #Blocks per game
    btn_blocks = Button(frame,
                    width=30,
                    height=3,
                    text="Blocks Per Game")
    btn_blocks.grid(row=5, column=1)

#Code for the first window where it takes in a player's name and brings up the second window
frame = Frame(master, relief=RAISED)
frame.grid(row=0, column=0, sticky="ns")
btn_ppg = Button(command=stat_window)
btn_ppg.grid(row=1, column=0)

master.mainloop()