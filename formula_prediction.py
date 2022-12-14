import numpy as np
import pandas as pd
import sys
sys.path.append('/home/marios/projects')
from tools.DataManipulation import DataManipulation



def main():
    data_dict = importData()

    # Print the names of the dictionary keys
    print("Data Dict Keys: " + str(data_dict.keys()))

    # Assign dataframes
    status_df = data_dict['status']
    races_df = data_dict['races']
    sprint_results_df = data_dict['sprint_results']
    seasons_df = data_dict['seasons']
    constructors_df = data_dict['constructors']
    circuits_df = data_dict['circuits']
    constructors_standings_df = data_dict['constructor_standings']
    qualifying_df = data_dict['qualifying']
    results_df = data_dict['results']
    constructor_results_df = data_dict['constructor_results']
    lap_times_df = data_dict['lap_times']
    driver_standings_df = data_dict['driver_standings']
    drivers_df = data_dict['drivers']
    pit_stops = data_dict['pit_stops']




    ##############################################################################################################
    # What to keep
    # circuits -> circuitId | circuitRef | name | location | country
    # constructor_results -> raceId | constructorId | points
    # constructors -> constructorId | constructorRef | nationality | ??Wikipedia number of characters in page????
    # constructor_standings -> raceId | constructorId | points | position | wins
    # drivers -> driverId | dob (age) | nationality | url (feature wordCount)
    # driver_standings -> raceId | driverId | points | position | wins
    # lap_times -> raceId | driverId | lap | position | milliseconds
    # pit_stops -> raceId | driverId | stop | lap | time | milliseconds
    # qualifying -> raceId | driverId | constructorId | position | q1 | q2 | q3 (last 3 from string to time or milliseconds)
    # races -> raceId | year | round | circuitId | date | time
    # results -> raceId | driverId | constructorId | grid | position | positionOrder | points | laps | milliseconds | fastestLap | rank | fastestLapTime | fastestLapSpeed | statusId
    # seasons -> 
    # sprint_results -> raceId | driverId | constructorId | grid | position | positionOrder | points (acquired) | laps | milliseconds | fastestLap | fastestLapTime | statusId



    # Dataframe Selections
    circuits_df = circuits_df[['circuitId','location','country', 'alt', 'url']]
    circuits_df.rename(columns={'url': 'url_circuit'}, inplace=True)

    constructor_results_df = constructor_results_df[['raceId','constructorId','points']]

    constructors_df = constructors_df[['constructorId','nationality','url']]
    constructors_df.rename(columns={'url': 'url_constructors', 'nationality': 'constructor_nationality'}, inplace=True)

    constructors_standings_df = constructors_standings_df[['raceId','constructorId','points','position','wins']]

    drivers_df = drivers_df[['driverId','dob','nationality','url']]

    driver_standings_df = driver_standings_df[['raceId','driverId','points','position','wins']]

    lap_times_df = lap_times_df[['raceId','driverId','lap','position','milliseconds']]

    pit_stops = pit_stops[['raceId','driverId','stop','lap','time','milliseconds']]

    qualifying_df = qualifying_df[['raceId','driverId','constructorId','position','q1','q2','q3']]

    races_df = races_df[['raceId','year','round','circuitId','date','time']]

    results_df = results_df[['raceId','driverId','constructorId','grid','position','positionOrder','points','laps','milliseconds','fastestLap','rank','fastestLapTime','fastestLapSpeed','statusId']]

    sprint_results_df = sprint_results_df[['raceId','driverId','constructorId','grid','position','positionOrder','points','laps','milliseconds','fastestLap','fastestLapTime','statusId']]





    ################################################# Merge the dataframes to include all data #################################################################

    # Added to results dataframe the constructor points at the time of the race
    merged_df = pd.merge(results_df, constructor_results_df, how='left', left_on=['raceId', 'constructorId'], right_on=['raceId', 'constructorId'], suffixes=(None,'_constructor'))

    # Added race info per record
    merged_df = merged_df.merge(races_df, how='left', left_on=['raceId'], right_on=['raceId'], suffixes=(None,'_of_race'))

    # Merged circuit information
    merged_df = merged_df.merge(circuits_df, how='left', left_on=['circuitId'], right_on=['circuitId'], suffixes=(None,'_of_circuit'))

    # 
    merged_df = merged_df.merge(constructors_df, how='left', left_on=['constructorId'], right_on=['constructorId'], suffixes=(None,'_of_constructor'))








    ##############################################################################################################
    #Feature Engineering 

    # Create Manipulator object
    manipulator = DataManipulation()

    # Create WordCount feature from wikipedia pages.
    constructors_df['word_count'] = constructors_df.apply(lambda row: manipulator.getWordCount(row['url']), axis=1)
    print(constructors_df)





def importData():
    # Importing multiple data files in dictionary
    manipulator = DataManipulation()
    data = manipulator.data_to_dict(setPath="/home/marios/projects/Test_Project/formula-1-world-championship-1950-2020/")
    return data






if __name__ == "__main__":
    main()
