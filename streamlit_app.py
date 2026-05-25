import streamlit as st
import requests
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title='AI Insurance Intelligence Platform',
    page_icon='⚠️',
    layout='wide')

st.sidebar.title('⚠️ AI Insurance Platform')

page = st.sidebar.selectbox('Navigate to:', [
    'Dashboard Home',
    'Risk KPIs',
    'Monte Carlo Simulation',
    'Fraud Detection',
    'Geographic Heatmap',
    'Data Explorer'])

API_URL = 'http://localhost:5000'

if page == 'Dashboard Home':
    st.title('AI Insurance Intelligence Platform')
    st.subheader("Pakistan's First AI-Powered Insurance Risk Dashboard")

    try:
        response = requests.get(f'{API_URL}/api/metrics?dataset=ctgan_auto_50k')
        data = response.json()

        col1, col2, col3 = st.columns(3)

        col1.metric(
            'Loss Ratio',
            f"{data['loss_ratio']:.2%}",
            help='Claims / Premiums. Below 60% is healthy.')

        col2.metric(
            'Fraud Rate',
            f"{data['fraud_rate']:.2%}",
            help='Percent of policies flagged as suspicious.)

        col3.metric(
            'Total Policies',
            f"{data['total_policies']:,}",
            help='Total synthetic policy records.)

    except Exception as e:
        st.error(f'Could not connect to API: {e}. Make sure api/app.py is running.')


 