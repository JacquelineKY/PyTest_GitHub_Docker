import pandas as pd



def compute_median_mean_diff(df): 
    age_column = df['Age']
    #scores_column = df['Scores']
    mean_Age = age_column.mean()
    median_Age = age_column.median()
    diff_Age = mean_Age - median_Age

    result = pd.DataFrame({'Mean_Age': [mean_Age], 'Median_Age': [median_Age], 'Difference_Age': [diff_Age]})
    
    return result

