import pandas as pd
import json

def excel_to_json(excel_file_path, columns_of_interest, json_file_path):
    # Load Excel file into a DataFrame
    df = pd.read_excel(excel_file_path)

    # Select columns of interest from the DataFrame
    player_data_df = df[columns_of_interest]

    # Convert DataFrame to list of dictionaries
    player_data_list = player_data_df.to_dict(orient='records')

    # Write list of dictionaries to a JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(player_data_list, json_file)

# Example usage:
excel_file_path = '/Users/arslantariq/Desktop/2021-2022_Football_Player_Stats_final.xlsm'
columns_of_interest = [
    'Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', 'MP', 'Starts', 'Min', '90s',
    'Goals', 'Shots', 'SoT', 'SoT%', 'G/Sh', 'G/SoT', 'ShoDist', 'ShoFK', 'ShoPK', 'PKatt',
    'PasTotCmp', 'PasTotAtt', 'PasTotCmp%', 'PasTotDist', 'PasTotPrgDist', 'PasShoCmp', 'PasShoAtt',
    'PasShoCmp%', 'PasMedCmp', 'PasMedAtt', 'PasMedCmp%', 'PasLonCmp', 'PasLonAtt', 'PasLonCmp%',
    'Assists', 'PasAss', 'Pas3rd', 'PPA', 'CrsPA', 'PasProg', 'PasAtt', 'PasLive', 'PasDead', 'PasFK',
    'TB', 'PasPress', 'Sw', 'PasCrs', 'CK', 'CkIn', 'CkOut', 'CkStr', 'PasGround', 'PasLow', 'PasHigh',
    'PaswLeft', 'PaswRight', 'PaswHead', 'TI', 'PaswOther', 'PasCmp', 'PasOff', 'PasOut', 'PasInt',
    'PasBlocks', 'SCA', 'ScaPassLive', 'ScaPassDead', 'ScaDrib', 'ScaSh', 'ScaFld', 'ScaDef',
    'GCA', 'GcaPassLive', 'GcaPassDead', 'GcaDrib', 'GcaSh', 'GcaFld', 'GcaDef', 'Tkl', 'TklWon',
    'TklDef3rd', 'TklMid3rd', 'TklAtt3rd', 'TklDri', 'TklDriAtt', 'TklDri%', 'TklDriPast', 'Press',
    'PresSucc', 'Press%', 'PresDef3rd', 'PresMid3rd', 'PresAtt3rd', 'Blocks', 'BlkSh', 'BlkShSv',
    'BlkPass', 'Int', 'Tkl+Int', 'Clr', 'Err', 'Touches', 'TouDefPen', 'TouDef3rd', 'TouMid3rd',
    'TouAtt3rd', 'TouAttPen', 'TouLive', 'DriSucc', 'DriAtt', 'DriSucc%', 'DriPast', 'DriMegs',
    'Carries', 'CarTotDist', 'CarPrgDist', 'CarProg', 'Car3rd', 'CPA', 'CarMis', 'CarDis', 'RecTarg',
    'Rec', 'Rec%', 'RecProg', 'CrdY', 'CrdR', '2CrdY', 'Fls', 'Fld', 'Off', 'Crs', 'TklW', 'PKwon',
    'PKcon', 'OG', 'Recov', 'AerWon', 'AerLost', 'AerWon%'
]
json_file_path = '/Users/arslantariq/Desktop/Football_stat_AWS/player_data.json'

excel_to_json(excel_file_path, columns_of_interest, json_file_path)
