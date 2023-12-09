from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt

years = ["2013-2014", "2014-2015", "2015-2016", "2016-2017", "2017-2018", "2018-2019", "2019-2020", "2020-2021", "2021-2022", "2022-2023"]

#Establishes the first window where it asks the user for a player and takes in the player's name
master = Tk()
master.title("User Input for Player")

master.rowconfigure(0,minsize=300, weight=1)
master.columnconfigure(0,minsize=300,weight=1)

#The first window where it asks the user for a player and takes in the player's name
frame = Frame(master, relief=RAISED)
frame.grid(row=0, column=0, sticky="ns")

#the text box on the first window
text_box = Label(frame,
                width=60,
                height=3,
                text="Which NBA player would you like to view stats for?",
                bg="RED")
text_box.grid(row=0,columnspan=2)

#the box for where the user inputs the player they want
input = tk.Entry(master)
input.grid(row=0, columnspan=2)
# user_inputted_player = input.get().title() #variable where the players name is saved

#Function creates the second window which determines which stat whill be displayed on the graph
def stat_window(name):
    print('hello from start window', name)
    window2 = Toplevel(master)
    window2.title("User Input for Stats")

    window2.rowconfigure(0,minsize=300, weight=1)
    window2.columnconfigure(0,minsize=300,weight=1)

    frame2 = Frame(window2, relief=RAISED)
    frame2.grid(row=0, column=0, sticky="ns")

    #Text Box
    text_box = Label(frame2,
                    width=60,
                    height=3,
                    text="Which stat would you like to view?",
                    bg="LIGHTBLUE")
    text_box.grid(row=0,columnspan=2)

    #Making each of the buttons for the second window
    #Points per game button
    btn_ppg = Button(frame2,
                    width=30,
                    height=3,
                    text="Points Per Game",
                    command=lambda : line_graph("PPG", [6, 20, 15, 0, 5, 8, 10, 12, 6, 12], [5, 8, 10, 12, 6, 9, 7, 0, 5, 2], name))
    btn_ppg.grid(row=1, column=0)

    #Minutes per game button
    btn_mpg = Button(frame2,
                    width=30,
                    height=3,
                    text="Minutes Per Game",
                    command=lambda : line_graph("MPG", [6, 20, 15, 0, 5, 8, 10, 12, 6, 12], [5, 8, 10, 12, 6, 9, 7, 0, 5, 2], name))
    btn_mpg.grid(row=1, column=1)

    #Games played button
    btn_games = Button(frame2,
                    width=30,
                    height=3,
                    text="Games Per Season",
                    command=lambda : line_graph("GP", [6, 20, 15, 0, 5, 8, 10, 12, 6, 12], [5, 8, 10, 12, 6, 9, 7, 0, 5, 2], name))
    btn_games.grid(row=2, column=0)

    #EFG per season
    btn_efg = Button(frame2,
                    width=30,
                    height=3,
                    text="eFG% Per Season",
                    command=lambda : line_graph("eFG%", [6, 20, 15, 0, 5, 8, 10, 12, 6, 12], [5, 8, 10, 12, 6, 9, 7, 0, 5, 2], name))
    btn_efg.grid(row=2, column=1)

    #Free throws per season
    btn_games = Button(frame2,
                    width=30,
                    height=3,
                    text="FT% Per Season",
                    command=lambda : line_graph("FT%", [6, 20, 15, 0, 5, 8, 10, 12, 6, 12], [5, 8, 10, 12, 6, 9, 7, 0, 5, 2], name))
    btn_games.grid(row=3, column=0)

    #Rebounds per game
    btn_rebounds = Button(frame2,
                    width=30,
                    height=3,
                    text="Rebounds Per Game",
                    command=lambda : line_graph("TRB", [6, 20, 15, 0, 5, 8, 10, 12, 6, 12], [5, 8, 10, 12, 6, 9, 7, 0, 5, 2], name))
    btn_rebounds.grid(row=3, column=1)

    #Assists per game
    btn_assists = Button(frame2,
                    width=30,
                    height=3,
                    text="Assists Per Game",
                    command=lambda : line_graph("AST", [6, 20, 15, 0, 5, 8, 10, 12, 6, 12], [5, 8, 10, 12, 6, 9, 7, 0, 5, 2], name))
    btn_assists.grid(row=4, column=0)

    #Steals per game
    btn_steals = Button(frame2,
                    width=30,
                    height=3,
                    text="Steals Per Game",
                    command=lambda : line_graph("STL", [6, 20, 15, 0, 5, 8, 10, 12, 6, 12], [5, 8, 10, 12, 6, 9, 7, 0, 5, 2], name))
    btn_steals.grid(row=4, column=1)

    #Turnovers per game
    btn_turnovers = Button(frame2,
                    width=30,
                    height=3,
                    text="Turnovers Per Game",
                    command=lambda : line_graph("TOV", [6, 20, 15, 0, 5, 8, 10, 12, 6, 12], [5, 8, 10, 12, 6, 9, 7, 0, 5, 2], name))
    btn_turnovers.grid(row=5, column=0)

    #Blocks per game
    btn_blocks = Button(frame2,
                    width=30,
                    height=3,
                    text="Blocks Per Game",
                    command=lambda : line_graph("BLK", [6, 20, 15, 0, 5, 8, 10, 12, 6, 12], [5, 8, 10, 12, 6, 9, 7, 0, 5, 2], name))
    btn_blocks.grid(row=5, column=1)

def line_graph(stat_type, rg_stat, ps_stat, player):

    fig, ax = plt.subplots()
    ax.plot(years, rg_stat, label="Regular Season")
    ax.plot(years, ps_stat, label="Playoffs") 
    ax.legend()

    #titles
    ax.set_title(player, loc='center', fontsize="xx-large")
    ax.set_ylabel(stat_type)
    ax.set_xlabel("Seasons")

    #style changes for graph
    ax.grid(True) #creates grid
    plt.xticks(fontsize=6)

    plt.show()

#button to bring the user to the second window
btn_continue = Button(frame,
                width=7,
                height=1,
                text="Continue",
                command=lambda : stat_window(input.get().title()))
btn_continue.place(x=180, y=165); 

master.mainloop()