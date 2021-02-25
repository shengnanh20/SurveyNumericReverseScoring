import csv
import numpy as np
import pandas as pd


if __name__ == '__main__':
    file_path = 'study-2_pilot-2_2021.02_NotHSRData_SurveysNumeric_CondBtwn-na_CondWin-na_Trial-na_Team-TM000001-000006_Member-na_Vers-1.csv'
    results_path = 'results.csv'
    question_num = 15  # total question number
    reverse_que_list = [2,6,8,10,11,12,13,15]  # questions need to be reverse scored
    print('Reverse Scored Questions:', reverse_que_list)

    df = pd.read_csv(file_path)
    temp = df[['Q8_1','Q8_2','Q8_3','Q8_4','Q8_5','Q8_6','Q8_7','Q8_8','Q8_9','Q8_10','Q8_11','Q8_12','Q8_13','Q8_14','Q8_15']]
    temp = temp.apply(pd.to_numeric,errors='coerce')
    for i in range(question_num):
        if i+1 in reverse_que_list:
            temp.iloc[:, i] = 8-temp.iloc[:, i]
        else:
            continue

    temp['mean_score'] = temp.mean(axis=1)
    # temp = temp.dropna(axis=0, how='any')
    
    temp = pd.concat([df['Q5'], df['Q185'], temp], axis=1)
    print(temp)
    temp.to_csv(results_path)
