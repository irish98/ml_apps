# flake8: noqa
import streamlit as st
import pandas as pd
import plotly.express as px 

st.title('Hi, Here we have Live Sales Tracker')
st.subheader('Streamlit Application Usecase')

df = pd.read_csv(r"C:\Users\rishabh.saxena\Desktop\ML_Apps\Input_Sales_Data_v2.csv")

st.subheader("Sales Data")
st.dataframe(df.head())
# st.subheader("dataset stats")
# st.dataframe(df.describe())
# st.subheader("dataset summary")
# st.dataframe(df.info())
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df['Date'] = df['Date'].dt.date

selected_date = st.slider('Date slider', min_value = df['Date'].min(), max_value=df['Date'].max())

filtered_df = df[df['Date'] == selected_date]

st.write(filtered_df.groupby(['Manufacturer','Date']).agg({'Volume':"sum", 'Value': "sum"}).reset_index())

st.sidebar.image("logo.png", width=280)

# Plot line graph for top 5 manufacturers
manufacturer_sales = filtered_df.groupby('Manufacturer')['Value'].sum().reset_index()

# # Sort the manufacturers based on total volume sales and select top 5
top_5_manufacturers = manufacturer_sales.nlargest(5, 'Value')

# Plot bar chart with top 5 manufacturers and their total volume sales
fig = px.line(manufacturer_sales[manufacturer_sales['Manufacturer'].isin(top_5_manufacturers['Manufacturer'])],
              x='Manufacturer', y='Value', title='Top 5 Manufacturers Volume Sales Trends')
st.plotly_chart(fig)

# st.write(st.__version__)
# st.write(px.__version__)
# st.write(pd.__version__)

# Create a plot for each top manufacturer
# plt.figure(figsize=(10, 6))
# for manufacturer in top_5_manufacturers['Manufacturer']:
#     manufacturer_data = filtered_df[filtered_df['Manufacturer'] == manufacturer]
#     plt.plot(manufacturer_data['Date'], manufacturer_data['Volume'], label=manufacturer)

# # Add title and labels
# plt.title('Top 5 Manufacturers by Volume Sales')
# plt.xlabel('Date')
# plt.ylabel('Volume Sales')


st.subheader('Thank you for visiting')

# selected_date = st.slider('Select a date', min_value=df['Date'].min(), 
#                           max_value=df['Date'].max())


# # Filter the dataframe based on the selected date
# filtered_df = df[df['Date'] == selected_date]

# # New line add.