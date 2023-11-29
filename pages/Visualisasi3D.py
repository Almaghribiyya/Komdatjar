import pandas as pd
import plotly.express as px
import streamlit as st

# Load the dataset
csv_path1 = "D:\KDJK\Visualisasi\pages\CICDS_Wednesday.csv"
df = pd.read_csv(csv_path1)

# Display the dataset
st.dataframe(df.head())

# Filter and process the data
kolom_timestamp_label_ip = df[[' Source IP', ' Label', ' Timestamp']]
label_counts_ip = kolom_timestamp_label_ip.groupby([' Source IP', ' Label', ' Timestamp']).size().reset_index(name='Jumlah')

# Create an animated 3D scatter plot using Plotly Express
fig = px.scatter_3d(label_counts_ip, x=' Label', y=' Source IP', z='Jumlah',
                    animation_frame=' Timestamp',
                    labels={' Source IP': 'Source IP', ' Label': 'Label', 'Jumlah': 'Count', ' Timestamp': 'Timestamp'},
                    title='Animated 3D Scatter Plot Based on Label, Source IP, and Timestamp',
                    symbol='Jumlah', size='Jumlah')

# Display the animated plot
st.plotly_chart(fig)