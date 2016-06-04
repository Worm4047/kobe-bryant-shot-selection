import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unique_params import *

"""







period
playoffs
season 
seconds_remaining
shot_distance
shot_made_flag (this is what you are predicting)
shot_type
shot_zone_area
shot_zone_basic
shot_zone_range
team_id
team_name
game_date
matchup
opponent
shot_id
"""
data.action_type=data.loc[:,'action_type'].apply(lambda x :  np.where(x == unique_action_type)[0][0])
data.combined_shot_type=data.loc[:,'combined_shot_type'].apply(lambda x :  np.where(x == unique_combined_shot_type)[0][0])
data.game_event_id=data.loc[:,'game_event_id'].apply(lambda x :  np.where(x == unique_game_event_id)[0][0])
data.game_id=data.loc[:,'game_id'].apply(lambda x :  np.where(x == unique_game_id)[0][0])
data.lat=data.loc[:,'lat'].apply(lambda x :  np.where(x == unique_lat)[0][0])
data.loc_x=data.loc[:,'loc_x'].apply(lambda x :  np.where(x == unique_loc_x)[0][0])
data.loc_y=data.loc[:,'loc_y'].apply(lambda x :  np.where(x == unique_loc_y)[0][0])
data.lon=data.loc[:,'lon'].apply(lambda x :  np.where(x == unique_lon)[0][0])
data.minutes_remaining=data.loc[:,'minutes_remaining'].apply(lambda x :  np.where(x == unique_minutes_remaining)[0][0])
data.period=data.loc[:,'period'].apply(lambda x :  np.where(x == unique_period)[0][0])
data.playoffs=data.loc[:,'playoffs'].apply(lambda x :  np.where(x == unique_playoffs)[0][0])
data.season=data.loc[:,'season'].apply(lambda x :  np.where(x == unique_season)[0][0])
data.seconds_remaining=data.loc[:,'seconds_remaining'].apply(lambda x :  np.where(x == unique_seconds_remaining)[0][0])
data.shot_distance=data.loc[:,'shot_distance'].apply(lambda x :  np.where(x == unique_shot_distance)[0][0])
data.shot_type=data.loc[:,'shot_type'].apply(lambda x :  np.where(x == unique_shot_type)[0][0])
data.shot_zone_area=data.loc[:,'shot_zone_area'].apply(lambda x :  np.where(x == unique_shot_zone_area)[0][0])
data.shot_zone_basic=data.loc[:,'shot_zone_basic'].apply(lambda x :  np.where(x == unique_shot_zone_basic)[0][0])
data.shot_zone_range=data.loc[:,'shot_zone_range'].apply(lambda x :  np.where(x == unique_shot_zone_range)[0][0])
data.team_id=data.loc[:,'team_id'].apply(lambda x :  np.where(x == unique_team_id)[0][0])
data.team_name=data.loc[:,'team_name'].apply(lambda x :  np.where(x == unique_team_name)[0][0])
data.game_date=data.loc[:,'game_date'].apply(lambda x :  np.where(x == unique_game_date)[0][0])
data.matchup=data.loc[:,'matchup'].apply(lambda x :  np.where(x == unique_matchup)[0][0])
data.opponent=data.loc[:,'opponent'].apply(lambda x :  np.where(x == unique_opponent)[0][0])
data.shot_id=data.loc[:,'shot_id'].apply(lambda x :  np.where(x == unique_shot_id)[0][0])

data.to_csv('cleaned_test.csv')