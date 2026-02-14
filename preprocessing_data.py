from loading_data import load_data,pd
from sklearn.preprocessing import OrdinalEncoder,StandardScaler
from sklearn.model_selection import train_test_split

def process_data():
    df=load_data()

    print('Applying one hot encoding.....')
    encoder=OrdinalEncoder()
    encoded=encoder.fit_transform( df[['day_type','burnout_risk']])
    encoded_df=pd.DataFrame(data=encoded, columns=['day_type','burnout_risk'])

    df=pd.merge(df.drop(columns=['day_type','burnout_risk']),encoded_df,how='cross')

    X=df.drop(columns=['user_id','burnout_score','burnout_risk'])


    print('Appying Standard Scaler to data fields (Normalizing)........')
    scaler=StandardScaler()
    X=pd.DataFrame(scaler.fit_transform(X),columns=X.columns.tolist())

    y1=df['burnout_risk']
    y2=df['burnout_score']
    
    print('Splitting the data in training and testing')
    
    X_train, X_test, y1_train,y1_test=train_test_split(X,y1, test_size=0.25,random_state=27)
    X_train, X_test, y2_train,y2_test=train_test_split(X,y2, test_size=0.25,random_state=27)

    return X_train, X_test, y1_train,y1_test,y2_train,y2_test