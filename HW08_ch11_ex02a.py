#!/usr/bin/env python3
# HW08_ch11_ex02a
# This is discussed in ThinkPython2 but not formally an exercise.
# Dictionaries have a method called 'get' that takes a key and a default value.
# If the key appears in the dictionary, get returns the corresponding value;
# otherwise it returns the default value. For example:

# >>> h = histogram('a')
# >>> print h
# {'a': 1}
# >>> h.get('a', 0)
# 1
# >>> h.get('b', 0)
# 0

# (1) Use get to write histogram_old more concisely. You should be able to
# eliminate the if statement.

# (2) Use histogram_new to take pledge.txt and create a dict histogram with
# word counts (do not change the case of the words).
###############################################################################
# Imports


# Body
pledge_histogram = {}


def histogram_old(word_list):
    d = dict()
    for word in word_list:
        d[word] = d.get(word, 0) + 1
    return d


def histogram_new(word_list):
    pledge_list = get_pledge_list()
    hist_new = {}
    hist_new = histogram_old(pledge_list)
    return hist_new




def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. returns the list.
    """
    # Your code here.
    with open('pledge.txt', 'r') as fin:
        lines = fin.read()
        pledge_list = lines.split()

        punct =',.:'
    for idx in range(0, len(pledge_list)):
        # search punctuation marks (p_mark) in pledge_list list of words
        # and remove the punctuation if present
        if any((p_mark in punct) for p_mark in pledge_list[idx]):
            pledge_list[idx] = pledge_list[idx][:-1]

    return pledge_list


###############################################################################
def main():  # DO NOT CHANGE BELOW
    print(histogram_new(get_pledge_list()))

if __name__ == '__main__':
    main()
