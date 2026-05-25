from api.utils.data_loader import load_dataset


def generate_data_preview():

    df = load_dataset()

    return {
        'rows': int(len(df)),
        'columns': int(len(df.columns)),
        'column_names': list(df.columns),
        'preview': df.head(100).to_dict(orient='records')
    }