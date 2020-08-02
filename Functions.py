import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

class color:

    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    
def return_categorical_related_feature(data, feature, alpha=0.05):
    
    print(color.BOLD + color.BLUE + "Correlations of the features" + color.END)
    print(color.BOLD + color.RED + "{:<20} {:<20}".format('feature','p value') + color.END)
    for f in data.columns:
        
        actual_table = pd.crosstab(columns=data[feature], index=data[f])
        col_sum = actual_table.sum(axis=1)
        row_sum = actual_table.sum(axis=0)      
        stat, p, dof, expected_table = chi2_contingency(actual_table)
        
        if (alpha > p):
            print("{:<20} {:<20}".format(f, p))
            
    
def return_categorical_related_feature_1(data, feature, alpha=0.5):
    
        print(color.BOLD + color.BLUE + " "*30 + "Correlations of the features" + color.END)
        for f in data.columns:
            print(f)
            col_sum = actual_table.sum(axis=1)
            row_sum = actual_table.sum(axis=0)
            expected_table = np.zeros((len(row_sum), len(col_sum)))           
            actual_table = pd.crosstab(columns=data[feature], index=data[f])
            
            for i in range(len(data["school"].unique())):
                for j in range(len(data["sex"].unique())):
                    expected_table[i][j] = (col_sum[i]*row_sum[j])/col_sum.sum()
              
            chi_table = np.zeros((len(row_sum), len(col_sum)))
            for i in range(len(row_sum)):
                 for j in range(len(row_sum)):
                    chi_table[i][j] = ((actual_table[i][j]-expected_table[i][j])**2)/expected_table[i][j]    
            chi_square_val = chi_table.sum()
        
            degree_freedom = (len(data[feature])-1)*(len(data[f])-1)
            critical = chi2.ppf(1-alpha, degree_freedom)
            
           # correlated_feature[f] = 
        
def return_correlated_features(data, feature, significance=0.1, need=False):

        print(color.BOLD + color.BLUE + " "*30 + "Correlations of the features" + color.END)
        corr_matrix = data.corr()
        correlations = corr_matrix[feature].sort_values(ascending=False)
        positive_corr = correlations[correlations >= significance][1:].to_dict()
        negative_corr = correlations[correlations <= -significance].to_dict()
        
        if need:
            return [positive_corr, negative_corr]
        
        print(color.BOLD + color.RED + "{:<20} {:<15} {:<20} {:<20} {:<15}".format('feature','relation', '',
                                                                                   'feature', 'relation') + color.END)
        if (len(positive_corr) > len(negative_corr)):
            for i in range(len(positive_corr)):
                negative_corr[str(" "*i)] = " "*i
        elif (len(positive_corr) < len(negative_corr)) :
            for i in range(len(negative_corr)):
                positive_corr[str(" "*i)] = " "*i
                
        for val_1, val_2 in zip(positive_corr.items(), negative_corr.items()):
            k1, v1 = val_1
            k2, v2 = val_2
            
            try:
                k1, k2, v1, v2 = k1, k2, round(float(v1), 2), round(float(v2), 2)
            
            except:
                
                try:
                    if (v1.replace(".", "").isdigit()):
                        v1 = round(float(v1), 2)
                    else:
                        v2 = round(float(v2), 2)
                except:
                    if (v2.replace(".", "").isdigit()):
                        v2 = round(float(v2), 2)
                    else:
                        v1 = round(float(v1), 2)
                        
            print("{:<20} {:<15} {:<20} {:<20} {:<15}".format(k1, v1, "", k2, v2))
