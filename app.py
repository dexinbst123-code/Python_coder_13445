import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

data = {
    'Square_Feet': [1500, 2000, 1200, 2500, 1800, 3000, 1400, 2200, 1600, 2800],
    'Bedrooms': [3, 4, 2, 4, 3, 5, 2, 4, 3, 5],
    'Bathrooms': [2.0, 2.5, 1.0, 3.0, 2.0, 3.5, 1.5, 2.5, 2.0, 3.0],
    'Year_Built': [1995, 2005, 1980, 2015, 2000, 2020, 1990, 2010, 2002, 2018],
    'Price': [250000, 320000, 180000, 450000, 290000, 550000, 210000, 380000, 275000, 510000]
}


df = pd.DataFrame(data)

print(df)

x = df[['Square_Feet', 'Bedrooms']]
y = df['Price']

pipeline = Pipeline([
    ("impute", SimpleImputer()),
    ("scaler", StandardScaler()),  
    ("poly", PolynomialFeatures()),
    ("model", LinearRegression())
])

param_grid = {
    'impute__strategy': ["mean",'median'],
    'poly__degree': [1,2,3,4],
    'model__fit_intercept': [True, False]
}
grid_search = GridSearchCV(estimator=pipeline, cv=2, scoring='r2',param_grid=param_grid)

grid_search.fit(x,y)

data = pd.DataFrame(data=[[1200,3]],columns=['Square_Feet','Bedrooms'])
grid_search.predict(data)

st.title(" House Price Predictor")
st.subheader("Enter house Detail")

st.sidebar.header("WELCOME !")


st.header("Input Features")
sq_ft = st.number_input("Square Feet", min_value=500, max_value=5000, value=1500)
beds = st.slider("Bedrooms", 1, 10, 3)


if st.button("Predict Price"):
    input_data = pd.DataFrame([[sq_ft, beds]], 
                             columns=['Square_Feet', 'Bedrooms'])
    
    prediction = grid_search.predict(input_data)

    st.success(f"Estimated House Price: **${prediction[0]:,.2f}**")




