import streamlit as st
import requests
import plotly.express as px
import pandas as pd
from scipy.stats import ks_2samp, wasserstein_distance

def ai_table(df):

    import plotly.graph_objects as go

    table = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=list(df.columns),
                    fill_color='#0f172a',
                    font=dict(color='#38bdf8', size=15),
                    align='left',
                    height=38
                ),
                cells=dict(
                    values=[df[col] for col in df.columns],
                    fill_color='#111827',
                    font=dict(color='#e5e7eb', size=14),
                    align='left',
                    height=34
                )
            )
        ]
    )

    table.update_layout(
        paper_bgcolor='rgba(15,23,42,0)',
        plot_bgcolor='rgba(15,23,42,0)',
        font=dict(color='white'),
        margin=dict(l=0, r=0, t=10, b=0)
    )

    st.plotly_chart(
        table,
        use_container_width=True,
        config={
            'displayModeBar': 'hover',
            'displaylogo': False
        }
    )

st.markdown(
    """
    <style>

    .stApp {
    background:

    radial-gradient(
        circle at top left,
        rgba(217,70,239,0.12),
        transparent 30%
    ),

    radial-gradient(
        circle at top right,
        rgba(168,85,247,0.14),
        transparent 26%
    ),

    radial-gradient(
        circle at bottom left,
        rgba(79,70,229,0.14),
        transparent 28%
    ),

    linear-gradient(
        135deg,
        #020617,
        #081028,
        #111c44
    );

    background-attachment: fixed;
    color: #e5e7eb;
}

    section[data-testid="stSidebar"] {
    background:
    linear-gradient(
        180deg,
        rgba(20,11,45,0.95),
        rgba(8,16,40,0.95)
    );

    border-right: 1px solid rgba(217,70,239,0.22);
}

section[data-testid="stSidebar"] * {
    color: #e9d5ff !important;
    opacity: 1 !important;
    font-weight: 600;
}

    h1 {
    font-size: 30px !important;
    font-weight: 800 !important;
    letter-spacing: -1px;
    color: #e9d5ff !important;
    text-shadow: 0 0 18px rgba(192,132,252,0.18);
}
    h2, h3 {
    color: #f0abfc !important;
    letter-spacing: -0.5px;
    text-shadow: 0 0 12px rgba(217,70,239,0.14);
}

    div[data-testid="metric-container"] {
        background: rgba(255,255,255,0.04);
        backdrop-filter: blur(14px);
        border: 1px solid rgba(217,70,239,0.35);
        padding: 22px;
        border-radius: 18px;
        box-shadow: 0 12px 30px rgba(0,0,0,0.35);
    }

    div[data-testid="metric-container"] {
        transition: all 0.25s ease;
    }

    div[data-testid="metric-container"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 30px rgba(217,70,239,0.25);
}

    div[data-testid="stMetricValue"] {
        color: #c084fc !important;
        font-size: 42px !important;
        font-weight: 800 !important;
    }

    div[data-testid="stMetricLabel"] {
    color: #f9a8d4 !important;
    font-size: 18px !important;
    font-weight: 600 !important;
    letter-spacing: -0.3px;
    opacity: 0.95 !important;
}

    div[data-testid="stAlert"] {
        border-radius: 16px !important;
        border: 1px solid rgba(217,70,239,0.35) !important;
        background: rgba(22,101,52,0.22) !important;
    }

    div[data-testid="stAlert"] * {
        color: #dcfce7 !important;
        opacity: 1 !important;
    }

    div[data-testid="stDataFrame"] {
        background: rgba(15,23,42,0.92) !important;
        border: 1px solid rgba(56,189,248,0.20);
        border-radius: 14px;
        padding: 10px;
    }

    div[data-baseweb="select"] > div {
        background-color: #0f172a !important;
        color: #ffffff !important;
        border: 1px solid rgba(56,189,248,0.35);
        border-radius: 10px;
    }

    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
    }
/* Hide Streamlit top header bar */
header[data-testid="stHeader"] {
    background: transparent !important;
}

/* Make sidebar dropdown menu readable */
div[data-baseweb="popover"] {
    background-color: #0f172a !important;
}

div[data-baseweb="menu"] {
    background-color: #0f172a !important;
}

div[role="option"] {
    background-color: #0f172a !important;
    color: #f8fafc !important;
}

div[role="option"]:hover {
    background-color: #1e293b !important;
    color: #d946ef !important;
}

/* Download button styling */
.stDownloadButton button {
    background: linear-gradient(135deg, #0284c7, #38bdf8) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.7rem 1.2rem !important;
    font-weight: 800 !important;
}

/* Hide Plotly toolbar unless hover */
.modebar {
    opacity: 0 !important;
    transition: opacity 0.2s ease-in-out;
}

.js-plotly-plot:hover .modebar {
    opacity: 1 !important;
}
/* Fix dropdown menu readability */
div[data-baseweb="popover"] {
    background-color: #0f172a !important;
}

div[data-baseweb="menu"] {
    background-color: #0f172a !important;
    border: 1px solid rgba(56,189,248,0.35) !important;
}

div[role="listbox"] {
    background-color: #0f172a !important;
}

div[role="option"] {
    background-color: #0f172a !important;
    color: #f8fafc !important;
    font-weight: 700 !important;
}

div[role="option"] * {
    color: #f8fafc !important;
    opacity: 1 !important;
}

div[role="option"]:hover {
    background-color: #1e293b !important;
}

div[role="option"]:hover * {
    color: #38bdf8 !important;
}
/* Force metric labels to peach-pink */
div[data-testid="metric-container"] label,
div[data-testid="metric-container"] p,
div[data-testid="metric-container"] span,
div[data-testid="stMetricLabel"],
div[data-testid="stMetricLabel"] *,
[data-testid="stMetricLabel"] {
    color: #f9a8d4 !important;
    opacity: 1 !important;
    font-size: 18px !important;
    font-weight: 700 !important;
}

    </style>
    """,
    unsafe_allow_html=True
)
st.set_page_config(
    page_title='AI Insurance Intelligence Platform',
    page_icon='⚠️',
    layout='wide'
)

