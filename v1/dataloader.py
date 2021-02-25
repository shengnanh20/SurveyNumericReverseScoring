import csv
import numpy as np
import pandas as pd


if __name__ == '__main__':
    file_path = 'ASIST Experiment 1 Surveys_June 20, 2020_choice output - Sheet2.csv'
    # file_path = 'study-2_pilot-2_2021.02_NotHSRData_SurveysNumeric_CondBtwn-na_CondWin-na_Trial-na_Team-TM000001-000006_Member-na_Vers-1.csv'
    results_path = 'results.csv'
    question_num = 15
    subject_num = 11
    reverse_que_list = [2,6,8,10,11,12,13,15]
    print('Reverse Scored Questions:', reverse_que_list)

    with open(file_path, 'r') as csvfile:
        # data1 = csv.DictReader(csvfile)
        # rows1= [row for row in data1]
        data = csv.reader(csvfile)
        rows = [row for row in data]

    scores = np.array(rows[1:subject_num])
    results = []
    for i in range(scores.shape[0]):
        subject_id = scores[i][0]
        sub_score = []
        for j in range(1, question_num):
            score = int(scores[i][j])
            if score == -99:
                continue
            elif j in reverse_que_list:
                sub_score.append(8-score)
            else:
                sub_score.append(score)
        mean_score = np.mean(sub_score)
        print('Reversed score of %s is: ' %subject_id, sub_score)
        print('Mean score of %s is: %.3f' %(subject_id, mean_score), '\n')
        results.append([subject_id, mean_score])

    result_frame = pd.DataFrame(results, columns=['subject_id', 'mean_score'])
    result_frame.to_csv(results_path)
