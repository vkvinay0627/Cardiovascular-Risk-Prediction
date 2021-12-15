# Missing Value Count Function
def show_missing(DataFrame):
    missing = DataFrame.columns[DataFrame.isnull().any()].tolist()
#     return missing

    # Missing data counts and percentage
    print('Missing Data Count')
    print(DataFrame[missing].isnull().sum().sort_values(ascending = False))
    print('--'*50)
    print('Missing Data Percentage')
    print(round(DataFrame[missing].isnull().sum().sort_values(ascending = False)/len(DataFrame)*100,2))
#-----------------------------------------------------------------------------------------------------------------------------#
def impute_nan_mean(df,variable):
    df[variable].fillna(df[variable].mean(),inplace = True)
    
def impute_nan_median(df,variable):
    df[variable].fillna(df[variable].median(),inplace = True)
    
def drop_column(df,variable):
    df.drop([variable],axis=1,inplace = True)
#-----------------------------------------------------------------------------------------------------------------------------#
def Categorical_columns(df):
    Categorical_columns = df.iloc[:,:]
    discrete_cat = []
    for var in Categorical_columns:
        if len(df[var].unique())<20:
            print(var, ' values: ', df[var].unique())
            discrete_cat.append(var)
        
    print('There are {} Categorical columns'.format(len(discrete_cat)))
      
def Numerical_columns(df):
    Numerical_columns = df.iloc[:,:]
    discrete_num = []
    for var in Numerical_columns:
        if len(df[var].unique())>10:
            print(var)
            discrete_num.append(var)
    print('There are {} Numerical columns'.format(len(discrete_num)))
#-----------------------------------------------------------------------------------------------------------------------------#