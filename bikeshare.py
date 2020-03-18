import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES=['chicago', 'new york', 'washington']

months=['january','february','march','april','may','june']

days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter city name:  ").lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("re-enter city.")
            continue
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter month:  ").lower()
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("re-enter month.")
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter day:  ").lower()
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday'):
            print("r-enter day.")
            continue
        else:
            break


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month
    df['week day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    #filters "referenced from-stackflow discussions"
    if month != 'all':
        month = months.index(month) + 1
        df = df[ df['month'] == month ]


    if day != 'all':
        df = df[ df['week day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month = months[df['month'].mode()[0]-1]

    print('the most common month:', common_month)

    # TO DO: display the most common day of week
    common_day = df['week day'].mode()[0]

    print('the most common day of the week:', common_day)

    # TO DO: display the most common start hour

    common_hour = df['hour'].mode()[0]

    print('the most common start:', common_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()

    print('most commonly used start station is', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()

    print('most commonly used end station is', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination_stations = df[['Start Station','End Station']].mode()
    print('most frequent combination of start station and end station trip is {} and {}:', format. (common_end_station[0],common_start_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    total_travel_time = df['hour'].sum()

    print('total travel time is: 'total_travel_time)

    # TO DO: display mean travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    mean_travel_time = df['hour'].mean()

    print('mean travel time is: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print(user_types)

    # TO DO: Display counts of gender
    gender_counts = df['Gender'].value_counts()

    print(gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    year_births = df['Birth Year'].value_counts().max().min()

    print(year_births)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    first_row = 0
    display_raw_data = input('\ndo you want to see first few lines of raw data?. Type yes or no.\n')
    while display_raw_data.lower() == 'yes':
        raw_head = df.iloc[first_row:first_row+5]
        print(raw_head)
        first_row += 5
        display_raw_data = input('\nWould you like to see more data? Enter yes or   no.\n')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# used sites: stackoverflow, classroom discussions and general python facebook fans p
