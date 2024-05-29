from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

def convert_data(pop):
    if 'M' in str(pop):
        return float(pop[:-1]) * 1e6
    elif 'K' in str(pop):
        return float(pop[:-1]) * 1e3
    else:
        return pop
    
def millions_formatter(x, pos):
    return f"{int(x/1e6)}M"

def main():
    try:
        income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_expectancy = load("life_expectancy_years.csv")
        if income.empty or life_expectancy.empty:
            raise AssertionError("No data provided")
        income_1900 = income['1900'].astype(float)
        life_expectancy_1900 = life_expectancy['1900'].astype(float)

        merged_df = pd.merge(income_1900, life_expectancy_1900, left_index=True, right_index=True)
        print("merged :",merged_df)

        plt.scatter(merged_df['1900_x'], merged_df['1900_y'])
        plt.title("1900")
        plt.ylabel("Life Expectancy")
        plt.xlabel("Gross domestic product")
        plt.xscale('log')
        plt.xticks(ticks=[300, 1000, 10000], labels=[300, '1k', '10k'])
        plt.show()
    except AssertionError as e:
        print(e)
        return
    return None

main()