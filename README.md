## Date created
31/12/2023

# Bikeshare Data

## Description
This project consists of python program _bikeshare.py_ that queries and filters bikeshare rental data for a number of USA cities: Chicago, New York City and Washington.  After starting the program the user is prompted to select the city (a mandatory selection), and then allows the user to select to filter data on a particular month and/or day as additional optional filters.  The user may enter **all** for either the month or day selection to not filter on month or day.

The program performs the following primary functions:
1. Prompts the user to select city, and then optionally month and/or day to filter data over in the **get_filters** function.
2. Reads the selected city's datafile in the **load_data** function.
3. Extracts the month and day from the **Start Time** column in the **load_data** function.
4. Filters the city data in the **load_data** function using the user selected filters from the **get_filters** function.  All subsequent calculations are performed on the filtered data.
5. Calculates and prints the most popular month, day and hour in the **time_stats** function.
6. Calculates and prints the most popular start station and end station, and most popular combination of start and end stations (the order of start and end station does not matter) in the **station_stats** function.
7. Calculates and prints the total travel time (all trips summated) in seconds and also hours, and the mean travel time in seconds in the **trip_duration_stats** function.
8. Calculates and prints user type counts in the **user_stats** function.  If the respective columns are present in the city's datafile this function also calculates and prints user gender counts, and the earliest, most recent and most common user birth year.
9. Prompts the user whether they would like to view the tabulated data and if so, displays data 5 rows at a time, allowing the user to manually select whether to scroll further down the data in 5 row blocks.  This is performed by the **display_data** function.
10. Prompts the user whether they would like to run another analysis or exit the program.

Some secondary functions:
a. Processing time is calculated for all **_stats** functions.
b. Error handling implemented on user inputs to remove case sensitivity.

All rental data is for the months January to June 2017.  The user may only select from these months.

The rental data may or may not include user gender and birth year information.  The code checks whether these columns are present prior to analysing statistics for them.

**Note:**  The code can query and filter only one city's datafile at a time.  Mutlicity queries are not possible, but the code does prompt the user whether they wish to run an additional analysis.

### Using Other Data
To use this code with other data files, the following code changes are required.

#### Filenames and Format
The files must be in csv format, otherwise additional statements will need to be added to read the file in the correct format in the **load_data** funtion.
City names and data filenames will need to be added to the **CITY_DATA** dictionary at the start of the code.
City names will need to be added to the **get_filters** function.

#### Column Names and Data Types
Column Names need to match the following text strings **in bold** and are case sensitive.
**Start Time**  The start time of the trip in a format compatible with pandas to_datetime format and down to hourly resolution.
**End Time**  The end time of the trip in a format compatible with pandas to_datetime format and down to hourly resolution.
**Trip Duration**  The duration of the trip in seconds as an integer or float.
**Start Station**  The trip starting station as a text string.
**End Station**  The trip starting station as a text string.
**User Type**  A user type category, e.g. Customer and Subscriber, but other categories could be used if using other data.  The data type for these values does not need to be a string.
**Gender**  The gender of the user.  The code checks if this column exists prior to analysing it.  The data type for these values does not need to be a string.
**Birth Year**  The birth year of the user as an integer or float.  The code checks if this column exists prior to analysing it.

#### Code Changes Required
The data files used only have data for January through June.  If you have data for other months, add these months to the **get_filters** function, in the month_input statements.  Make sure the added month names are Capitalised.

The code allows for optional **Gender** and **Birth Year** columns.  If any other columns are missing in your data e.g. **Trip Duration**, **Start Station**, **End Station**, **User Type**, additional statements will need to be added in the **station_stats**, **trip_duration_stats** and **user_stats** functions to handle missing columns.  Note that **Start Time** is a mandatory column as month, day and hour are extracted from this column's values.

# Files used
**Note:** All files need to be located in the same directory.
**bikeshare.py** contains the python code to be run.
**chicago.csv** contains the rental data for Chicago, Il, USA.
**new_york_city.csv** contains the rental data for New York City, NY, USA.
**washington.csv** contains the rental data for Washington, DC, USA.

# Credits
Udacity Programming for Data Science with Python project submission.