st.sidebar.title('⚠️ AI Insurance Platform')

st.sidebar.markdown(
    '''
    # AI Insurance Platform

    ### Synthetic Risk Intelligence

    ---
    '''
)

page = st.sidebar.radio(
    'Navigation',
    [
        'Dashboard Home',
        'Risk KPIs',
        'Monte Carlo Simulation',
        'Fraud Detection',
        'Geographic Heatmap',
        'Data Explorer',
        'Real vs Synthetic Comparison',
        'Upload Data for Comparison'
    ]
)

API_URL = 'http://localhost:5000'

if page == 'Dashboard Home':

    st.title('AI-Powered Insurance Risk Intelligence Platform')

    st.markdown(
        '### Synthetic Data Generation • Fraud Analytics • Statistical Validation • Risk Monitoring'
    )

    try:
        metrics_response = requests.get(
            f'{API_URL}/api/metrics?dataset=ctgan_auto_50k'
        )

        metrics_data = metrics_response.json()

        comparison_response = requests.get(
            'http://localhost:5000/api/comparison'
        )

        comparison_data = comparison_response.json()
        summary = comparison_data['summary']

        col1, col2, col3, col4 = st.columns(4)

        col1.metric('📄 Total Policies', f"{metrics_data['total_policies']:,}")
        col2.metric('📉 Loss Ratio', f"{metrics_data['loss_ratio']:.2%}")
        col3.metric('🛡 Fraud Rate', f"{metrics_data['fraud_rate']:.2%}")
        col4.metric('🧠 Best Model', summary['best_model'])

        st.subheader('System Status')

        s1, s2, s3, s4 = st.columns(4)

        status_cards = [
            ('✅ Flask API Active', s1),
            ('🛡 Fraud Detection Active', s2),
            ('📂 Upload Validation Enabled', s3),
            ('⚡ Synthetic Comparison Ready', s4)
        ]

        for text, col in status_cards:
            col.markdown(
                f"""
                <div style="
                    background: rgba(217,70,239,0.12);
                    backdrop-filter: blur(14px);
                    border: 1px solid rgba(217,70,239,0.35);
                    padding: 14px;
                    border-radius: 14px;
                    text-align:center;
                    font-weight:700;
                ">
                {text}
                </div>
                """,
                unsafe_allow_html=True
            )

        st.subheader('Platform Capabilities')

        c1, c2 = st.columns(2)

        with c1:
            st.markdown(
                """
                <div style="
                    background: rgba(255,255,255,0.06);
                    backdrop-filter: blur(14px);
                    border: 1px solid rgba(217,70,239,0.28);
                    box-shadow: 0 8px 30px rgba(217,70,239,0.08);
                    padding: 26px;
                    border-radius: 22px;
                    line-height: 1.7;
                ">
                Fraud analytics, risk KPI monitoring, geographic claim analysis,
                and Monte Carlo loss simulation are integrated into one dashboard.
                </div>
                """,
                unsafe_allow_html=True
            )

        with c2:
            st.markdown(
                """
                <div style="
                    background: rgba(255,255,255,0.06);
                    backdrop-filter: blur(14px);
                    border: 1px solid rgba(217,70,239,0.28);
                    box-shadow: 0 8px 30px rgba(217,70,239,0.08);
                    padding: 26px;
                    border-radius: 22px;
                    line-height: 1.7;
                ">
                Users can upload insurance datasets, validate schema,
                compare distributions, and generate similarity results.
                </div>
                """,
                unsafe_allow_html=True
            )

        st.subheader('Model Evaluation Summary')

        col5, col6 = st.columns(2)

        col5.metric(
            'CTGAN Avg Wasserstein',
            f"{summary['ctgan_avg_wasserstein']:.2f}"
        )

        col6.metric(
            'TVAE Avg Wasserstein',
            f"{summary['tvae_avg_wasserstein']:.2f}"
        )

    except Exception as e:
        st.error(f'Dashboard Home error: {e}')
