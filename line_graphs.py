import matplotlib.pyplot as plt

years = ["2013-2014", "2014-2015", "2015-2016", "2016-2017", "2017-2018", "2018-2019", "2019-2020", "2020-2021", "2021-2022", "2022-2023"]

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

tatum = "Jayson Tatum"
type = "Rebound per Game"
post = [5, 8, 10, 12, 6, 9, 7, 0, 5, 2]
regular = [6, 20, 15, 0, 5, 8, 10, 12, 6, 12]
line_graph(type, regular, post, tatum)