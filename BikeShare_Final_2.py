'''
Created on 10/07/2020

@author: Sandra
'''
import pandas as pd
from astropy.units import day

CITY_DATA = { 'C': 'chicago.csv',
              'N': 'new_york_city.csv',
              'W': 'washington.csv' }

city_dict = {'C':'Chicago',
             'N':'New York City',
             'W':'Washington'}

month_dict = {'1':'January',
              '2':'February',
              '3':'March',
              '4':'April',
              '5':'May',
              '6':'June',
              'A':'All'}

day_dict = {'0':'Monday',
            '1':'Tuesday',
            '2':'Wednesday',
            '3':'Thursday',
            '4':'Friday',
            '5':'Saturday',
            '6':'Sunday',
            'A':'All'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - letter of the city to analyze
        (str) month - number of the month to filter by, or "A' for all to apply no month filter
        (str) day - number of the day of week to filter by, or "A" for all to apply no day filter
    """
    final_answer_string = 'YN'
    result_fa = 0    
    final_answer = 'N'
    while final_answer != 'Y':
        print()
        print('Hello! Let\'s explore some US bikeshare data!')
        
        #get user input for city 
        letter_string = 'WCN'
        result_c = 0
        
        while result_c == 0:
            city = str(input("Which city would you like to analyse? Please enter C for Chicago, N for New York City or W for Washington")).upper()
            
            if len(city) <2:
                for letter in letter_string:
                    if city[0][0] == letter:
                        result_c +=1
                        
                if result_c != 1:
                    print('Whoops, that doesn\'t look like a city I recognise')
        
        #get user input for month   
        month_string = '123456A'
        result_m = 0
        
        while result_m == 0:
            month = str(input('Which month would you like to filter by? Enter 1 for Jan, 2 for Feb, 3 for Mar, 4 for Apr, 5 for May, 6 for Jun or A for all months')).upper()
            
            if len(month) <2:
                for m in month_string:
                    if month[0][0] == m:
                        result_m +=1
                        
                if result_m !=1:
                    print('Whoops, that doesn\'t look like a month I recognise')        
        
        #get user input for day of week
        day_string = '0123456A'
        result_d = 0
        
        while result_d == 0:
            day = str(input('Which day would you like to filter by? Enter 0 for Mon, 1 for Tue, 2 for Wed, 3 for Thur, 4 for Fri, 5 for Sat, 6 for Sun or A for all days')).upper()
            
            if len(day) <2:
                for d in day_string:
                    if day[0][0] == d:
                        result_d +=1
                        
                if result_d !=1:
                    print('Whoops, that doesn\'t look like a day I recognise')

        print()
        print('Please confirm your selection as below:')
        
        for key, value in city_dict.items():
            if (key == city):
                print('City Filter: {}'.format(value))
                
        for key, value in month_dict.items():
            if (key == month):
                print('Month Filter: {}'.format(value))
    
        for key, value in day_dict.items():
            if (key == day):
                print('Day Filter: {}'.format(value))
        
        print()
        result_fa =0
        while result_fa ==0:
            final_answer = str(input('Please enter Y to continue with this selection, or N to start again.')).upper()

            if len(final_answer) <2:
                for i in final_answer_string:
                    if final_answer[0][0] == i:
                        result_fa +=1
                        
                if result_fa != 1:
                    print('Whoops, that doesn\'t look like input I recognise.')
    return [city,month,day]


def load_data(my_list):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - letter of the city to analyze
        (str) month - number of the month to filter by, or "A' for all to apply no month filter
        (str) day - number of the day of week to filter by, or "A" for all to apply no day filter
    Returns:
        Statistical output and snapshot of raw data if requested.
    """
    city = my_list[0]
    month = my_list[1]
    day = my_list[2]
    
    # load the datafile
    for key, value in CITY_DATA.items():
            if (key == city):
                df = pd.read_csv(value)
    
    # convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day_of_week and hour from Start Time column, add Start_End_Station Column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    df['start_end_station'] = df['Start Station'] + '_' + df['End Station']

    #filter by month
    if month != 'A':
        months = ['1','2','3','4','5','6']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day
    if day != 'A':
        days = ['0','1','2','3','4','5','6']
        day = days.index(day)
        df = df[df['day_of_week'] == day]
    
    print()
    print('Please find your results below')
    print('-'*60)
    print()
    
    #only execute if month selection is All
    if month =='A':
        popular_month = df['month'].mode()[0]
        print('Most popular month: ',popular_month) 

    #only execute of day selection is All
    if day == 'A':
        popular_day = df['day_of_week'].mode()[0]
        print('Most popular day: ',popular_day)                  

    popular_hour = df['hour'].mode()[0]
    popular_time_in_use = df['Trip Duration'].mode()[0]
    average_usage_period = df['Trip Duration'].mean(axis=0)
    total_sum_use_time = df['Trip Duration'].sum(axis=0)
    popular_start_station = df['Start Station'].mode()[0]
    popular_end_station = df['End Station'].mode()[0]
    popular_start_end_station = df['start_end_station'].mode()[0]
    user_types = df['User Type'].value_counts()

    print('Most popular start hour: ',popular_hour)
    print ('Most popular use time in minutes: ',popular_time_in_use/60)
    print('Average usage period in minutes: ',average_usage_period/60)
    print('Total sum of use time in hours: ',total_sum_use_time/3600)
    print('Most popular start station: ',popular_start_station)
    print('Most popular end station: ',popular_end_station)
    print('Most Popular start & end station combination: ',popular_start_end_station)
    print()
    print('User Type: ',user_types)
    print()
    if city != 'W':
        gender = df['Gender'].value_counts()
        print('Gender: ',gender)
        print()
        

    #get user input for raw data
    x = (0)
    y = (5)
    print('-'*60)
    print()
    row = 'Y'
    while x == 0:
        row = str(input('Would you like to see 5 rows of raw data? Please enter Y for Yes, or N for No to exit')).upper()
            
        if row == 'Y':
            print(df.iloc[x:y])
            print('-'*60)
            print()
                
            while row =='Y':
                row_again = str(input('Would you like to see 5 more rows of data? Please enter Y for Yes or N for No to exit')).upper()
                    
                if row_again == 'Y':
                    x +=5
                    y +=5
                    print(df.iloc[x:y])
                    print('-'*60)
                        
                if row_again == 'N':
                    print()
                    print('Goodbye!')
                    break   
                
        if row == 'N':
            print()
            print('Goodbye!')
            break               


load_data(get_filters())