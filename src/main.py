# some testing stuff
import csv
import argparse
import matplotlib as plt
import pandas as pd

def get_args():
    # create a parser
    parser = argparse.ArgumentParser()
    # add the argument to take csv input
    parser.add_argument('confirmed_csv')
    parser.add_argument('deaths_csv')
    parser.add_argument('recovered_csv')
    # parse the input
    args = parser.parse_args()

    return args

def preprocess(dataframe):
    # takes a dataframe, preprocesses
    return dataframe

def get_country(dataframe,country,column='Country/Region',drop=['Country/Region','Lat','Long']):
    # get specific country from dataframe
    df_temp = dataframe.loc[dataframe[column] == country].T
    df_temp = df_temp.drop(drop)
    df_temp.columns = df_temp.iloc[0]
    df_temp = df_temp.drop(df_temp.index[0])
    return df_temp


def main():
    
    # take user args
    args = get_args()

    # get arguments
    confirmed = args.confirmed_csv
    deaths = args.deaths_csv
    recovered = args.recovered_csv

    # read the csvs into pandas dataframes
    confirmed_df = pd.read_csv(confirmed)
    deaths_df = pd.read_csv(deaths)
    recovered_df = pd.read_csv(recovered)

    # get Canada dataframe
    canada_confirmed_df = get_country(confirmed_df,'Canada')
    canada_deaths_df = get_country(deaths_df,'Canada')
    canada_recovered_df = get_country(recovered_df,'Canada')

    # get Alberta specific data
    confirmed_data = canada_confirmed_df['Alberta']
    deaths_data = canada_deaths_df['Alberta']
    #recovered_data = canada_recovered_df['Alberta']

    # make / save plot
    fig = deaths_data.plot().get_figure()
    fig.savefig('canada_plot.pdf')

    #print(confirmed_data)
    #print(deaths_data)
    #print(recovered_data)
    print(canada_recovered_df)


if __name__ == "__main__":
    main()
