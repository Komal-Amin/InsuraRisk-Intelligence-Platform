import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
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

st.markdown("""
<style>

/* Main app */
.stApp {
    background-color: #050505;
    color: #f3f4f6;
}

/* Main container */
.block-container {
    padding-top: 2rem;
    max-width: 1250px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #080808;
    border-right: 1px solid rgba(255,255,255,0.06);
}

section[data-testid="stSidebar"] * {
    color: #d1d5db !important;
    font-weight: 500;
}

/* Headings */
h1 {
    color: #ff69c7 !important;
    font-size: 42px !important;
    font-weight: 800 !important;
    line-height: 1.1;
    letter-spacing: -1px;
}

h2, h3 {
    color: #ffffff !important;
    font-weight: 700 !important;
}

/* Metric cards */
div[data-testid="metric-container"] {
    background: #0c0c0f;
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 18px;
    padding: 22px;
    box-shadow: none;
}

/* Metric labels */
div[data-testid="stMetricLabel"] {
    color: #8b8f98 !important;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-size: 13px !important;
    font-weight: 600 !important;
}

/* Metric values */
div[data-testid="stMetricValue"] {
    color: #ff69c7 !important;
    font-size: 42px !important;
    font-weight: 800 !important;
}

/* Cards */
.custom-card {
    background: #0c0c0f;
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 18px;
    padding: 24px;
    margin-bottom: 18px;
}

/* Dataframes */
div[data-testid="stDataFrame"] {
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.05);
}

/* Plotly charts */
.js-plotly-plot {
    border-radius: 18px;
    overflow: hidden;
}

/* Buttons */
button[kind="primary"] {
    background: #ff69c7 !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
}

/* Divider spacing */
hr {
    border-color: rgba(255,255,255,0.05);
}

/* Hide Streamlit branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title='AI Insurance Intelligence Platform',
    layout='wide',
    initial_sidebar_state="expanded"
)

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

if page == 'Dashboard Home':

    st.title('InsuraRisk Intelligence Platform')

    st.markdown(
        '### Synthetic Data Generation • Fraud Analytics • Statistical Validation • Risk Monitoring'
    )

    try:
        df = pd.read_csv(
            'data/synthetic/ctgan_auto_50k.csv'
        )

        real = pd.read_csv(
            'data/synthetic/baseline_auto.csv'
        )

        ctgan = pd.read_csv(
            'data/synthetic/ctgan_auto_50k.csv'
        )

        tvae = pd.read_csv(
            'data/synthetic/tvae_auto_50k.csv'
        )

        total_claims = df['claim_amount'].sum()
        total_premium = df['premium'].sum()

        loss_ratio = total_claims / total_premium
        fraud_rate = df['fraud_flag'].mean()
        total_policies = len(df)

        ctgan_avg_wasserstein = (
            wasserstein_distance(
                real['premium'],
                ctgan['premium']
            )
            +
            wasserstein_distance(
                real['claim_amount'],
                ctgan['claim_amount']
            )
        ) / 2

        tvae_avg_wasserstein = (
            wasserstein_distance(
                real['premium'],
                tvae['premium']
            )
            +
            wasserstein_distance(
                real['claim_amount'],
                tvae['claim_amount']
            )
        ) / 2

        best_model = (
            'CTGAN'
            if ctgan_avg_wasserstein < tvae_avg_wasserstein
            else 'TVAE'
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            '📄 Total Policies',
            f'{total_policies:,}'
        )

        col2.metric(
            '📉 Loss Ratio',
            f'{loss_ratio:.2%}'
        )

        col3.metric(
            '🛡 Fraud Rate',
            f'{fraud_rate:.2%}'
        )

        col4.metric(
            '🧠 Best Model',
            best_model
        )

        st.subheader('System Status')

        s1, s2, s3, s4 = st.columns(4)

        status_cards = [
            ('✅ Streamlit App Active', s1),
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
            f'{ctgan_avg_wasserstein:.2f}'
        )

        col6.metric(
            'TVAE Avg Wasserstein',
            f'{tvae_avg_wasserstein:.2f}'
        )

    except Exception as e:
        st.error(
            f'Dashboard Home error: {e}'
        )
elif page == 'Monte Carlo Simulation':

    st.title('Monte Carlo Simulation')
    st.caption('All monetary values are shown in Pakistani Rupees (PKR).')

    try:

        df = pd.read_csv(
            'data/synthetic/ctgan_auto_50k.csv'
        )

        simulated_losses = np.random.normal(
            loc=df['claim_amount'].mean(),
            scale=df['claim_amount'].std(),
            size=10000
        )

        simulated_losses = np.abs(simulated_losses)

        mean_loss = simulated_losses.mean()
        p95_loss = np.percentile(simulated_losses, 95)
        p99_loss = np.percentile(simulated_losses, 99)

        col1, col2, col3 = st.columns(3)

        col1.metric(
            'Mean Loss',
            f"{mean_loss:,.2f}"
        )

        col2.metric(
            'P95 Loss',
            f"{p95_loss:,.2f}"
        )

        col3.metric(
            'P99 CAT Loss',
            f"{p99_loss:,.2f}"
        )

        st.markdown(
            """
            <div style="
                background: #111116;
                border: 1px solid rgba(236,72,153,0.25);
                border-radius: 14px;
                padding: 18px 22px;
                margin-bottom: 20px;
                color: #d1d5db;
                font-weight: 600;
                box-shadow: 0 10px 30px rgba(0,0,0,0.35);
            ">
                Monte Carlo simulation generated directly from synthetic claims data.
            </div>
            """,
            unsafe_allow_html=True
        )

        fig = px.histogram(
            simulated_losses,
            nbins=50,
            title='Monte Carlo Loss Distribution'
        )

        fig.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(15,23,42,0)',
            plot_bgcolor='rgba(15,23,42,0)',
            font=dict(color='#e5e7eb'),
            title_font=dict(color='#ffffff', size=22)
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    except Exception as e:

        st.error(
            f'Monte Carlo error: {e}'
        )
elif page == 'Fraud Detection':

    st.title('Fraud Detection Dashboard')

    try:

        df = pd.read_csv(
            'data/synthetic/ctgan_auto_50k.csv'
        )

        fraud_df = df[
            df['fraud_flag'] == 1
        ].copy()

        fraud_cases = len(fraud_df)
        total_records = len(df)
        fraud_rate = fraud_cases / total_records

        col1, col2, col3 = st.columns(3)

        col1.metric(
            'Fraud Cases',
            fraud_cases
        )

        col2.metric(
            'Total Records',
            total_records
        )

        col3.metric(
            'Fraud Rate',
            f"{fraud_rate:.2%}"
        )

        st.markdown(
            """
            <div style="
                background: #111116;
                border: 1px solid rgba(236,72,153,0.25);
                border-radius: 14px;
                padding: 18px 22px;
                margin-bottom: 20px;
                color: #d1d5db;
                font-weight: 600;
                box-shadow: 0 10px 30px rgba(0,0,0,0.35);
            ">
                Fraud analysis generated directly from synthetic dataset.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.subheader(
            'Top Fraud Records'
        )

        display_columns = [
            col for col in [
                'policy_id',
                'premium',
                'claim_amount',
                'region',
                'customer_age'
            ]
            if col in fraud_df.columns
        ]

        ai_table(
            fraud_df[
                display_columns
            ].head(20)
        )

    except Exception as e:

        st.error(
            f'Fraud dashboard error: {e}'
        )
elif page == 'Geographic Heatmap':

    st.title('Geographic Risk Heatmap')

    try:

        df = pd.read_csv(
            'data/synthetic/ctgan_auto_50k.csv'
        )

        geo_df = df.groupby(
            'region'
        ).agg(
            average_claim_amount=('claim_amount', 'mean'),
            fraud_rate=('fraud_flag', 'mean'),
            total_policies=('policy_id', 'count')
        ).reset_index()

        st.markdown(
            """
            <div style="
                background: #111116;
                border: 1px solid rgba(236,72,153,0.25);
                border-radius: 14px;
                padding: 18px 22px;
                margin-bottom: 20px;
                color: #d1d5db;
                font-weight: 600;
                box-shadow: 0 10px 30px rgba(0,0,0,0.35);
            ">
                Geographic risk summary generated directly from synthetic dataset.
            </div>
            """,
            unsafe_allow_html=True
        )

        geo_df['average_claim_amount'] = geo_df[
            'average_claim_amount'
        ].apply(
            lambda x: f"PKR {x:,.2f}"
        )
        
        geo_df['fraud_rate'] = (
            geo_df['fraud_rate'] * 100
        ).apply(
            lambda x: f"{x:.2f}%"
        )
        
        geo_df['total_policies'] = geo_df[
            'total_policies'
        ].apply(
            lambda x: f"{x:,}"
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
            background: #111116;
            border: 1px solid rgba(236,72,153,0.25);
            border-radius: 14px;
            padding: 18px 22px;
            margin-bottom: 20px;
            color: #d1d5db;
            font-weight: 600;
            box-shadow: 0 10px 30px rgba(0,0,0,0.35);
        ">
            KPI metrics calculated directly from synthetic dataset.
        </div>
        """,
        unsafe_allow_html=True
    )

    try:

        df = pd.read_csv(
            'data/synthetic/ctgan_auto_50k.csv'
        )

        total_premium = df['premium'].sum()
        total_claims = df['claim_amount'].sum()

        loss_ratio = total_claims / total_premium
        fraud_rate = df['fraud_flag'].mean()
        combined_ratio = loss_ratio + 0.0009
        risk_score = (
            df['claim_amount'].mean() /
            df['premium'].mean()
        ) * 100

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            'Loss Ratio',
            f"{loss_ratio:.2%}"
        )

        col2.metric(
            'Fraud Rate',
            f"{fraud_rate:.2%}"
        )

        col3.metric(
            'Risk Score',
            f"{risk_score:.2f}"
        )

        col4.metric(
            'Combined Ratio',
            f"{combined_ratio:.2%}"
        )

        st.subheader(
            'Average Claim Amount by Region'
        )

        summary = df.groupby(
            'region'
        )['claim_amount'].mean().reset_index()

        fig = px.line(
            summary,
            x='region',
            y='claim_amount',
            markers=True
        )

        fig.update_layout(
            title='',
            template='plotly_dark',
            paper_bgcolor='rgba(15,23,42,0.0)',
            plot_bgcolor='rgba(15,23,42,0.0)',
            font=dict(color='#e5e7eb'),
            title_font=dict(
                color='#ffffff',
                size=22
            ),
            yaxis_tickprefix='PKR ',
            yaxis_tickformat=',.0f',
            legend=dict(
                bgcolor='rgba(0,0,0,0)',
                font=dict(color='#e5e7eb')
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    except Exception as e:

        st.error(
            f'Risk KPI error: {e}'
        )
elif page == 'Data Explorer':

    st.title('Data Explorer')

    try:

        df = pd.read_csv(
            'data/synthetic/ctgan_auto_50k.csv'
        )

        rows = len(df)
        columns = len(df.columns)

        col1, col2 = st.columns(2)

        col1.metric('Rows', f'{rows:,}')
        col2.metric('Columns', columns)

        st.markdown(
            """
            <div style="
                background: #111116;
                border: 1px solid rgba(236,72,153,0.25);
                border-radius: 14px;
                padding: 18px 22px;
                margin-bottom: 20px;
                color: #d1d5db;
                font-weight: 600;
                box-shadow: 0 10px 30px rgba(0,0,0,0.35);
            ">
                Data preview loaded directly from synthetic dataset. Monetary values are shown in PKR.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.subheader('Dataset Preview')

        preview_df = df.head(20).copy()

        if 'premium' in preview_df.columns:

            preview_df['premium'] = preview_df[
                'premium'
            ].apply(
                lambda x: f"PKR {x:,.2f}"
            )

        if 'claim_amount' in preview_df.columns:

            preview_df['claim_amount'] = preview_df[
                'claim_amount'
            ].apply(
                lambda x: f"PKR {x:,.2f}"
            )

        ai_table(preview_df)

    except Exception as e:

        st.error(
            f'Data Explorer error: {e}'
        )
elif page == 'Real vs Synthetic Comparison':

    st.title('Real vs Synthetic Data Comparison')

    try:

        real_df = pd.read_csv(
            'data/synthetic/baseline_auto.csv'
        )

        ctgan_df = pd.read_csv(
            'data/synthetic/ctgan_auto_50k.csv'
        )

        tvae_df = pd.read_csv(
            'data/synthetic/tvae_auto_50k.csv'
        )

        comparison_results = []

        numeric_columns = [
            'premium',
            'claim_amount'
        ]

        for column in numeric_columns:

            ctgan_ks = ks_2samp(
                real_df[column],
                ctgan_df[column]
            )

            tvae_ks = ks_2samp(
                real_df[column],
                tvae_df[column]
            )

            ctgan_wasserstein = wasserstein_distance(
                real_df[column],
                ctgan_df[column]
            )

            tvae_wasserstein = wasserstein_distance(
                real_df[column],
                tvae_df[column]
            )

            comparison_results.append({
                'column': column,
                'ctgan_ks_pvalue': ctgan_ks.pvalue,
                'ctgan_mean': ctgan_df[column].mean(),
                'ctgan_wasserstein': ctgan_wasserstein,
                'real_mean': real_df[column].mean(),
                'tvae_ks_pvalue': tvae_ks.pvalue,
                'tvae_mean': tvae_df[column].mean(),
                'tvae_wasserstein': tvae_wasserstein
            })

        comparison_df = pd.DataFrame(
            comparison_results
        )

        ctgan_avg_wasserstein = comparison_df[
            'ctgan_wasserstein'
        ].mean()

        tvae_avg_wasserstein = comparison_df[
            'tvae_wasserstein'
        ].mean()

        best_model = (
            'CTGAN'
            if ctgan_avg_wasserstein < tvae_avg_wasserstein
            else 'TVAE'
        )

        st.markdown(
            f"""
            <div style="
                background: #111116;
                border: 1px solid rgba(236,72,153,0.25);
                border-radius: 14px;
                padding: 18px 22px;
                margin-bottom: 20px;
                color: #d1d5db;
                font-weight: 600;
                box-shadow: 0 10px 30px rgba(0,0,0,0.35);
            ">
                Best Performing Synthetic Model: {best_model}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.subheader('Statistical Comparison Table')

        formatted_comparison_df = comparison_df.copy()

        formatted_comparison_df['ctgan_ks_pvalue'] = formatted_comparison_df[
            'ctgan_ks_pvalue'
        ].map('{:.4e}'.format)

        formatted_comparison_df['tvae_ks_pvalue'] = formatted_comparison_df[
            'tvae_ks_pvalue'
        ].map('{:.4e}'.format)

        formatted_comparison_df['ctgan_wasserstein'] = formatted_comparison_df[
            'ctgan_wasserstein'
        ].map('{:.2f}'.format)

        formatted_comparison_df['tvae_wasserstein'] = formatted_comparison_df[
            'tvae_wasserstein'
        ].map('{:.2f}'.format)

        formatted_comparison_df['real_mean'] = formatted_comparison_df[
            'real_mean'
        ].map('{:.2f}'.format)

        formatted_comparison_df['ctgan_mean'] = formatted_comparison_df[
            'ctgan_mean'
        ].map('{:.2f}'.format)

        formatted_comparison_df['tvae_mean'] = formatted_comparison_df[
            'tvae_mean'
        ].map('{:.2f}'.format)

        ai_table(formatted_comparison_df)

        csv = comparison_df.to_csv(
            index=False
        ).encode('utf-8')

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

        col1, col2 = st.columns(2)

        col1.metric(
            'CTGAN Avg Wasserstein',
            f"{ctgan_avg_wasserstein:.2f}"
        )

        col2.metric(
            'TVAE Avg Wasserstein',
            f"{tvae_avg_wasserstein:.2f}"
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

            uploaded_df = pd.read_csv(
                uploaded_file
            )

            MAX_ROWS = 100000

            if len(uploaded_df) > MAX_ROWS:

                st.warning(
                    f'Uploaded file has {len(uploaded_df):,} rows. Using first {MAX_ROWS:,} rows for faster analysis.'
                )

                uploaded_df = uploaded_df.head(
                    MAX_ROWS
                )

            synthetic_df = pd.read_csv(
                'data/synthetic/ctgan_auto_50k.csv'
            )

            st.markdown(
                """
                <div style="
                    background: #111116;
                    border: 1px solid rgba(236,72,153,0.25);
                    border-radius: 14px;
                    padding: 18px 22px;
                    margin-bottom: 20px;
                    color: #d1d5db;
                    font-weight: 600;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.35);
                ">
                    Uploaded dataset loaded successfully.
                </div>
                """,
                unsafe_allow_html=True
            )

            st.subheader(
                'Uploaded Data Preview'
            )

            ai_table(
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
                    comparison
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

                    st.success(
                        'Uploaded data is reasonably similar to the synthetic dataset.'
                    )

                else:

                    st.warning(
                        'Uploaded data shows noticeable differences from the synthetic dataset.'
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

                    fig3.update_layout(
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
                        f"Only one insurance type found: {uploaded_insurance['insurance_type'].iloc[0]}"
                    )

        except Exception as e:

            st.error(
                f'Upload comparison error: {e}'
            )