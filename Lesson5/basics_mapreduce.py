import logging
import sys
import string

from util import logfile

logging.basicConfig(filename=logfile, format='%(message)s',
                   level=logging.INFO, filemode='w')


def word_count():
    # For this exercise, write a program that serially counts the number of occurrences
    # of each word in the book Alice in Wonderland.
    #
    # The text of Alice in Wonderland will be fed into your program line-by-line.
    # Your program needs to take each line and do the following:
    # 1) Tokenize the line into string tokens by whitespace
    #    Example: "Hello, World!" should be converted into "Hello," and "World!"
    #    (This part has been done for you.)
    #
    # 2) Remove all punctuation
    #    Example: "Hello," and "World!" should be converted into "Hello" and "World"
    #
    # 3) Make all letters lowercase
    #    Example: "Hello" and "World" should be converted to "hello" and "world"
    #
    # Store the the number of times that a word appears in Alice in Wonderland
    # in the word_counts dictionary, and then *print* (don't return) that dictionary
    #
    # In this exercise, print statements will be considered your final output. Because
    # of this, printing a debug statement will cause the grader to break. Instead,
    # you can use the logging module which we've configured for you.
    #
    # For example:
    # logging.info("My debugging message")
    #
    # The logging module can be used to give you more control over your
    # debugging or other messages than you can get by printing them. Messages
    # logged via the logger we configured will be saved to a
    # file. If you click "Test Run", then you will see the contents of that file
    # once your program has finished running.
    #
    # The logging module also has other capabilities; see
    # https://docs.python.org/2/library/logging.html
    # for more information.

    word_counts = {}

    for line in sys.stdin:
        data = line.strip().split(" ")
        for key in data:
            key = key.translate(string.maketrans("",""),string.punctuation).lower()
            if key in word_counts.keys():
                word_counts[key] += 1
            else:
                word_counts[key] = 1
    print(word_counts)

word_count()


def mapper():

    #Also make sure to fill out the reducer code before clicking "Test Run" or "Submit".

    #Each line will be a comma-separated list of values. The
    #header row WILL be included. Tokenize each row using the
    #commas, and emit (i.e. print) a key-value pair containing the
    #district (not state) and Aadhaar generated, separated by a tab.
    #Skip rows without the correct number of tokens and also skip
    #the header row.

    #You can see a copy of the the input Aadhaar data
    #in the link below:
    #https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv

    #Since you are printing the output of your program, printing a debug
    #statement will interfere with the operation of the grader. Instead,
    #use the logging module, which we've configured to log to a file printed
    #when you click "Test Run". For example:
    #logging.info("My debugging message")
    #
    #Note that, unlike print, logging.info will take only a single argument.
    #So logging.info("my message") will work, but logging.info("my","message") will not.

    for line in sys.stdin:
        data = line.strip().split(",")
        if len(data) != 12 or data[0] == 'Registrar':
            continue
        print('{0}\t{1}'.format(data[3], data[8]))

mapper()


def reducer():
    # Also make sure to fill out the mapper code before clicking "Test Run" or "Submit".

    # Each line will be a key-value pair separated by a tab character.
    # Print out each key once, along with the total number of Aadhaar
    # generated, separated by a tab. Make sure each key-value pair is
    # formatted correctly! Here's a sample final key-value pair: 'Gujarat\t5.0'

    # Since you are printing the output of your program, printing a debug
    # statement will interfere with the operation of the grader. Instead,
    # use the logging module, which we've configured to log to a file printed
    # when you click "Test Run". For example:
    # logging.info("My debugging message")
    # Note that, unlike print, logging.info will take only a single argument.
    # So logging.info("my message") will work, but logging.info("my","message") will not.

    old_key = None
    word_count = 0

    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(data) != 2:
            continue
        this_key, count = data
        if old_key and old_key != this_key:
            print('{0}\t{1}'.format(old_key, word_count))
            word_count = 0
        old_key = this_key
        word_count += float(count)
    if old_key != None:
        print('{0}\t{1}'.format(old_key, word_count))

reducer()
