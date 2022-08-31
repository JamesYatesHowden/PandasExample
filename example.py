import pandas as pd


def example():
    inputs = pd.read_csv('inputs.csv')
    stats = inputs.describe(percentiles=[0.05, 0.9]) 
    print(f'\n\n {stats} \n\n')
    stats.to_csv('stats.csv')


if __name__ == "__main__":
    example()