import time
import pandas as pd
# Import numpy included in project stating template but no used in this program. 
#import numpy as np

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # Lowercase the entry to match the CITY_DATA dictionary format.
    while True:
        city = input('Enter city (chicago, new york city, washington)\n').lower()
        if city in CITY_DATA:
            break
        else:
            print('The data for that city does not exist.  Please select again and check spelling.')
    # TO DO: get user input for month (all, january, february, ... , june)
    #Capitalize the day to match dataframe format when day is extracted from Start Time text string in load_data function.
    while True:
        month = input('Enter month if you wish to filter on a particular month (Jan - Jun), or type all for all months\n(i.e. all, january, february, ..., june)\n').capitalize()
        if month in ('All', 'January', 'February', 'March', 'April', 'May', 'June'):
            break
        else:
            print('The data for that month does not exist.  Please select again.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday).
    #Capitalize the day to match dataframe format when day is extracted from Start Time text string in load_data function.
    while True:
        day = input('Enter start day if you wish to filter on a particular day, or type all for all days\n(all, sunday, monday, ..., saturday)\n').capitalize()
        if day in ('All','Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'):
            break
        else:
            print('You have mispelled the day or need to enter all.  Please try again.')

    # Displays the inputs back to user for clarification.
    print('\nYou have selected data for city/month/day:\n', city, '/ ',month,'/ ',day)

    # End of the get_filters function.  City, month and day are returned to be used in city file selection and dataframe month/day queries.
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
    #Assign the city data csv name to be analysed. Use the user's city input as the key
    #in the CITY_DATA dictionary to get the correct filename to upload.
    city_filename = CITY_DATA.get(city)

    #Read in the city data.  The unqueried dataframe will be df0.
    df0 = pd.read_csv(city_filename)

    ## convert the Start Time column to datetime
    df0['Start Time'] = pd.to_datetime(df0['Start Time'])

    ## extract month from the Start Time column to create a month column as a string
    df0['Month'] = df0['Start Time'].dt.month_name().astype(str)

    # extract day from the Start Time column to create a day column as a string
    df0['Day'] = df0['Start Time'].dt.day_name().astype(str)

    # extract hour from the Start Time column to create an hour column
    df0['Hour'] = df0['Start Time'].dt.hour

    #Conditional query of city dataframe based on month and/or day selected by user.
    if month == 'All' and day == 'All':
        df = df0 #no query, as all months and all days selected.
    elif month == 'All':
        df = df0[df0['Day'] == day] #Query on day only as all months selected.
    elif day == 'All':
        df = df0[df0['Month'] == month] #Query on month only as all days selected.
    else:
        # Query on both day and month.
        df = df0[(df0['Month'] == month) & (df0['Day'] == day)]

    #The code below can be uncommented to write the queried dataframe to file
    #and check the user entries are the correct format and type for the dataframe.
    #df.to_csv("FilteredDataframe.csv")
    #print(month, type(month))
    #print(day, type(day))

    #End of load_data function.  Returns the queried dataframe for further analysis.
    return df;

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month.  Specify 0 index to select value (and not key).
    month_popular = df['Month'].mode()[0]
    print('\nThe most popular trip month for this city/month/day is:\n', month_popular)

    # TO DO: display the most common day of week
    day_popular = df['Day'].mode()[0]
    print('\nThe most popular trip start day for this city/month/day is:\n', day_popular)

    # TO DO: display the most common start hour
    hour_popular = df['Hour'].mode()[0]
    print('\nThe most popular trip start hour for this city/month/day is:\n', hour_popular)

    # Round execution duration to milliseconds.
    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station.  Specify 0 index to select value (and not key).
    start_stn_popular = df['Start Station'].mode()[0]
    print('The most commonly used starting station for this city/month/day is:\n', start_stn_popular)

    # TO DO: display most commonly used end station
    end_stn_popular = df['End Station'].mode()[0]
    print('\nThe most commonly used end station is:\n', end_stn_popular)

    # TO DO: display most frequent combination of start station and end station trip
    stn_combo_popular = df.groupby('Start Station')['End Station'].value_counts().idxmax()
    print('\nThe most frequent combination of start and end stations for this city/month/day is:\n', stn_combo_popular)
    # Round execution duration to milliseconds.
    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time.  Convert to integer to remove decimal places.
    tot_travel_time = int(df['Trip Duration'].sum())
    # Recalculate total travel time in hours and round to 2 decimal places.
    total_travel_time_hrs = round(tot_travel_time/3600,2)
    print('The total travel time for this city/month/day is:\n', tot_travel_time, ' seconds, i.e. ', total_travel_time_hrs, ' hours')

    # TO DO: display mean travel time, and covert to integer to remove decimal places.
    mean_travel_time = int(df['Trip Duration'].mean())
    print('\nThe mean travel time for this city/month/day is:\n', mean_travel_time, ' seconds')

    # Round execution duration to milliseconds.
    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.
       Some city data files have user gender and birth year, but others do not.
       Check for gender and birth year dataframe indexes prior to analysing these values.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types.  Convert to dictionary to prevent Name and dtype value_counts
    # being printed.
    user_type_counts = df['User Type'].value_counts().to_dict()
    print('The User Type counts for this city/month/day are:\n', user_type_counts)

    # TO DO: Display counts of gender.  Check dataframe gender index exists.
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts().to_dict()
        print('\nThe gender counts for this city/month/day are:\n', gender_counts)
    else:
        print('The data for this city does not include user gender information')

    """ TO DO: Display earliest, most recent, and most common year of birth.
        Check that dataframe includes birth year index.
        Convert to integer to remove decimal place in displayed year.
    """
    if 'Birth Year' in df.columns:
        earliest_birth = int(df['Birth Year'].min())
        newest_birth = int(df['Birth Year'].max())
        # Add index to mode to prevent key being printed with value.
        commonest_birth = int(df['Birth Year'].mode()[0])
        print('\nThe earliest, most recent and most common years of birth for this city/month/day are:\n {}, {}, and {}'.format(earliest_birth, newest_birth, commonest_birth))
    else:
        print('The data for this city does not include user birth year information')

    # Round execution duration to milliseconds.
    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)

