import time
from datetime import datetime, date
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input('Which City are you from? Chicago, New York City, Washington ::: '))
        if city.title() not in ('New York City', 'Chicago', 'Washington'):
          print('This city is not listed, Please try again')
          continue
        else:
           break


    # get user input for month (all, january, february, ... , june)
    while True:
        month = str(input('Which Month would you like to explore? All, January, February, March, April, May, June :::  '))
        if month.title() not in ('All, January, February, March, April, May, June'):
             print('This month is not listed, Please try again')
             continue
        else:
             break

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\nAre you looking for a particular day?  Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or 'All'.\n")
      if day.title() not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All'):
        print('This day is not listed, Please try again')
        continue
      else:
        break

    print('-'*40)
    return city.title(), month.title(), day.title()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])

     # to_datetime is used to convert date into date format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month_name()
    df['day'] = df['Start Time'].dt.weekday_name
    #print(df.head())

    # filter by month
    if month != 'All':

        # use the index of the month list
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == months[month]]

        # filter by day of week
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]
    #print(df.head())
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode().iloc[0]
    print('Most Common Month:', popular_month)

    # display the most common day of week
    popular_day = df['day'].mode().iloc[0]
    print('Most Common day:', popular_day)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode().iloc[0]
    print('Most Common Hour:', popular_hour)


    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    common_start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('Most common start station:', common_start_station)


    # display most commonly used end station
    common_end_station = df['End Station'].mode().iloc[0]
    print('\nMost common end station is {}\n'.format(common_end_station))


    # display most frequent combination of start station and end station trip
    combination_station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', common_start_station, " & ", common_end_station)


    print('\nThis took %s seconds.' % (time.time() - common_start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = datetime.time

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    time = total_travel_time
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    print('\nTotal travel time is {} days {} hours {} minutes {} seconds'.format(day, hour, minutes, seconds))


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    time1 = mean_travel_time
    day2 = time1// (24 * 3600)
    time1 = time1 % (24 * 3600)
    hour1 = time1 // 3600
    time1 %= 3600
    minutes1 = time1 // 60
    time1 %= 60
    seconds1 = time1
    print('\nMean travel time is {} hours {} minutes {} seconds'.format(hour1, minutes1, seconds1))


    print("\nThis took %s seconds." % (datetime.combine(date.today(), time.time) - datetime.combine(date.today(), time.time)))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    subscribers = df['User Type'].str.count('Subscriber').sum()
    no_of_customers = df['User Type'].str.count('Customer').sum()
    print('\nNumber of subscribers are {}\n'.format(int(subscribers)))
    print('\nNumber of customers are {}\n'.format(int(no_of_customers)))

    # Display counts of gender
    if('Gender' in df):
        male_count = df['Gender'].str.count('Male').sum()
        female_count = df['Gender'].str.count('Female').sum()
        print('\nNumber of male users are {}\n'.format(int(male_count)))
        print('\nNumber of female users are {}\n'.format(int(female_count)))


    # Display earliest, most recent, and most common year of birth
    if('Birth Year' in df):
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        most_common_birth_year = st.mode(df['Birth Year'])
        print('\n Oldest Birth Year is {}\n Youngest Birth Year is {}\n Most popular Birth Year is {}\n'.format(int(earliest_year), int(recent_year), int(most_common_birth_year)))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == '__main__':
    main()
