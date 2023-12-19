import streamlit as st
import pandas as pd


import numpy as np
import pandas as pd
import sklearn


from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split 
from sklearn import metrics 
from sklearn.metrics import classification_report

from sklearn.model_selection import GridSearchCV
import xgboost as xgb
from xgboost import XGBClassifier

st.write("""
# Churn Problem App
This app predicts the **exited people**!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    Gender = st.sidebar.slider('Gender', 0, 1, 1)
    CreditScore = st.sidebar.slider('Credit Score', 200, 1000, 50)
    Geography = st.sidebar.slider('Geography', 0, 2, 1)
    Age = st.sidebar.slider('Age', 20, 60, 2)
    Tenure = st.sidebar.slider('Tenure', 1,11, 1)
    Balance = st.sidebar.slider('Balance', 0,150000, 20000)
    NumOfProducts = st.sidebar.slider('NumOfProducts', 1,4, 1)
    HasCrCard = st.sidebar.slider('HasCrCard',0,1,1)
    IsActiveMember = st.sidebar.slider('IsActiveMember',0,1,1)
    EstimatedSalary = st.sidebar.slider('EstimatedSalary',5000,150000,5000)
    data = {'CreditScore': CreditScore,
            'Geography': Geography,
            'Gender': Gender,
            'Age': Age,
            'Tenure':Tenure,
            'Balance':Balance,
            'NumOfProducts':NumOfProducts,
            'HasCrCard':HasCrCard,
            'IsActiveMember': IsActiveMember,
            'EstimatedSalary':EstimatedSalary
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

churn = pd.read_csv(r'C:\Users\satar\Downloads\Compressed\Project 2 - Churn modelling\Churn.csv')

labelGender = LabelEncoder()
churn['Gender'] = labelGender.fit_transform(churn['Gender'])
labelGeography = LabelEncoder()
churn['Geography'] = labelGeography.fit_transform(churn['Geography'])

X = churn.drop(['RowNumber','CustomerId','Surname','Exited'],axis=1)
Y = churn['Exited']

Gen = {'Male':1,'Female':0}
Geo = {'France':0,'Spain':2,'Germany':1}
st.subheader('Class labels and their corresponding index number')
st.write(pd.DataFrame(Gen,index=[0]))
st.write(pd.DataFrame(Geo,index=[0]))

sc = StandardScaler()
X= sc.fit_transform(X)

xgb_cls = XGBClassifier(use_label_encoder=False,booster='dart',objective='binary:logistic',learning_rate=0.02,max_depth=4,min_child_weight=7,gamma=0.3,colsample_bytree=0.55,n_estimators=700,reg_alpha=0.5)

xgb_cls.fit(X, Y)

prediction = xgb_cls.predict(sc.transform(df))
prediction_proba = xgb_cls.predict_proba(sc.transform(df))


# st.subheader('Prediction')
# st.write(.target_names[prediction])
# #st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
