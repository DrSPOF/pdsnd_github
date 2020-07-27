'''
Created on 10/07/2020

@author: Sandra
'''
import pandas as pd
from astropy.units import day

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

month_dict = {'jan':'1',
              'feb':'2',
              'mar':'3',
              'apr':'4',
              'may':'5',
              'jun':'6',
              'all':'all'}

day_dict = {'monday':'0',
            'tuesday':'1',
            'wednesday':'2',
            'thursday':'3',
            'friday':'4',
            'saturday':'5',
            'sunday':'6',
            'all':'all'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name (abbreviated to 3 letetrs) of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    final_answer_string = 'YN'
    result_fa = 0    
    final_answer = 'N'
    while final_answer != 'Y':
        print('Hello! Let\'s explore some US bikeshare data!')
        
        #get user input for city 
        city_list = ['washington', 'chicago','new york']
        print(city_list[0],city_list[1],city_list[2])
        result_c = 0
        
        while result_c == 0:
            city = str(input("Which city would you like to analyse? Please enter Chicago, New York or Washington")).lower()
            
            for c in city_list:
                if c == city:
                    result_c +=1
            if result_c == 0:
                print('Whoops, that doesn\'t look like a city I recognise')        
        
        #get user input for month   
        month_list = ['jan', 'feb', 'mar','apr','may','jun','all']
        result_m = 0
        
        while result_m == 0:
            month = str(input('Which month would you like to filter by? Enter Jan, Feb, Mar, Apr, May, Jun or All for all months')).lower()

            for m in month_list:
                if m == month:
                    result_m +=1
                        
            if result_m !=1:
                print('Whoops, that doesn\'t look like a month I recognise')        
        
        #get user input for day of week
        day_list = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
        result_d = 0
        
        while result_d == 0:
            day = str(input('Which day would you like to filter by? Enter any day of the week, or enter All for all days')).lower()
            
            for d in day_list:
                if d == day:
                    result_d +=1
                        
            if result_d !=1:
                print('Whoops, that doesn\'t look like a day I recognise')

        print()
        print('Please confirm your selection as below:')
        print('City Filter: {}'.format(city).title())
        print('Month Filter: {}'.format(month).title())
        print('Day Filter: {}'.format(day).title())
                
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
        (str) city - name of the city to analyze
        (str) month - name (abbreviated to 3 letters)  of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        Statistical output and snapshot of raw data if requested.
    """
    city = my_list[0]
    
    for key, value in month_dict.items():
            if (key == my_list[1]):
                month = (value)

    for key, value in day_dict.items():
            if (key == my_list[2]):
                day = (value)
                
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
    if month != 'all':
        months = ['1','2','3','4','5','6']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day
    if day != 'all':
        days = ['0','1','2','3','4','5','6']
        day = days.index(day)
        df = df[df['day_of_week'] == day]
    
    print()
    print('Please find your results below')
    print()
    
    #only execute if month selection is All
    if month =='all':
        popular_month = df['month'].mode()[0]
        print('Most popular month: ',popular_month) 

    #only execute of day selection is All
    if day == 'all':
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
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print('Gender: ',gender)
        print()

    #get user input for raw data
    x = (0)
    y = (5)
    
    row = 'Y'
    while x == 0:
        row = str(input('Would you like to see 5 rows of raw data? PLease enter Y for Yes, or N for No to exit')).upper()
            
        if row == 'Y':
            print(df.iloc[x:y])
                
            while row =='Y':
                row_again = str(input('Would you like to see 5 more rows of data? Please enter Y for Yes or N for No to exit')).upper()
                    
                if row_again == 'Y':
                    x +=5
                    y +=5
                    print(df.iloc[x:y])
                        
                if row_again == 'N':
                    print()
                    print('Goodbye!')
                    break   
                
        if row == 'N':
            print()
            print('Goodbye!')
            break               


load_data(get_filters())