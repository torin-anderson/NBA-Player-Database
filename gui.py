from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
import CSV_reader as stats

years = ['2013-2014','2014-2015','2015-2016',
         '2016-2017','2017-2018','2018-2019',
         '2019-2020','2020-2021','2021-2022','2022-2023'] #establishes all possible years that can be viewed
stats.read_data() #reads all of the csv files


#Establishes the first window where it asks the user for a player and takes in the player's name
master = Tk()
master.title("User Input for Player")

master.rowconfigure(0,minsize=300, weight=1)
master.columnconfigure(0,minsize=300,weight=1)

frame = Frame(master, relief=RAISED)
frame.grid(row=0, column=0, sticky="ns")

#the text box on the top of the first window that asks which nba player the user wants to view
text_box = Label(frame,
                width=60,
                height=3,
                text="Which NBA player would you like to view stats for?",
                bg="RED")
text_box.grid(row=0,columnspan=2)

#the box for where the user inputs the player they want
input = tk.Entry(master)
input.grid(row=0, columnspan=2)

#button to bring the user to the second window
btn_continue = Button(frame,
                width=7,
                height=1,
                text="Continue",
                command=lambda : stat_window(input.get().title()))
btn_continue.place(x=180, y=165)


def stat_window(name):
    '''
    This function creates the second window that has 10 
    buttons to select different stats to view on the graph in the next window.

    Has one parameter: name. 
        Name  is taken from the previous window through the entry box and the button brings it to this function.

    Each button in this window brings the user to a graph that compares the player's career
    and the stat for the button they clicked. 
    '''

    window2 = Toplevel(master)
    window2.title("User Input for Stats")

    window2.rowconfigure(0,minsize=300, weight=1)
    window2.columnconfigure(0,minsize=300,weight=1)

    frame2 = Frame(window2, relief=RAISED)
    frame2.grid(row=0, column=0, sticky="ns")

    #the text box at the top of the second window that asks which stat would like to be viewed
    text_box = Label(frame2,
                    width=60,
                    height=3,
                    text="Which stat would you like to view?",
                    bg="LIGHTBLUE")
    text_box.grid(row=0,columnspan=2)

    #Retreiving the numbers for each type of stat for the inputted player
    ppg= stats.find_player(name,'PTS',1,1)
    mpg = stats.find_player(name,'MP',1,1)
    gp = stats.find_player(name,'G',1,1)
    eFG = stats.find_player(name,'eFG%',1,1)
    ft = stats.find_player(name,'FT%',1,1)
    rb = stats.find_player(name,'TRB',1,1)
    ast= stats.find_player(name,'AST',1,1)
    stl = stats.find_player(name,'STL',1,1)
    tov= stats.find_player(name,'TOV',1,1)
    blk = stats.find_player(name,'BLK',1,1)

    #Making each of the buttons for the second window
    #Points per game button
    btn_ppg = Button(frame2,
                    width=30,
                    height=3,
                    text="Points Per Game",
                    command=lambda : line_graph("PPG", 
                                                ppg[1], 
                                                ppg[0], 
                                                name))
    btn_ppg.grid(row=1, column=0)

    #Minutes per game button
    btn_mpg = Button(frame2,
                    width=30,
                    height=3,
                    text="Minutes Per Game",
                    command=lambda : line_graph("MPG", 
                                                mpg[1], 
                                                mpg[0], 
                                                name))
    btn_mpg.grid(row=1, column=1)

    #Games played button
    btn_games = Button(frame2,
                    width=30,
                    height=3,
                    text="Games Per Season",
                    command=lambda : line_graph("GP", 
                                                gp[1], 
                                                gp[0], 
                                                name))
    btn_games.grid(row=2, column=0)

    #EFG per season
    btn_efg = Button(frame2,
                    width=30,
                    height=3,
                    text="eFG% Per Season",
                    command=lambda : line_graph("eFG%", 
                                                eFG[1], 
                                                eFG[0], 
                                                name))
    btn_efg.grid(row=2, column=1)

    #Free throws per season
    btn_ft = Button(frame2,
                    width=30,
                    height=3,
                    text="FT% Per Season",
                    command=lambda : line_graph("FT%", 
                                                ft[1], 
                                                ft[0], 
                                                name))
    btn_ft.grid(row=3, column=0)

    #Rebounds per game
    btn_rebounds = Button(frame2,
                    width=30,
                    height=3,
                    text="Rebounds Per Game",
                    command=lambda : line_graph("TRB", 
                                                rb[1], 
                                                rb[0], 
                                                name))
    btn_rebounds.grid(row=3, column=1)

    #Assists per game
    btn_assists = Button(frame2,
                    width=30,
                    height=3,
                    text="Assists Per Game",
                    command=lambda : line_graph("AST", 
                                                ast[1], 
                                                ast[0], 
                                                name))
    btn_assists.grid(row=4, column=0)

    #Steals per game
    btn_steals = Button(frame2,
                    width=30,
                    height=3,
                    text="Steals Per Game",
                    command=lambda : line_graph("STL", 
                                                stl[1], 
                                                stl[0], 
                                                name))
    btn_steals.grid(row=4, column=1)

    #Turnovers per game
    btn_turnovers = Button(frame2,
                    width=30,
                    height=3,
                    text="Turnovers Per Game",
                    command=lambda : line_graph("TOV",  
                                                tov[1],
                                                tov[0], 
                                                name))
    btn_turnovers.grid(row=5, column=0)

    #Blocks per game
    btn_blocks = Button(frame2,
                    width=30,
                    height=3,
                    text="Blocks Per Game",
                    command=lambda : line_graph("BLK", 
                                                blk[1], 
                                                blk[0], 
                                                name))
    btn_blocks.grid(row=5, column=1)

#Function that creates the graph
def line_graph(stat_type, rg_stat, ps_stat, name):
    '''
    This function creates the third window that displays a line graph that compares
    each season that the player played and the stat the user chose to view, the seasons
    acting as the x-axis and the stat as the y-axis.

    Has four parameters: stat_type, rg_stat, ps_stat, and name. 
        stat_type follows which stat the user selected to view and displays the name of that stat as the label for the y-axis.
        rg_stat and ps_stat are the regular season and post_season numbers for the stat shown and are both plotted on the graph, 
            rg_stat as blue and ps_stat as orange. If a season on the graph was missed by the player then the stat is shown as 0.
        name is used as the title for the graph
    '''

    fig, ax = plt.subplots()
    ax.plot(years[10 - len(rg_stat):], #the x-axis starting when the player started or if they played before 2013-2014 then starts 2013-2014 season 
            rg_stat, 
            label="Regular Season") #plots regular season 
    ax.plot(years[10 - len(rg_stat):], #the x-axis starting when the player started or if they played before 2013-2014 then starts 2013-2014 season 
            ps_stat, 
            label="Playoffs") #plots post season stat,
    ax.legend()

    #titles
    ax.set_title(name, loc='center', fontsize="xx-large")
    ax.set_ylabel(stat_type)
    ax.set_xlabel("Seasons")

    #style changes for graph
    ax.grid(True) #creates grid
    plt.xticks(fontsize=6) #changes font size for x-axis ticks or seasons nubmers

    plt.show()

master.mainloop()