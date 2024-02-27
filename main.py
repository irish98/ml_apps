# flake8: noqa
import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Live Sales Tracker for Manufacturer')
st.subheader('Streamlit Application Usecase')

df = pd.read_csv(r"C:\Users\rishabh.saxena\Desktop\ML_Apps\Input_Sales_Data_v2.csv")

st.subheader("dataset header")
st.dataframe(df.head())
# st.subheader("dataset stats")
# st.dataframe(df.describe())
# st.subheader("dataset summary")
# st.dataframe(df.info())
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.date

selected_date = st.slider('Date slider', min_value = df['Date'].min(), max_value=df['Date'].max())

filtered_df = df[df['Date'] == selected_date]

st.write(filtered_df.groupby(['Manufacturer','Date']).agg({'Volume':"sum", 'Value': "sum"}).reset_index())

st.sidebar.image("logo.png", width=200)

# Plot line graph for top 5 manufacturers
manufacturer_sales = filtered_df.groupby('Manufacturer')['Value'].sum().reset_index()

# Sort the manufacturers based on total volume sales and select top 5
top_5_manufacturers = manufacturer_sales.nlargest(5, 'Value')

# Plot bar chart with top 5 manufacturers and their total volume sales
fig = px.line(manufacturer_sales[manufacturer_sales['Manufacturer'].isin(top_5_manufacturers['Manufacturer'])],
              x='Manufacturer', y='Value', title='Top 5 Manufacturers Volume Sales Trends')
st.plotly_chart(fig)
# selected_date = st.slider('Select a date', min_value=df['Date'].min(), 
#                           max_value=df['Date'].max())


# # Filter the dataframe based on the selected date
# filtered_df = df[df['Date'] == selected_date]

# # New line add.