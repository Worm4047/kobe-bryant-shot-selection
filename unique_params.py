import numpy as np 
import pandas as pd 


data = pd.read_csv('predicting_set.csv')
data=data.drop('Unnamed: 0',1)

unique_action_type = data.action_type.unique()
unique_combined_shot_type = data.combined_shot_type.unique()
unique_game_event_id = data.game_event_id.unique()
unique_game_id = data.game_id.unique()
unique_lat = data.lat.unique()
unique_loc_x = data.loc_x.unique()
unique_loc_y = data.loc_y.unique()
unique_lon = data.lon.unique()
unique_minutes_remaining = data.minutes_remaining.unique()
unique_period = data.period.unique()
unique_playoffs = data.playoffs.unique()
unique_season = data.season.unique()
unique_seconds_remaining = data.seconds_remaining.unique()
unique_shot_distance = data.shot_distance.unique()
unique_shot_type = data.shot_type.unique()
unique_shot_zone_area = data.shot_zone_area.unique()
unique_shot_zone_basic = data.shot_zone_basic.unique()
unique_shot_zone_range = data.shot_zone_range.unique()
unique_team_id = data.team_id.unique()
unique_team_name = data.team_name.unique()
unique_game_date = data.game_date.unique()
unique_matchup = data.matchup.unique()
unique_opponent = data.opponent.unique()
unique_shot_id = data.shot_id.unique()

