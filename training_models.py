from preprocessing_data import process_data
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import r2_score,accuracy_score


X_train, X_test, y1_train,y1_test,y2_train,y2_test=process_data()
print('The column names are:',X_train.columns)
#Linear Regression
with mlflow.start_run(run_name="Linear_Regression_Model"):
    linear_model=LinearRegression()
    linear_model.fit(X_train,y2_train)

    linearpredict_y2=linear_model.predict(X_test)
    linear_model_R2=r2_score(y_true=y2_test,y_pred=linearpredict_y2)

    mlflow.log_param('Model type','Linear Regression')
    mlflow.log_metric('R2 Score', linear_model_R2)

with mlflow.start_run(run_name="Logistic_Regression_Model"): #Logistic Regression

    logistic_model=LogisticRegression()
    logistic_model.fit(X_train,y1_train)

    logisticpredict_y1=logistic_model.predict(X_test)
    logistic_model_accuracy=accuracy_score(y_true=y1_test,y_pred=logisticpredict_y1)

    mlflow.log_param('Model type','Logistic Regression')
    mlflow.log_metric('Accuracy', logistic_model_accuracy)


with mlflow.start_run(run_name="Random_Forest_Regressor"):#Random Forest Regressor
    random_regressor=RandomForestRegressor()
    random_regressor.fit(X_train,y2_train)

    randompredict_y2=random_regressor.predict(X_test)
    random_model_r2=r2_score(y_true=y2_test,y_pred=randompredict_y2)

    mlflow.log_param('Model type','Random Forest Regressor')
    mlflow.log_metric('R2 Score', random_model_r2)

with mlflow.start_run(run_name="Random Forest Classifier"):  #Random Forest Classifier
    Random_Classifier=RandomForestClassifier()
    Random_Classifier.fit(X_train,y1_train)

    randompredict_y1=Random_Classifier.predict(X_test)
    random_model_accuracy=accuracy_score(y_true=y1_test,y_pred=randompredict_y1)

    mlflow.log_param('Model type','Random Forest Classifier')
    mlflow.log_metric('Accuracy', logistic_model_accuracy)

print('---------------------------Linear Regression---------------------------')
print("The linear regression coefficients are:",linear_model.coef_)
print("The linear regression intercept is are:",linear_model.intercept_)

print('---------------------------Logistic Regression---------------------------')
print("The logistic regression coefficients are:",logistic_model.coef_)
print("The logistic regression intercept is are:",logistic_model.intercept_)


print('---------------------------Random Forest Regressor---------------------------')
print("The feature importance for random forest regressor on burnout score are:",100*random_regressor.feature_importances_)


print('---------------------------Random Forest Regressor---------------------------')
print("The feature importance for random forest Classifier on burnout level are:",100*Random_Classifier.feature_importances_)