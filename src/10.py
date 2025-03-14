
import pandas as pd

def get_data(url):
    df = pd.read_csv(url)
    return df

