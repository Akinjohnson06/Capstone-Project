""" An easy made functions for my personal use """

def summary(table): # shows the summary of the Data
    print('1 - Top 5 Records of the dataset')
    print(table.head())
    print()
    
    print('2 - Bottom 5 Records of the dataset')
    print(table.tail())
    print()
    
    print('3 - Columns of the dataset')
    print(table.columns)
    print()
    
    print('4 - Number of Rows and Columns of the dataset')
    print(table.shape)
    print()
    
    print('5 - Data types')
    print(table.dtypes)
    print()
    
    print('6 - Summary of the Dataset')
    print(table.info())
    print()
    
    print('7 - Sum of missing Values')
    print(table.isnull().sum())
    print()
    
    print('8 - Dataset summary')
    print(table.describe())
    print()

def outliers(df, col): # gives you an array of the outliers
    """
    Detects outliers in a given dataset using the Interquartile Range (IQR) method.

     Parameters:
    - df: The name of the Dataset you imported
    - col: The column in the dataset you want to check for outliers
    Returns:
    - outliers: NumPy array, containing the indices of the detected outliers.
    """
    IQ1 = df[col].quantile(0.25)
    IQ3 = df[col].quantile(0.75)
    IQR = IQ3 - IQ1
    
    lower_bound = IQ1 - 1.5 * IQR
    upper_bound = IQ3 + 1.5 * IQR
    index = df.index[(df[col] < lower_bound) | (df[col] > upper_bound)]
    return index

def del_outliers(df, column, threshold=3): # deletes outliers in the dataset and returns a clean dataset 
    """
    Removes outliers from a given dataset based on the provided indices.

    Parameters:
    - df: The name of the Dataset you imported
    - column: The column in the dataset you want to delete
    
    Returns:
    - It returns a cleaned Dataset without the outliers
    """
    mean = df[column].mean()
    std_dev = df[column].std()
    
    lower_bound = mean - threshold * std_dev #PEMDAS
    upper_bound = mean + threshold * std_dev
    # remove outliers
    
    df = df[(df[column]>= lower_bound) & (df[column]<= upper_bound)]
    return df

def viz_outliers(df, column): # visualizes a boxplot that also show outliers
    """
    Visualize outliers with the use of boxplot

    Parameters:
    - df: The name of the Dataset you imported
    - column: The column in the dataset you want to visualize
    
    Returns:
    - It returns a boxplot that shows if the column has outliers
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    sns.boxplot(data=df, x=column)