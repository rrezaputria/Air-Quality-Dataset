import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# data
df = pd.read_csv('dashboard/combined_df.csv.gz', compression='gzip')
df.columns = ['No', 'Year', 'Month', 'Day', 'Hour', 'PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3',
              'Temperature', 'Pressure', 'DewPoint', 'Rain', 'WindDirection', 'WindSpeed', 
              'Station', 'WindDirectionDegree', 'Date', 'AQI_PM2.5', 'AQI_PM10', 'AQI_SO2', 
              'AQI_NO2', 'AQI_CO', 'AQI_O3', 'AQI_Category_PM2.5', 'AQI_Category_PM10', 
              'AQI_Category_SO2', 'AQI_Category_NO2', 'AQI_Category_CO', 'AQI_Category_O3']

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set up the Streamlit app
st.set_page_config(page_title="Air Quality Dashboard", layout="centered")
st.sidebar.title("Navigation")

# Navigasi
page = st.sidebar.radio("Select Page:", ("Home", "Pollutant Trend Visualization", "AQI Trend"))

# Home page
if page == "Home":
    st.title("Air Quality Dashboard")
    st.image("air_quality_image.jpg")  # Make sure this image exists in the same directory
    st.write("This dashboard provides insights into air quality trends over time.")

# Pollutant trend visualization page
elif page == "Pollutant Trend Visualization":
    st.title("Pollutant Trend Visualization")

    # Pollutan
    pollutant_options = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
    selected_pollutants = st.multiselect("Select Pollutants:", pollutant_options)

    if len(selected_pollutants) > 0:  # Add a check for empty selections

        # Average day
        if st.checkbox("Show Daily Average"):
            daily_avg = df.groupby('Date')[selected_pollutants].mean().reset_index()
            plt.figure(figsize=(10, 5))
            for pollutant in selected_pollutants:
                sns.lineplot(data=daily_avg, x='Date', y=pollutant, label=pollutant)
            plt.title(f'Daily Average of Selected Pollutants')
            plt.xlabel('Date')
            plt.ylabel('Concentration')
            plt.legend(title='Pollutants')
            st.pyplot(plt)

        # Time select
        time_option = st.radio("Select Time Range:", ('Monthly', 'Yearly'))

        # Year select
        if time_option == 'Yearly':
            selected_year = st.selectbox("Select Year:", df['Year'].unique())
            filtered_data = df[df['Year'] == selected_year]
        else:
            filtered_data = df

        # Visualization trend
        if time_option == 'Monthly':
            trend_data = filtered_data.groupby(['Year', 'Month'])[selected_pollutants].mean().reset_index()
            trend_data['Date'] = pd.to_datetime(trend_data[['Year', 'Month']].assign(Day=1))

            # Visualisasi tren bulanan
            plt.figure(figsize=(10, 5))
            for pollutant in selected_pollutants:
                sns.lineplot(data=trend_data, x='Date', y=pollutant, label=pollutant)
            plt.title(f'Monthly Trend of Selected Pollutants')
            plt.xlabel('Date')
            plt.ylabel('Concentration')
            plt.legend(title='Pollutants')
            st.pyplot(plt)
        else:
            trend_data = filtered_data.groupby('Year')[selected_pollutants].mean().reset_index()

            plt.figure(figsize=(10, 5))
            trend_data_melted = trend_data.melt(id_vars='Year', value_vars=selected_pollutants, 
                                                var_name='Pollutant', value_name='Concentration')
            sns.barplot(data=trend_data_melted, x='Year', y='Concentration', hue='Pollutant')
            plt.title(f'Yearly Trend of Selected Pollutants')
            plt.xlabel('Year')
            plt.ylabel('Concentration')
            plt.legend(title='Pollutants')
            st.pyplot(plt)

# AQI trend page
elif page == "AQI Trend":
    st.title("AQI Trend Visualization")

    # AQI select
    aqi_options = ['AQI_PM2.5', 'AQI_PM10', 'AQI_SO2', 'AQI_NO2', 'AQI_CO', 'AQI_O3']
    selected_aqi = st.multiselect("Select AQI Types:", aqi_options)

    if len(selected_aqi) > 0:  # Add a check for empty selections

        # Average day
        if st.checkbox("Show Daily Average"):
            daily_aqi_avg = df.groupby('Date')[selected_aqi].mean().reset_index()
            plt.figure(figsize=(10, 5))
            for aqi in selected_aqi:
                sns.lineplot(data=daily_aqi_avg, x='Date', y=aqi, label=aqi)
            plt.title(f'Daily Average of Selected AQI Types')
            plt.xlabel('Date')
            plt.ylabel('AQI Concentration')
            plt.legend(title='AQI Types')
            st.pyplot(plt)

        time_option = st.radio("Select Time Range for AQI:", ('Monthly', 'Yearly'))
        if time_option == 'Yearly':
            selected_year = st.selectbox("Select Year for AQI:", df['Year'].unique())
            filtered_aqi_data = df[df['Year'] == selected_year]
        else:
            filtered_aqi_data = df

        if time_option == 'Monthly':
            trend_aqi_data = filtered_aqi_data.groupby(['Year', 'Month'])[selected_aqi].mean().reset_index()
            trend_aqi_data['Date'] = pd.to_datetime(trend_aqi_data[['Year', 'Month']].assign(Day=1))

            # Visualisasi tren bulanan AQI
            plt.figure(figsize=(10, 5))
            for aqi in selected_aqi:
                sns.lineplot(data=trend_aqi_data, x='Date', y=aqi, label=aqi)
            plt.title(f'Monthly Trend of Selected AQI Types')
            plt.xlabel('Date')
            plt.ylabel('AQI Concentration')
            plt.legend(title='AQI Types')
            st.pyplot(plt)
        else:
            trend_aqi_data = filtered_aqi_data.groupby('Year')[selected_aqi].mean().reset_index()

            # Visualisasi tren tahunan AQI
            plt.figure(figsize=(10, 5))
            trend_aqi_data_melted = trend_aqi_data.melt(id_vars='Year', value_vars=selected_aqi, 
                                                        var_name='AQI Type', value_name='Concentration')
            sns.barplot(data=trend_aqi_data_melted, x='Year', y='Concentration', hue='AQI Type')
            plt.title(f'Yearly Trend of Selected AQI Types')
            plt.xlabel('Year')
            plt.ylabel('AQI Concentration')
            plt.legend(title='AQI Types')
            st.pyplot(plt)