elif page == 'Monte Carlo Simulation':

    st.title('Monte Carlo Simulation')

    try:

        response = requests.get(
            'http://localhost:5000/api/simulation/monte-carlo'
        )

        simulation_data = response.json()

        st.metric(
            'Mean Loss',
            f"{simulation_data['mean']:,.2f}"
        )

        st.metric(
            'P95 Loss',
            f"{simulation_data['p95']:,.2f}"
        )

        st.metric(
            'P99 CAT Loss',
            f"{simulation_data['p99']:,.2f}"
        )

        st.markdown(
    """
    <div style="
        background: rgba(217,70,239,0.10);
        border: 1px solid rgba(217,70,239,0.30);
        backdrop-filter: blur(14px);
        border-radius: 18px;
        padding: 18px;
        margin-bottom: 20px;
        color: #f5d0fe;
        font-weight: 600;
        box-shadow: 0 8px 25px rgba(217,70,239,0.08);
    ">
        Fraud results loaded from Flask API
    </div>
    """,
    unsafe_allow_html=True
)

    except Exception as e:
        st.error(f'Monte Carlo error: {e}')
elif page == 'Fraud Detection':

    st.title('Fraud Detection Dashboard')

    try:
        response = requests.get('http://localhost:5000/api/fraud')
        fraud_data = response.json()

        col1, col2, col3 = st.columns(3)

        col1.metric('Fraud Cases', fraud_data['fraud_cases'])
        col2.metric('Total Records', fraud_data['total_records'])
        col3.metric('Fraud Rate', f"{fraud_data['fraud_rate']:.2%}")

        st.markdown(
    """
    <div style="
        background: rgba(217,70,239,0.10);
        border: 1px solid rgba(217,70,239,0.30);
        backdrop-filter: blur(14px);
        border-radius: 18px;
        padding: 18px;
        margin-bottom: 20px;
        color: #f5d0fe;
        font-weight: 600;
        box-shadow: 0 8px 25px rgba(217,70,239,0.08);
    ">
        Fraud results loaded from Flask API
    </div>
    """,
    unsafe_allow_html=True
)

        fraud_df = pd.DataFrame(fraud_data['top_fraud_records'])

        st.subheader('Top Fraud Records')
        ai_table(fraud_df)

    except Exception as e:
        st.error(f'Fraud dashboard error: {e}')
