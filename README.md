# Air Quality Dashboard

This project aims to analyze air quality data, covering pollutants such as **PM2.5**, **PM10**, **SO2**, **NO2**, **CO**, and **O3**, alongside weather factors like **temperature**, **air pressure**, and **rainfall**. The goal is to understand the trends, analyze correlations, and visualize air quality conditions across different locations.

## Setup Environment with Anaconda

1. Create a new environment and install Python:
    ```bash
    conda create --name air-quality-ds
    conda activate air-quality-ds
    ```

2. Install Streamlit and other dependencies:
    ```bash
    conda install -c conda-forge streamlit
    ```

3. **Run Streamlit App:**
    ```bash
    streamlit run submission/dashboard/dashboard.py
    ```

## Setup Environment with Shell/Terminal

Create the necessary directories and files for the project:
```bash
mkdir -p submission/dashboard
mkdir -p submission/data
touch submission/dashboard/combined_df.csv
touch submission/dashboard/dashboard.py
touch submission/data/data_1.csv
touch submission/data/data_2.csv
touch submission/Project-Air-Quality.ipynb
touch submission/README.md
touch submission/requirements.txt
touch submission/url.txt
