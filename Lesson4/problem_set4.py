from pandas import *
from ggplot import *


def plot_weather_data(turnstile_weather):
    """
    You are passed in a dataframe called turnstile_weather.
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.
    You should feel free to implement something that we discussed in class
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/

    You can check out:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv

    To see all the columns and data points included in the turnstile_weather
    dataframe.

    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    """

    weather_data = pandas.read_csv(turnstile_weather)
    plot = ggplot(weather_data, aes('Hour', 'ENTRIESn_hourly')) + \
        geom_point(color='red') + \
        geom_line(color='red') + \
        ggtitle('Subway entries per hour') + \
        xlab('Hour') + \
        ylab('Entries')
    return plot


# print(plot_weather_data(r'..\Lesson3\turnstile_data_master_with_weather.csv'))

def plot_weather_data2(turnstile_weather):
    """
    plot_weather_data is passed a dataframe called turnstile_weather.
    Use turnstile_weather along with ggplot to make another data visualization
    focused on the MTA and weather data we used in Project 3.

    Make a type of visualization different than what you did in the previous exercise.
    Try to use the data in a different way (e.g., if you made a lineplot concerning
    ridership and time of day in exercise #1, maybe look at weather and try to make a
    histogram in this exercise). Or try to use multiple encodings in your graph if
    you didn't in the previous exercise.

    You should feel free to implement something that we discussed in class
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time-of-day or day-of-week
     * How ridership varies by subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/

    You can check out the link
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv
    to see all the columns and data points included in the turnstile_weather
    dataframe.

   However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    """

    weather_data = pandas.read_csv(turnstile_weather)
    plot = ggplot(weather_data, aes('UNIT', 'ENTRIESn_hourly')) + \
        geom_point() + \
        geom_line() + \
        ggtitle('Subway entries per hour') + \
        xlab('Hour') + \
        ylab('Entries')
    return plot


# print(plot_weather_data2(r'..\Lesson3\turnstile_data_master_with_weather.csv'))
# p = ggplot(aes(x='carat'), data=diamonds)
# print(p + geom_histogram() + ggtitle("Histogram of Diamond Carats") + labs("Carats", "Freq"))
print(ggplot(aes(x='date', y='beef'), data=meat) +
      geom_point(color='lightblue') +
      stat_smooth(span=.15, color='black', se=True) +
      ggtitle("Beef: It's What's for Dinner") +
      xlab("Date") +
      ylab("Head of Cattle Slaughtered"))