elif page == 'Geographic Heatmap':

    st.title('Geographic Risk Heatmap')

    try:

        response = requests.get(
            'http://localhost:5000/api/geographic'
        )

        geo_data = response.json()

        geo_df = pd.DataFrame(geo_data)

        st.markdown(
    """
    <div style="
        background: rgba(217,70,239,0.10);
        border: 1px solid rgba(217,70,239,0.30);
        backdrop-filter: blur(14px);
        border-radius: 18px;
        padding: 18px;
        margin-bottom: 20px;
        color: #f5d0fe;
        font-weight: 600;
        box-shadow: 0 8px 25px rgba(217,70,239,0.08);
    ">
        Fraud results loaded from Flask API
    </div>
    """,
    unsafe_allow_html=True
)

        ai_table(geo_df)

        fig = px.bar(
            geo_df,
            x='region',
            y='average_claim_amount',
            title='Average Claim Amount by Region'
        )
        fig.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(15,23,42,0.0)',
            plot_bgcolor='rgba(15,23,42,0.0)',
            font=dict(color='#e5e7eb'),
            title_font=dict(color='#ffffff', size=22),
            legend=dict(
                bgcolor='rgba(0,0,0,0)',
                font=dict(color='#e5e7eb')
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        fig2 = px.bar(
            geo_df,
            x='region',
            y='fraud_rate',
            title='Fraud Rate by Region'
        )
        fig2.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(15,23,42,0.0)',
            plot_bgcolor='rgba(15,23,42,0.0)',
            font=dict(color='#e5e7eb'),
            title_font=dict(color='#ffffff', size=22)
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    except Exception as e:
        st.error(
            f'Geographic dashboard error: {e}'
        )
elif page == 'Risk KPIs':

    st.title('Risk KPI Analysis')
    st.markdown(
    """
    <div style="
        background: rgba(217,70,239,0.10);
        border: 1px solid rgba(217,70,239,0.30);
        backdrop-filter: blur(14px);
        border-radius: 18px;
        padding: 18px;
        margin-bottom: 20px;
        color: #f5d0fe;
        font-weight: 600;
        box-shadow: 0 8px 25px rgba(217,70,239,0.08);
    ">
        Using Flask API endpoint: /api/kpis
    </div>
    """,
    unsafe_allow_html=True
)

    try:
        response = requests.get(
            'http://localhost:5000/api/kpis'
        )

        kpi_data = response.json()

        df = pd.read_csv(
            'data/synthetic/ctgan_auto_50k.csv'
        )

        loss_ratio = kpi_data['loss_ratio']
        combined_ratio = kpi_data['combined_ratio']
        fraud_rate = kpi_data['fraud_rate']
        risk_score = kpi_data['risk_score']

        col1, col2, col3 = st.columns(3)

        col1.metric('Loss Ratio', f"{loss_ratio:.2%}")
        col2.metric('Fraud Rate', f"{fraud_rate:.2%}")
        col3.metric('Risk Score', risk_score)

        st.metric('Combined Ratio', f"{combined_ratio:.2%}")

        st.subheader('Claims by Insurance Type')

        summary = df.groupby(
            'region'
        )['claim_amount'].mean().reset_index()

        fig = px.line(
            summary,
            x='region',
            y='claim_amount',
            markers=True,
            title='Average Claim Amount by Insurance Type'
        )
        fig.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(15,23,42,0.0)',
            plot_bgcolor='rgba(15,23,42,0.0)',
            font=dict(color='#e5e7eb'),
            title_font=dict(color='#ffffff', size=22),
            legend=dict(
                bgcolor='rgba(0,0,0,0)',
                font=dict(color='#e5e7eb')
            )
        )

        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f'Risk KPI error: {e}')
elif page == 'Data Explorer':

    st.title('Data Explorer')

    try:

        response = requests.get(
            'http://localhost:5000/api/data-preview'
        )

        data = response.json()

        col1, col2 = st.columns(2)

        col1.metric('Rows', data['rows'])
        col2.metric('Columns', data['columns'])

        st.markdown(
    """
    <div style="
        background: rgba(217,70,239,0.10);
        border: 1px solid rgba(217,70,239,0.30);
        backdrop-filter: blur(14px);
        border-radius: 18px;
        padding: 18px;
        margin-bottom: 20px;
        color: #f5d0fe;
        font-weight: 600;
        box-shadow: 0 8px 25px rgba(217,70,239,0.08);
    ">
        Data preview loaded from Flask API
    </div>
    """,
    unsafe_allow_html=True
)

        st.subheader('Dataset Preview')

        preview_df = pd.DataFrame(data['preview'])

        ai_table(preview_df.head(20))

    except Exception as e:
        st.error(
            f'Data Explorer error: {e}'
        )