def display_data(df):
    # Ask the user whether they want to display the data from the queried dataFrame.  Converts entry to lowercase.
    display_data_input = input("Would you like to see the city/month/day data? Please enter y or n:").lower()
    #Initialise the row counter for the while loop.
    i = 0
    #Initiate loop for displaying data 5 rows at a time.
    while True:
        #Exits loop if user chooses not to view rows at any time.
        if display_data_input[0] == 'n':
            break
        #Displays queried dataFrame data if user enters y.
        elif display_data_input[0] == 'y':
            #Print 5 rows of the dataFrame starting at row i (initialised prior to loop at row 0).  Print all columns.
            print(df.iloc[i:i+5,:])
            #Prompts user to select whether they wish to view another 5 rows.  Converts input to lowercase.
            display_data_input = input("Would you like to see more 5 more rows of the selected city/month/day data?").lower()
            #Increments i by 5 to display next 5 rows of data.
            i += 5
        #Check for typographical error in user input.
        else:
            display_data_input = input("\nYour input is invalid. Please enter y or n\n").lower()

def main():
    while True:
        # load the user selected and cleaned city, month and day inputs into the get_filters function
        # to clean and format them to match the dataframe value types.
        city, month, day = get_filters()
        # Load the filters into load_data function to upload the city data and query the dataframe and
        # extract the selected month and day rows.
        df = load_data(city, month, day)
        # Analyse the queried dataframe for time, station, trip duration and user statistics.
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        # Allow user to print dataframe rows to screen of queried dataFrame.
        display_data(df)

        # Allow user to run another analisys.  
        restart = input('\nWould you like to restart?  Please enter y or n.\n').lower()
        #Checks first letter entered by user is y incase they enter "yes".
        if restart[0] != 'y':
            break

# Check whether script is being run directly, and if so define the main entry point for the script.
if __name__ == "__main__":
	main()
