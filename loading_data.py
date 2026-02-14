import pandas as pd

def load_data():
    print("Loading Data.......")
    df=pd.read_csv("work_from_home_burnout_dataset.csv")
    #print(df.head(3))

    #print(df.info())
    #Print("The summary statistics of the dataset",df.describe())
    return df

