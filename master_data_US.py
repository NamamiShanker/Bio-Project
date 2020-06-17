'''
Author:         Namami Shanker
Date:           17/06/2020
Data Source:    https://github.com/CSSEGISandData/COVID-19
About:  This program extracts information of confirmed cases of Covid-19 and total deaths only in US, starting from the date 22-Jan-2020
        upto the latest updation on the GitHub repository from which it extracts the data, which is generally updated daily. Please be 
        informed that in US the clear data about number of patients is not available so that isnt provided by this script.
        
        Thanks for using my script. Below are the states from which it can extract data.


American Samoa
Guam
Northern Mariana Islands
Puerto Rico
Virgin Islands
Alabama
Alaska
Arizona
Arkansas
California
Colorado
Connecticut
Delaware
District of Columbia
Florida
Georgia
Hawaii
Idaho
Illinois
Indiana
Iowa
Kansas
Kentucky
Louisiana
Maine
Maryland
Massachusetts
Michigan
Minnesota
Mississippi
Missouri
Montana
Nebraska
Nevada
New Hampshire
New Jersey
New Mexico
New York
North Carolina
North Dakota
Ohio
Oklahoma
Oregon
Pennsylvania
Rhode Island
South Carolina
South Dakota
Tennessee
Texas
Utah
Vermont
Virginia
Washington
West Virginia
Wisconsin
Wyoming
Diamond Princess
Grand Princess
'''


import pandas as pd
import datetime
import re

def download_data(state):
    temp = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
    raw_confirmed = temp[temp.Province_State == state]
    temp = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv')
    raw_deaths = temp[temp.Province_State == state]
    return raw_confirmed, raw_deaths

def extract_data(state, raw_confirmed, raw_deaths):
    raw_confirmed = raw_confirmed.iloc[:,11: ]
    lis = []
    for i in raw_confirmed.columns:
        sum = raw_confirmed[i].sum()
        dic = {'state':state,'date':i, 'cases_confirmed': sum}
        lis.append(dic)
    confirmed = pd.DataFrame(lis)
    raw_deaths = raw_deaths.iloc[:, 12:]
    lis = []
    for i in raw_deaths.columns:
        sum = raw_deaths[i].sum()
        lis.append(sum)
    lis = pd.Series(lis)
    confirmed['total_deaths'] = lis
    return confirmed

def main():
    state = 'California' # input("Enter the name of US state. Please be sure to enter the name exactly same as mentioned in the state list: ")
    raw_confirmed, raw_deaths = download_data(state)
    confirmed_cummulative = extract_data(state, raw_confirmed, raw_deaths)
    confirmed_cummulative.to_csv('data.csv')


if __name__ == '__main__':
    main()