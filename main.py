# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 22:39:30 2019

@author: Kenny
"""
import requests
import pandas as pd

maps = list()
mystats = list()

def fi_search(p_name):
    header = {'Authorization': 'Bearer 88edf053-5c28-45e6-a661-651f9b237993'} #my secret key, replace with yours
    p_info_url = 'https://open.faceit.com/data/v4/players?nickname=' + p_name + '&game=csgo'
    r1 = requests.get(p_info_url, headers = header)
    data = r1.json()
    
    p_id = data['player_id']

    p_stat_url = 'https://open.faceit.com/data/v4/players/' + p_id + '/stats/csgo'
    r2 = requests.get(p_stat_url, headers = header)
    stat_data = r2.json()
    
    # Stats from lifetime array
    lifetime_hs = stat_data['lifetime']['Average Headshots %']
    lifetime_avg_kd = stat_data['lifetime']['Average K/D Ratio']
    current_win_streak = stat_data['lifetime']['Current Win Streak']
    lifetime_tot_kd = stat_data['lifetime']['K/D Ratio']
    lifetime_win_streak = stat_data['lifetime']['Longest Win Streak']
    lifetime_matches = stat_data['lifetime']['Matches']
    lifetime_win_rate = stat_data['lifetime']['Win Rate %']
    lifetime_wins = stat_data['lifetime']['Wins']
    print(lifetime_hs)
    print(lifetime_avg_kd)
    print(current_win_streak)
    print(lifetime_tot_kd)
    print(lifetime_win_streak)
    print(lifetime_matches)
    print(lifetime_win_rate)
    print(lifetime_wins)
    
    for i in stat_data['segments']:
        maps.append(i['label'])
    print(maps)
    
    for i in stat_data['segments']:
        mystats.append(i['stats'])
    #print(mystats)
    
    for i in range(len(maps)):
        print("\nAssist Stats on " + maps[i-1] + ":")
        print(p_name + ' has an average of ' + mystats[i-1]['Average Assists'] + ' assists.')
        print(p_name + ' has a total of ' + mystats[i-1]['Assists'] + ' assists.')
        
        print("\nDeath Stats on " + maps[i-1] + ":")
        print(p_name + ' has an average of ' + mystats[i-1]['Average Deaths'] + ' deaths.')
        print(p_name + ' has a total of ' + mystats[i-1]['Deaths'] + ' deaths.')
        
        print("\nHeadshot Stats on " + maps[i-1] + ":")
        print(p_name + ' has an average of ' + mystats[i-1]['Headshots per Match'] + ' headshots per match.')
        print(p_name + ' has an average headshot percentage of ' + mystats[i-1]['Average Headshots %'] + '%.')
        print(p_name + ' has a total of ' + mystats[i-1]['Headshots'] + ' headshots.')
        print(p_name + ' has a total hs percent of ' + mystats[i-1]['Total Headshots %'] + '%.')
        
        print("\nKD Stats on " + maps[i-1] + ":")
        print(p_name + ' has an average k/d ratio of ' + mystats[i-1]['Average K/D Ratio'] + '.')
        print(p_name + ' has a total k/d ratio of ' + mystats[i-1]['K/D Ratio'] + '.')
        
        print("\nKR Stats on " + maps[i-1] + ":")
        print(p_name + ' has an average k/r ratio of ' + mystats[i-1]['Average K/R Ratio'] + '.')
        print(p_name + ' has a total k/r ratio of ' + mystats[i-1]['K/R Ratio'] + '.')
        
        print("\nKill Stats on " + maps[i-1] + ":")
        print(p_name + ' has an average of ' + mystats[i-1]['Average Kills'] + ' kills.')
        print(p_name + ' has ' + mystats[i-1]['Kills'] + ' in total kills.')
        print(p_name + ' has an average of ' + mystats[i-1]['Average Penta Kills'] + ' aces.')
        print(p_name + ' has a total of ' + mystats[i-1]['Penta Kills'] + ' aces.')
        print(p_name + ' has an average of ' + mystats[i-1]['Average Quadro Kills'] + ' 4-kill rounds.')
        print(p_name + ' has a total of ' + mystats[i-1]['Quadro Kills'] + ' 4-kill rounds.')
        print(p_name + ' has an average of ' + mystats[i-1]['Average Triple Kills'] + ' 3-kill rounds.')
        print(p_name + ' has a total of ' + mystats[i-1]['Triple Kills'] + ' 3-kill rounds.')
        
        print("\nMVP Stats on " + maps[i-1] + ":")
        print(p_name + ' has an average of ' + mystats[i-1]['Average MVPs'] + ' MVPs.')
        print(p_name + ' has ' + mystats[i-1]['MVPs'] + ' in total MVPs.')
        
        print("\nMatch Stats on " + maps[i-1] + ":")
        print(p_name + ' has played ' + mystats[i-1]['Matches'] + ' matches.')
        print(p_name + ' has a total of ' + mystats[i-1]['Rounds'] + ' rounds.')
        print(p_name + ' has a win rate of ' + mystats[i-1]['Win Rate %'] + '%.')
        print(p_name + ' has a total of ' + mystats[i-1]['Wins'] + ' wins.')
    
fi_search('-bish0p')









