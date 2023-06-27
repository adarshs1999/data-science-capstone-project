import streamlit as st
import pickle

st.title('Vehicle Price Prediction with ML')
st.text("Enter the vehicle details to get an estimated value of the vehicle")

c1, c2 = st.columns(2)

with st.form("Form", clear_on_submit=True):
    with c1:
        vehicle = st.text_input("vehicle name")
        brandName = vehicle.split(" ")[0].title()
        modelName = " ".join(vehicle.split(" ")[1:3]).title()
        kilometer = st.number_input("kilometer driven", max_value=172500)
        fuel = st.selectbox("Fuel type", ["Choose type", "Petrol","LPG", "Electric", "Diesel", "CNG"])
        seller = st.selectbox("Seller type", ["Dealer", "Individual", "Trustmark Dealer"])
                
    Years = [2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010,
            2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999,
            1998, 1997, 1996, 1995, 1992]
    with c2:    
        year = st.selectbox("Year of purchase", Years, index=0)

        gearbox = st.selectbox("gearbox type", ["Manual", "Automatic"])
        owner = st.selectbox("Owner type", ["First Owner", "Second Owner", "other"])
        
    state = st.form_submit_button("Predict")

model_test_data = [[brandName, modelName, year, kilometer, fuel, seller, gearbox, owner]]

mlModel = pickle.load(open('MyPipe.pkl', 'rb'))
pred = mlModel.predict(model_test_data)

if state:
        st.write("The calculated value for the vehicle is:")
        st.write(pred[0])
