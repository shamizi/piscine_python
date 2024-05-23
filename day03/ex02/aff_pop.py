from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

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
        df = load("population_total.csv")
        if df.empty:
            raise AssertionError("No data provided")
        france = df[df['country'] == 'France'].iloc[:, 1:]
        belgique = df[df['country'] == 'Belgium'].iloc[:, 1:]

        # Transposer les données pour les deux pays
        france_data = france.transpose()
        france_data.index = france_data.index.astype(int)
        
        belgique_data = belgique.transpose()
        belgique_data.index = belgique_data.index.astype(int)

        # Convertir les données de population
        france_data_converted = france_data.map(convert_data)
        belgique_data_converted = belgique_data.map(convert_data)

        france_data_filtered = france_data_converted.loc[(france_data_converted.index >= 1800) & (france_data_converted.index <= 2050)]
        belgique_data_filtered = belgique_data_converted.loc[(belgique_data_converted.index >= 1800) & (belgique_data_converted.index <= 2050)]
        
        ax1 = plt.gca()
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(millions_formatter))
        ax1.yaxis.set_major_locator(ticker.MultipleLocator(20e6))
        ax1.xaxis.set_major_locator(ticker.MultipleLocator(40))
        ax1.set_xlim(1770, 2070)
     
        plt.plot(france_data_filtered.index, france_data_filtered.values.flatten(), label='France', color='green')
        plt.plot(belgique_data_filtered.index, belgique_data_filtered.values.flatten(), label='Belgium', color='blue')
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.title("Population Projections")
        plt.legend(loc='lower right')
        
        plt.show()
    
    
    except AssertionError as e:
        print(e)
        return
    return None

main()