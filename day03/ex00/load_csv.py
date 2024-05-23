import pandas as pd
import os

def load(path: str) -> pd.DataFrame:
    #path qui n'existe pas
    #pas csv
    try:
        if not os.path.exists(path):
            raise AssertionError("File doesn't exist")
        if not path.endswith('.csv'):
            raise AssertionError("Not a csv file")
        df = pd.read_csv(path)
        print("Loading dataset of dimensions", df.shape)
        return df
    except AssertionError as e:
        print(e)
        return None

def main():
    print(load('population_total.csv'))

main()