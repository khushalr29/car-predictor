import streamlit as st
import pickle 
import pandas as pd
import sklearn

model=pickle.load(open("LinearRegressionModel.pkl",'rb'))

def predict(name,company,year,kms,fuel):
    ans = model.predict(pd.DataFrame([[name,company,year,kms,fuel]],columns=['name','company','year','kms_driven','fuel_type']))
    return ans[0]


st.set_page_config(page_title="Car Predicator",layout='wide')
petrol_list =['Petrol', 'Diesel', 'LPG']
car_data=pickle.load(open('cardata.pkl','rb'))
name=st.selectbox("",car_data['name'],placeholder='Car_Model_Name',index=None)
company=st.selectbox("",car_data['company'],placeholder='Car_Company',index=None)
year=st.number_input("Purchase_Year",value=2024,max_value=2025,min_value=1900)
kms=st.number_input("Kms_Driven",value=0,max_value=500000)
fuel=st.selectbox("",petrol_list,placeholder='fuel_type',index=None)

if st.button(' Check Price'):
    abc = predict(name,company,year,kms,fuel)
    ans = "Estimated Price is  : "+str(int(abc))
    st.success(ans)


