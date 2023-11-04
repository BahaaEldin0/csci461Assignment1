import pandas as pd
import eda

def transform(df):
    df = df.dropna()
    date_formats = ["%d-%m-%Y", "%d/%m/%Y"]

    df['parsed_date'] = None

    for date_format in date_formats:
        parsed_dates = pd.to_datetime(df['date'], format=date_format, errors='coerce')
        df['parsed_date'] = df['parsed_date'].combine_first(parsed_dates)

    df = df.dropna(subset=['parsed_date'])
    df['date'] = df['parsed_date']
    df.drop(columns=['parsed_date'], inplace=True)

    try:
        df['time_of_sale'] = pd.to_datetime(df['time_of_sale'], errors='coerce')
    except pd._libs.tslibs.parsing.DateParseError as e:
        print(f"Error parsing 'time_of_sale' column: {e}")

    df['total_amount'] = df['item_price'] * df['quantity']
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month

    df = df.sample(frac=0.5)

    df['total_amount_category'] = pd.cut(df['total_amount'], bins=[0,500,1000,float('inf')], labels=['Low', 'Medium', 'High'])
    df['quantity_category'] = pd.cut(df['quantity'], bins=[0,5,float('inf')], labels=['Low', 'High'])

    df.to_csv('res_dpre.csv', index=False)
    eda.analyze(df)
