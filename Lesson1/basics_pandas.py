import pandas as pd
import numpy as np

'''
The following code is to help you play with the concept of Series in Pandas.

You can think of Series as an one-dimensional object that is similar to
an array, list, or column in a database. By default, it will assign an
index label to each item in the Series ranging from 0 to N, where N is
the number of items in the Series minus one.

Please feel free to play around with the concept of Series and see what it does

*This playground is inspired by Greg Reda's post on Intro to Pandas Data Structures:
http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/
'''
# Change False to True to create a Series object
if False:
    series = pd.Series(['Dave', 'Cheng-Han', 'Udacity', 42, -1789710578])
    print(series)

'''
You can also manually assign indices to the items in the Series when
creating the series
'''

# Change False to True to see custom index in action
if False:
    series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
                       index=['Instructor', 'Curriculum Manager',
                              'Course Number', 'Power Level'])
    print(series)

'''
You can use index to select specific items from the Series
'''
# Change False to True to see Series indexing in action
if False:
    series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
                       index=['Instructor', 'Curriculum Manager',
                              'Course Number', 'Power Level'])
    print(series['Instructor'])
    print()
    print(series[['Instructor', 'Curriculum Manager', 'Course Number']])

'''
You can also use boolean operators to select specific items from the Series
'''
# Change False to True to see boolean indexing in action
if False:
    cuteness = pd.Series([1, 2, 3, 4, 5], index=['Cockroach', 'Fish', 'Mini Pig',
                                                 'Puppy', 'Kitten'])
    print(cuteness > 3)
    print()
    print(cuteness[cuteness > 3])

'''
The following code is to help you play with the concept of Dataframe in Pandas.

You can think of a Dataframe as something with rows and columns. It is
similar to a spreadsheet, a database table, or R's data.frame object.

*This playground is inspired by Greg Reda's post on Intro to Pandas Data Structures:
http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/
'''

'''
To create a dataframe, you can pass a dictionary of lists to the Dataframe
constructor:
1) The key of the dictionary will be the column name
2) The associating list will be the values within that column.
'''
# Change False to True to see Dataframes in action
if False:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    print(football)

'''
Pandas also has various functions that will help you understand some basic
information about your data frame. Some of these functions are:
1) dtypes: to get the data type for each column
2) describe: useful for seeing basic statistics of the dataframe's numerical
   columns
3) head: displays the first five rows of the dataset
4) tail: displays the last five rows of the dataset
'''
# Change False to True to see these functions in action
if False:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    print()
    # football.dtypes()
    print()
    print(football.describe())
    print()
    print(football.head())
    print()
    print(football.tail())


#################
# Syntax Reminder:
#
# The following code would create a two-column pandas DataFrame
# named df with columns labeled 'name' and 'age':
#
# people = ['Sarah', 'Mike', 'Chrisna']
# ages  =  [28, 32, 25]
# df = DataFrame({'name' : Series(people),
#                 'age'  : Series(ages)})

def create_dataframe():
    """
    Create a pandas dataframe called 'olympic_medal_counts_df' containing
    the data from the table of 2014 Sochi winter olympics medal counts.

    The columns for this dataframe should be called
    'country_name', 'gold', 'silver', and 'bronze'.

    There is no need to  specify row indexes for this dataframe
    (in this case, the rows will automatically be assigned numbered indexes).

    You do not need to call the function in your code when running it in the
    browser - the grader will do that automatically when you submit or test it.
    """

    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

    olympic_medal_counts_df = {'country_name': countries,
                               'gold': pd.Series(gold),
                               'silver': pd.Series(silver),
                               'bronze': pd.Series(bronze)}
    olympic_medal_counts_df = pd.DataFrame(olympic_medal_counts_df)

    return olympic_medal_counts_df


'''
You can think of a DataFrame as a group of Series that share an index.
This makes it easy to select specific columns that you want from the
DataFrame.

Also a couple pointers:
1) Selecting a single column from the DataFrame will return a Series
2) Selecting multiple columns from the DataFrame will return a DataFrame

*This playground is inspired by Greg Reda's post on Intro to Pandas Data Structures:
http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/
'''
# Change False to True to see Series indexing in action
if False:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    print(football['year'])
    print('')
    print(football.year)  # shorthand for football['year']
    print('')
    print(football[['year', 'wins', 'losses']])

'''
Row selection can be done through multiple ways.

Some of the basic and common methods are:
   1) Slicing
   2) An individual index (through the functions iloc or loc)
   3) Boolean indexing

You can also combine multiple selection requirements through boolean
operators like & (and) or | (or)
'''
# Change False to True to see boolean indexing in action
if False:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    print(football.iloc[[0]])
    print("")
    print(football.loc[[0]])
    print("")
    print(football[3:5])
    print("")
    print(football[football.wins > 10])
    print("")
    print(football[(football.wins > 10) & (football.team == "Packers")])

olympic_medal_counts = create_dataframe()


def avg_medal_count1(df):
    """
    Compute the average number of bronze medals earned by countries who
    earned at least one gold medal.

    Save this to a variable named avg_bronze_at_least_one_gold. You do not
    need to call the function in your code when running it in the browser -
    the grader will do that automatically when you submit or test it.

    HINT-1:
    You can retrieve all of the values of a Pandas column from a
    data frame, "df", as follows:
    df['column_name']

    HINT-2:
    The numpy.mean function can accept as an argument a single
    Pandas column.

    For example, numpy.mean(df["col_name"]) would return the
    mean of the values located in "col_name" of a dataframe df.
    """

    df = df['bronze'][df['gold'] >= 1]
    return np.mean(df)


# print(avg_medal_count1(olympic_medal_counts))


def avg_medal_count2(df):
    """
    Using the dataframe's apply method, create a new Series called
    avg_medal_count that indicates the average number of gold, silver,
    and bronze medals earned amongst countries who earned at
    least one medal of any kind at the 2014 Sochi olympics.  Note that
    the countries list already only includes countries that have earned
    at least one medal. No additional filtering is necessary.

    You do not need to call the function in your code when running it in the
    browser - the grader will do that automatically when you submit or test it.
    """

    return df[['gold', 'silver', 'bronze']].apply(np.mean)

# print(avg_medal_count2(olympic_medal_counts))


def numpy_dot(df):
    """
    Imagine a point system in which each country is awarded 4 points for each
    gold medal,  2 points for each silver medal, and one point for each
    bronze medal.

    Using the numpy.dot function, create a new dataframe called
    'olympic_points_df' that includes:
        a) a column called 'country_name' with the country name
        b) a column called 'points' with the total number of points the country
           earned at the Sochi olympics.

    You do not need to call the function in your code when running it in the
    browser - the grader will do that automatically when you submit or test it.
    """
    scores = [4, 2, 1]
    df['points'] = np.dot(df[['gold', 'silver', 'bronze']], scores)

    # YOUR CODE HERE
    olympic_points_df = df[['country_name', 'points']]

    return olympic_points_df

print(numpy_dot(olympic_medal_counts))


def imputation(filename):
    """
    Pandas dataframes have a method called 'fillna(value)', such that you can
    pass in a single value to replace any NAs in a dataframe or series. You
    can call it like this:
        dataframe['column'] = dataframe['column'].fillna(value)

    Using the numpy.mean function, which calculates the mean of a numpy
    array, impute any missing values in our Lahman baseball
    data sets 'weight' column by setting them equal to the average weight.

    You can access the 'weight' column in the baseball data frame by
    calling baseball['weight']
    """

    baseball = pd.read_csv(filename)
    value = np.mean(baseball['weight'])

    baseball['weight'] = baseball['weight'].fillna(value)
    return baseball
