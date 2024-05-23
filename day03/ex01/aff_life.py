from load_csv import load
import matplotlib.pyplot as plt

def main():
    try:
        df = load("life_expectancy_years.csv")
        if df.empty:
            raise AssertionError("No data provided")
        france = df.loc[df['country'] == 'France']
        year = france.iloc[:, 1:]
        year = year.transpose()
        year.index = year.index.astype(int)

        ax = year.plot.line()
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')
        plt.title('France Life expectancy Projections')
        plt.xticks(range(min(year.index), max (year.index) + 1, 40))
        ax.legend().remove()
        plt.show()

    except AssertionError as e:
        print(e)
        return
    return None

main()