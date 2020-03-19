#Jared Gabaldon
#corona Virus

#donwload the lastest data here: https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide
# and save it as a .csv

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import glob
import os
import datetime


population_of_argentian = 44  #populalation size is repesented in millions
population_of_chile = 18
population_of_peru = 32
population_of_usa = 327
population_of_germany = 83
population_of_brazil = 209
population_of_china = 1300
population_of_italy = 61
population_of_uk = 66

def devide_country_population(country, population):

    density = country['Cases']/population

    return density

def get_specific_country_data(raw_data, country_name):

    country_data = raw_data[raw_data.CountryExp == country_name]
    country_data = country_data.iloc[::-1]

    return country_data


def plot_corona_cases_per_day():
    fig, ax = plt.subplots(figsize=(9,5))

    united_states_data.plot(x='DateRep', y='Cases', ax=ax, label='USA')
    argentina_data.plot(x='DateRep', y='Cases', ax=ax, label='Argentina')
    germany_data.plot(x='DateRep', y='Cases', ax=ax, label='Germany')
    chile_data.plot(x='DateRep', y='Cases', ax=ax, label='Chile')
    peru_data.plot(x='DateRep', y='Cases', ax=ax, label='Peru')
    brazil_data.plot(x='DateRep', y='Cases', ax=ax, label='Brazil')
    uk_data.plot(x='DateRep', y='Cases', ax=ax, label='UK')

    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    fig.autofmt_xdate()
    for tick in ax.get_xticklabels():
        tick.set_rotation(45)
    ax.tick_params(axis='x', which='both', labelsize=8)

    now = datetime.datetime.now()
    plt.title('New cases of corona virus per day prototype  ' + now.strftime("%b %d %Y") )
    plt.savefig('Outputs/New_Cases_Per_Day/new_cases_per_day_'+ now.strftime("%Y%m%d") +'.png')
    # plt.savefig('Outputs/new_cases_per_day_20200314.png')
    plt.show()

def plot_corona_case_density_per_day():
    fig2, ax2 = plt.subplots(figsize=(9,5))

    united_states_data.plot(x='DateRep', y='corona_density', ax=ax2, label='USA')
    argentina_data.plot(x='DateRep', y='corona_density', ax=ax2, label='Argentina')
    germany_data.plot(x='DateRep', y='corona_density', ax=ax2, label='Germany')
    chile_data.plot(x='DateRep', y='corona_density', ax=ax2, label='Chile')
    peru_data.plot(x='DateRep', y='corona_density', ax=ax2, label='Peru')
    brazil_data.plot(x='DateRep', y='corona_density', ax=ax2, label='Brazil')
    uk_data.plot(x='DateRep', y='corona_density', ax=ax2, label='UK')

    ax2.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    fig2.autofmt_xdate()
    for tick in ax2.get_xticklabels():
        tick.set_rotation(45)
    ax2.tick_params(axis='x', which='both', labelsize=8)

    now = datetime.datetime.now()
    plt.title('New cases of corona virus per day prototype (density)  '+ now.strftime("%b %d %Y") )
    plt.savefig('Outputs/New_Cases_Per_Day_Density/new_cases_per_day_density_'+ now.strftime("%Y%m%d") +'.png')
    plt.show()

def plot_china_corona_case_per_day():
    fig2, ax2 = plt.subplots(figsize=(9,5))

    china_data.plot(x='DateRep', y='Cases', ax=ax2, label='China')
    italy_data.plot(x='DateRep', y='Cases', ax=ax2, label='Italy')

    ax2.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    fig2.autofmt_xdate()
    for tick in ax2.get_xticklabels():
        tick.set_rotation(45)
    ax2.tick_params(axis='x', which='both', labelsize=8)

    now = datetime.datetime.now()
    plt.title('New cases of corona virus per day per mil people china prototype  '+ now.strftime("%b %d %Y") )
    plt.show()

def plot_china_corona_case_per_day_density():
    fig2, ax2 = plt.subplots(figsize=(9,5))

    china_data.plot(x='DateRep', y='corona_density', ax=ax2, label='China')
    italy_data.plot(x='DateRep', y='corona_density', ax=ax2, label='Italy')

    ax2.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    fig2.autofmt_xdate()
    for tick in ax2.get_xticklabels():
        tick.set_rotation(45)
    ax2.tick_params(axis='x', which='both', labelsize=8)

    now = datetime.datetime.now()
    plt.title('New cases of corona virus per day per mil people china prototype (density)  '+ now.strftime("%b %d %Y") )
    plt.show()

raw_data = pd.read_csv('Data/COVID-19-geographic-disbtribution-worldwide-2020-03-18.csv')
raw_data_china = raw_data

raw_data['DateRep']= pd.to_datetime(raw_data['DateRep'])
raw_data_china['DateRep']= pd.to_datetime(raw_data['DateRep'])

raw_data = raw_data[(raw_data['DateRep'] > '2020-02-20')]
raw_data_china = raw_data_china[(raw_data_china['DateRep'] > '2019-12-01')]

united_states_data = get_specific_country_data(raw_data, 'United_States_of_America')
germany_data = get_specific_country_data(raw_data, 'Germany')
argentina_data = get_specific_country_data(raw_data, 'Argentina')
chile_data = get_specific_country_data(raw_data, 'Chile')
peru_data = get_specific_country_data(raw_data, 'Peru')
brazil_data = get_specific_country_data(raw_data, 'Brazil')
uk_data = get_specific_country_data(raw_data, 'United_Kingdom')

china_data = get_specific_country_data(raw_data_china, 'China')
italy_data = get_specific_country_data(raw_data_china, 'Italy')

united_states_data['corona_density'] = devide_country_population(united_states_data, population_of_usa)
germany_data['corona_density'] = devide_country_population(germany_data, population_of_germany)
argentina_data['corona_density'] = devide_country_population(argentina_data, population_of_argentian)
chile_data['corona_density'] = devide_country_population(chile_data, population_of_chile)
peru_data['corona_density'] = devide_country_population(peru_data, population_of_peru)
brazil_data['corona_density'] = devide_country_population(brazil_data, population_of_brazil)
china_data['corona_density'] = devide_country_population(china_data, population_of_china)
italy_data['corona_density'] = devide_country_population(italy_data, population_of_italy)
uk_data['corona_density'] = devide_country_population(uk_data, population_of_uk)


plot_corona_cases_per_day()
plot_corona_case_density_per_day()

plot_china_corona_case_per_day()
plot_china_corona_case_per_day_density()



