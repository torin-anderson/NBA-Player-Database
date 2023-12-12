import os
import pandas as pd

ps = []
rg = []

def read_data():
    '''
    This function reads each of the csv files and adds them to a list depending on whether it's a csv for post season or regular season stats.
    '''

    for file in os.listdir(os.getcwd()): #iterates through each of the csv files
        if file.endswith('.csv'): 
            df = pd.read_csv(file)
            df = df.set_index('Player')
            if 'ps' in file: #appends post season list if the title of the csv tells it's for postseason stats
                ps.append(df)   
            else: #appends regular season list if the csv is not for postseason
                rg.append(df)

def find_player(player, stat, PS=0, RG=0):
    '''
    This function searches for the player in each of the csv files and then, if the player is found, returns the 
    selected stat into two lists with one for the regular season findings and one for the post season findings

    Has four parameters: player, stat, PS, RG.
        player is searched for through each of the csv files and if found allows data to be taken from that csv file.
        stat is what data is taken from the player if the player is found in the csv file.
        PS and RG are set at 0 and determine how many times the csv is searched through.
    '''

    result_ps = []
    result_rg = []

    if PS:
        for frame in ps:
            if player in frame.index: #if player is found in post season csv, then the stat will be appended to result_ps
                result_ps.append(frame.loc[player,stat])
            elif len(result_ps) >= 1 and player not in frame.index: #if player is in the league, but missed post season, then a 0 acts as place holder
                 result_ps.append(0)
    if RG: 
        for frame in rg:
            if player in frame.index: #if player is found in regular season csv, then the stat will be appended to result_rg
                result_rg.append(frame.loc[player,stat])
            elif len(result_rg) >= 1 and player not in frame.index: #if player is in the league, but missed regular season, then a 0 acts as place holder
                 result_rg.append(0)
    return result_ps, result_rg