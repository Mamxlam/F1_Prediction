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

    # Create Manipulator object
    manipulator = DataManipulation()

    # Create WordCount feature from wikipedia pages.
    constructors_df['word_count'] = constructors_df.apply(lambda row: manipulator.getWordCount(row['url']), axis=1)
    print(constructors_df)

    # What to keep
    # circuits -> circuitId | circuitRef | name | location | country
    # constructor_results -> raceId | constructorId | points
    # constructors -> constructorId | constructorRef | nationality | ??Wikipedia number of characters in page????
    # 





def importData():
    # Importing multiple data files in dictionary
    manipulator = DataManipulation()
    data = manipulator.data_to_dict(setPath="/home/marios/projects/Test_Project/formula-1-world-championship-1950-2020/")
    return data






if __name__ == "__main__":
    main()