elif page == 'Real vs Synthetic Comparison':

    st.title('Real vs Synthetic Data Comparison')

    try:
        response = requests.get(
            'http://localhost:5000/api/comparison'
        )

        comparison_data = response.json()

        comparison_df = pd.DataFrame(
            comparison_data['results']
        )

        summary = comparison_data['summary']

        st.markdown(
            """
            <div style="
                background: rgba(217,70,239,0.10);
                border: 1px solid rgba(217,70,239,0.30);
                backdrop-filter: blur(14px);
                border-radius: 18px;
                padding: 18px;
                margin-bottom: 20px;
                color: #f5d0fe;
                font-weight: 600;
                box-shadow: 0 8px 25px rgba(217,70,239,0.08);
            ">
                Comparison data loaded from Flask API
            </div>
            """,
            unsafe_allow_html=True
        )

        st.subheader('Statistical Comparison Table')

        formatted_comparison_df = comparison_df.copy()

        formatted_comparison_df['ctgan_ks_pvalue'] = formatted_comparison_df['ctgan_ks_pvalue'].map('{:.4e}'.format)
        formatted_comparison_df['tvae_ks_pvalue'] = formatted_comparison_df['tvae_ks_pvalue'].map('{:.4e}'.format)
        formatted_comparison_df['ctgan_wasserstein'] = formatted_comparison_df['ctgan_wasserstein'].map('{:.2f}'.format)
        formatted_comparison_df['tvae_wasserstein'] = formatted_comparison_df['tvae_wasserstein'].map('{:.2f}'.format)
        formatted_comparison_df['real_mean'] = formatted_comparison_df['real_mean'].map('{:.2f}'.format)
        formatted_comparison_df['ctgan_mean'] = formatted_comparison_df['ctgan_mean'].map('{:.2f}'.format)
        formatted_comparison_df['tvae_mean'] = formatted_comparison_df['tvae_mean'].map('{:.2f}'.format)

        ai_table(formatted_comparison_df)

        csv = comparison_df.to_csv(index=False).encode('utf-8')

        st.download_button(
            label='Download Comparison Results CSV',
            data=csv,
            file_name='real_vs_synthetic_comparison.csv',
            mime='text/csv'
        )

        st.subheader('Mean Comparison')

        mean_df = pd.melt(
            comparison_df,
            id_vars=['column'],
            value_vars=[
                'real_mean',
                'ctgan_mean',
                'tvae_mean'
            ],
            var_name='Dataset',
            value_name='Mean'
        )

        fig = px.bar(
            mean_df,
            x='column',
            y='Mean',
            color='Dataset',
            barmode='group',
            title='Real vs Synthetic Mean Comparison'
        )

        fig.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(15,23,42,0)',
            plot_bgcolor='rgba(15,23,42,0)',
            font=dict(color='#e5e7eb'),
            title_font=dict(color='#ffffff', size=22),
            legend=dict(
                bgcolor='rgba(0,0,0,0)',
                font=dict(color='#e5e7eb')
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.subheader('Wasserstein Distance')

        wasserstein_df = pd.melt(
            comparison_df,
            id_vars=['column'],
            value_vars=[
                'ctgan_wasserstein',
                'tvae_wasserstein'
            ],
            var_name='Model',
            value_name='Distance'
        )

        fig2 = px.bar(
            wasserstein_df,
            x='column',
            y='Distance',
            color='Model',
            barmode='group',
            title='Model Distance Comparison'
        )

        fig2.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(15,23,42,0)',
            plot_bgcolor='rgba(15,23,42,0)',
            font=dict(color='#e5e7eb'),
            title_font=dict(color='#ffffff', size=22),
            legend=dict(
                bgcolor='rgba(0,0,0,0)',
                font=dict(color='#e5e7eb')
            )
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

        st.markdown(
            f"""
            <div style="
                background: rgba(217,70,239,0.10);
                border: 1px solid rgba(217,70,239,0.30);
                backdrop-filter: blur(14px);
                border-radius: 18px;
                padding: 18px;
                margin-bottom: 20px;
                color: #f5d0fe;
                font-weight: 600;
                box-shadow: 0 8px 25px rgba(217,70,239,0.08);
            ">
                Best Performing Synthetic Model: {summary['best_model']}
            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        col1.metric(
            'CTGAN Avg Wasserstein',
            f"{summary['ctgan_avg_wasserstein']:.2f}"
        )

        col2.metric(
            'TVAE Avg Wasserstein',
            f"{summary['tvae_avg_wasserstein']:.2f}"
        )

        st.info(
            'Lower Wasserstein distance and closer mean values indicate better similarity to real/reference data.'
        )

    except Exception as e:
        st.error(
            f'Comparison dashboard error: {e}'
        )
elif page == 'Upload Data for Comparison':

    st.title('Upload Data for Comparison')

    uploaded_file = st.file_uploader(
        'Upload a CSV file',
        type=['csv']
    )

    if uploaded_file is not None:

        try:

            uploaded_df = pd.read_csv(uploaded_file)
            MAX_ROWS = 100000

            if len(uploaded_df) > MAX_ROWS:
    
                st.warning(
                    f'Uploaded file has {len(uploaded_df):,} rows. Using first {MAX_ROWS:,} rows for faster analysis.'
                )

                uploaded_df = uploaded_df.head(MAX_ROWS)
            synthetic_df = pd.read_csv(
                'data/synthetic/ctgan_auto_50k.csv'
            )

            st.markdown(
    """
    <div style="
        background: rgba(217,70,239,0.10);
        border: 1px solid rgba(217,70,239,0.30);
        backdrop-filter: blur(14px);
        border-radius: 18px;
        padding: 18px;
        margin-bottom: 20px;
        color: #f5d0fe;
        font-weight: 600;
        box-shadow: 0 8px 25px rgba(217,70,239,0.08);
    ">
        Fraud results loaded from Flask API
    </div>
    """,
    unsafe_allow_html=True
)

            st.subheader(
                'Uploaded Data Preview'
            )

            st.dataframe(
                uploaded_df.head(20)
            )

            required_cols = [
                'policy_id',
                'premium',
                'claim_amount',
                'fraud_flag',
                'region',
                'insurance_type'
            ]

            missing_cols = [
                col for col in required_cols
                if col not in uploaded_df.columns
            ]

            if missing_cols:

                st.error(
                    f'Missing required columns: {missing_cols}'
                )

            else:

                uploaded_fraud_rate = uploaded_df[
                    'fraud_flag'
                ].mean()

                synthetic_fraud_rate = synthetic_df[
                    'fraud_flag'
                ].mean()

                comparison = pd.DataFrame({

                    'Metric': [
                        'Average Premium',
                        'Average Claim Amount',
                        'Fraud Rate'
                    ],

                    'Uploaded Data': [
                        uploaded_df['premium'].mean(),
                        uploaded_df['claim_amount'].mean(),
                        uploaded_fraud_rate
                    ],

                    'Synthetic Data': [
                        synthetic_df['premium'].mean(),
                        synthetic_df['claim_amount'].mean(),
                        synthetic_fraud_rate
                    ]
                })

                st.subheader(
                    'Uploaded vs Synthetic Comparison'
                )

                ai_table(
                    comparison,
                    'Uploaded vs Synthetic Comparison'
                )

                fig = px.bar(
                    comparison,
                    x='Metric',
                    y=[
                        'Uploaded Data',
                        'Synthetic Data'
                    ],
                    barmode='group',
                    title='Uploaded vs Synthetic Data'
                )
                fig.update_layout(
                    template='plotly_dark',
                    paper_bgcolor='rgba(15,23,42,0.0)',
                    plot_bgcolor='rgba(15,23,42,0.0)',
                    font=dict(color='#e5e7eb'),
                    title_font=dict(color='#ffffff', size=22),
                    legend=dict(
                        bgcolor='rgba(0,0,0,0)',
                        font=dict(color='#e5e7eb')
                    )
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

                stat_results = []

                for col in [
                    'premium',
                    'claim_amount'
                ]:

                    ks_result = ks_2samp(
                        uploaded_df[col],
                        synthetic_df[col]
                    )

                    wasserstein = wasserstein_distance(
                        uploaded_df[col],
                        synthetic_df[col]
                    )

                    stat_results.append({
                        'Column': col,
                        'KS-Test P-Value': ks_result.pvalue,
                        'Wasserstein Distance': wasserstein
                    })

                stat_df = pd.DataFrame(
                    stat_results
                )

                st.subheader(
                    'Statistical Similarity Tests'
                )

                ai_table(
                    stat_df
                )

                avg_distance = stat_df[
                    'Wasserstein Distance'
                ].mean()

                st.metric(
                    'Average Wasserstein Distance',
                    f'{avg_distance:.2f}'
                )

                if avg_distance < 3000:

                    st.markdown(
    """
    <div style="
        background: rgba(217,70,239,0.10);
        border: 1px solid rgba(217,70,239,0.30);
        backdrop-filter: blur(14px);
        border-radius: 18px;
        padding: 18px;
        margin-bottom: 20px;
        color: #f5d0fe;
        font-weight: 600;
        box-shadow: 0 8px 25px rgba(217,70,239,0.08);
    ">
        Fraud results loaded from Flask API
    </div>
    """,
    unsafe_allow_html=True
)    

                else:

                    st.warning(
                        'Verdict: Uploaded data shows noticeable differences from the synthetic dataset.'
                    )

                csv_results = stat_df.to_csv(
                    index=False
                ).encode('utf-8')

                st.download_button(
                    label='Download Upload Comparison Test Results',
                    data=csv_results,
                    file_name='uploaded_vs_synthetic_tests.csv',
                    mime='text/csv'
                )

                st.subheader(
                    'Region Distribution'
                )

                uploaded_region = uploaded_df[
                    'region'
                ].value_counts().reset_index()

                uploaded_region.columns = [
                    'region',
                    'count'
                ]

                fig2 = px.pie(
                    uploaded_region,
                    names='region',
                    values='count',
                    title='Uploaded Dataset Region Distribution'
                )
                fig2.update_layout(
                    template='plotly_dark',
                    paper_bgcolor='rgba(15,23,42,0.0)',
                    plot_bgcolor='rgba(15,23,42,0.0)',
                    font=dict(color='#e5e7eb'),
                    title_font=dict(color='#ffffff', size=22)
                )
            
                st.plotly_chart(
                    fig2,
                    use_container_width=True
                )

                st.subheader(
                    'Insurance Type Distribution'
                )
                
                uploaded_insurance = uploaded_df[
                    'insurance_type'
                ].value_counts().reset_index()

                uploaded_insurance.columns = [
                    'insurance_type',
                    'count'
                ]
            if len(uploaded_insurance) > 1:
                
                fig3 = px.bar(
                     uploaded_insurance,
                     x='insurance_type',
                     y='count',
                     title='Insurance Type Distribution'
                )
                fig.update_layout(
                    template='plotly_dark',
                    paper_bgcolor='rgba(15,23,42,0)',
                    plot_bgcolor='rgba(15,23,42,0)',
                    font=dict(color='#e5e7eb'),
                    title_font=dict(color='#ffffff', size=22),
                    legend=dict(
                        bgcolor='rgba(0,0,0,0)',
                        font=dict(color='#e5e7eb')
                    )
                )

                st.plotly_chart(
                    fig3,
                    use_container_width=True
                )
                
            else:
            
                st.info(
                    f"Only one insurance type found: {uploaded_insurance['insurance_type'].iloc[0]}. Chart skipped because there is no category comparison."
                )
                                
                st.markdown(
    """
    <div style="
        background: rgba(217,70,239,0.10);
        border: 1px solid rgba(217,70,239,0.30);
        backdrop-filter: blur(14px);
        border-radius: 18px;
        padding: 18px;
        margin-bottom: 20px;
        color: #f5d0fe;
        font-weight: 600;
        box-shadow: 0 8px 25px rgba(217,70,239,0.08);
    ">
        Fraud results loaded from Flask API
    </div>
    """,
    unsafe_allow_html=True
)

        except Exception as e:

            st.error(
                f'Upload comparison error: {e}'
            )