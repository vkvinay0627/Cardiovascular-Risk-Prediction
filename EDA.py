def Categorical_columns_list(df):
    Categorical_columns = df.iloc[:,:]
    discrete_cat = []
    for var in Categorical_columns:
        if len(df[var].unique())<20:
            discrete_cat.append(var)
    return discrete_cat

    

def Numerical_columns_list(df):
    Numerical_columns = df.iloc[:,:]
    discrete_num = []
    for var in Numerical_columns:
        if len(df[var].unique())>10:
            discrete_num.append(var)
    return discrete_num


def univariate_categorical_EDA(df,discrete_cat):
    for col in discrete_cat:
        counts = df[col].value_counts().sort_index()
        import matplotlib.pyplot as plt 
        fig = plt.figure(figsize=(6, 5))
        ax = fig.gca()
        counts.plot.bar(ax = ax, color='steelblue')
        ax.set_title(col + ' counts')
        ax.set_xlabel(col) 
        ax.set_ylabel("Frequency")
    plt.show()
    
def univariate_numerical_EDA(df,discrete_num):
    for col in discrete_num:
        import matplotlib.pyplot as plt 
        fig = plt.figure(figsize=(9, 6))
        ax = fig.gca()
        feature = df[col]
        feature.hist(bins=50, ax = ax)
        ax.axvline(feature.mean(), color='magenta', linestyle='dashed', linewidth=2)
        ax.axvline(feature.median(), color='cyan', linestyle='dashed', linewidth=2)    
        ax.set_title(col)
    plt.show()
    

def heat_map(df):
    corr = df.corr()
    import matplotlib.pyplot as plt 
    plt.figure(figsize=(15,10))
    import seaborn as sns 
    sns.heatmap(corr, annot=True, annot_kws={'size':15},cmap='coolwarm')