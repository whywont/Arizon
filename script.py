import os
import pandas as pd
import openpyxl


def get_files():
    drive_path = 'C:\\Users\\Andrew\\Documents\\Arizona'
    path_list = []
    pl2 = []
    #Walk through dir and get the paths of all the csv files. Append to list
    for root, dirs, files in os.walk(drive_path):
            # print(os.listdir(dirs)[0])
            for name in files:
                if name.startswith("00") and (name.endswith('.XLSX') | name.endswith('.XLS')):
                    #HOW to get first occurence
                    temp_list = []
                    path_list.append(os.path.join(root, name))
            # pl2.append([name for name in files if name.startswith("00") and (name.endswith('.XLSX') | name.endswith('.XLS'))][0])

    # print(path_list)
    # print(pl2)
    return path_list

#Main function that will call all other functions. Takes path from app.py (GUI)
def controller():

    files = get_files()
    df = clean_oofr(files)



def clean_oofr(files):

    #To hold list of dicts
    matrix = []
    for file in files:
        table = {}
        #Make sure file can be opened.
        try:
            temp = pd.read_excel(file)
        except:
            continue
        if 'F/A' in temp.columns:
            table['FA count'] = temp['F/A'].count()
        elif 'FA' in temp.columns:
            table['FA count'] = temp['FA'].count

        if 'Builder' in temp.columns:
            table['Builder'] = temp['Builder'].values[0]
        elif 'BUILDER' in temp.columns:
            table['Builder'] = temp['BUILDER'].values[0]
        
        if 'Subdivision' in temp.columns:
            table['Subdivision'] = temp['Subdivision'].values[0]
        elif 'SUBDIVISION' in temp.columns:
            table['Subdivision'] = temp['SUBDIVISION'].values[0]

        matrix.append(table)

    df = pd.DataFrame(matrix)

    df['FA count'].fillna(0, inplace=True)
    df.fillna("No Information Available", inplace=True)

    df.to_csv('oofr_stats.csv', index=False)

controller() 


