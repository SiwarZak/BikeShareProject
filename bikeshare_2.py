'''import time
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


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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


if __name__ == "__main__":
	main()'''

import time
import pandas as pd
import numpy as np


CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york': 'new_york_city.csv',
    'washington': 'washington.csv'
}

# to load data based on user inputs
def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])

    # Convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month, day of week, and hour 
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month if applicable
    if month != 'none':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'none':
        df = df[df['day_of_week'] == day.title()]

    return df

# functions to calculate statistics
def time_stats(df):
    print("Calculating the most popular times of travel...")
    start_time = time.time()

    # most common month
    popular_month = df['month'].mode()[0]
    print(f"Most common month: {popular_month}")

    # most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print(f"Most common day of week: {popular_day}")

    # most common start hour
    popular_hour = df['hour'].mode()[0]
    print(f"Most common start hour: {popular_hour}")

    print(f"This took {time.time() - start_time} seconds.")
    print('-' * 40)

def station_stats(df):
    print("Calculating the most popular stations and trip...")
    start_time = time.time()

    # most common start station
    start_station = df['Start Station'].mode()[0]
    print(f"Most common start station: {start_station}")

    # most common end station
    end_station = df['End Station'].mode()[0]
    print(f"Most common end station: {end_station}")

    # most common trip from start to end
    df['Trip'] = df['Start Station'] + " to " + df['End Station']
    popular_trip = df['Trip'].mode()[0]
    print(f"Most common trip: {popular_trip}")

    print(f"This took {time.time() - start_time} seconds.")
    print('-' * 40)

def trip_duration_stats(df):
    print("Calculating trip duration...")
    start_time = time.time()

    # total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travel_time}")

    # avg travel time
    average_travel_time = df['Trip Duration'].mean()
    print(f"Average travel time: {average_travel_time}")

    print(f"This took {time.time() - start_time} seconds.")
    print('-' * 40)

def user_stats(df, city):
    print("Calculating user stats...")
    start_time = time.time()

    # Counts of user types
    user_types = df['User Type'].value_counts()
    print(f"Counts of user types:\n{user_types}")

    if city in ['chicago', 'new york']:
        # Counts of gender
        gender_counts = df['Gender'].value_counts()
        print(f"Counts of gender:\n{gender_counts}")

        # Earliest, most recent, and most common year of birth
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print(f"Earliest year of birth: {earliest_year}")
        print(f"Most recent year of birth: {most_recent_year}")
        print(f"Most common year of birth: {most_common_year}")
    else:
        print("Gender and birth year data not available for Washington.")

    print(f"This took {time.time() - start_time} seconds.")
    print('-' * 40)



def display_raw_data(df):
    #Display raw data upon user request in chunks of 5 rows.
    row_start = 0
    row_end = 5
    while row_start < len(df):
        view_data = input("Would you like to see 5 lines of raw data? Enter 'yes' or 'no': ").lower()
        if view_data != 'yes':
            break
        print(df.iloc[row_start:row_end])
        row_start += 5
        row_end += 5 

# Main function to run the program
def main():
    while True:
        city = input("Would you like to see data for Chicago, New York, or Washington? ").lower()
        while city not in CITY_DATA:
            city = input("Invalid input. Please choose from Chicago, New York, or Washington: ").lower()

        filter_choice = input("Would you like to filter the data by month, day, or not at all? Type 'none' for no time filter: ").lower()
        while filter_choice not in ['month', 'day', 'none']:
            filter_choice = input("Invalid input. Please type 'month', 'day', or 'none': ").lower()

        month = 'none'
        day = 'none'

        if filter_choice == 'month':
            month = input("Which month? January, February, March, April, May, or June? Please type out the full month name: ").lower()
            while month not in ['january', 'february', 'march', 'april', 'may', 'june']:
                month = input("Invalid input. Please choose from January, February, March, April, May, or June: ").lower()
        elif filter_choice == 'day':
            day = input("Which day? Please type the full name of the day (e.g., Monday, Tuesday, etc.): ").lower()

        print("\nLoading data...\n")
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input("Would you like to restart? Type 'yes' or 'no': ").lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()

