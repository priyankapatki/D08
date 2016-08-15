#!/usr/bin/env python3
# HW08_ch11_ex02b
# This borrows from exercise two in the book.
# Dictionaries have a method called keys that returns the keys of the
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical
# order.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
###############################################################################
# Imports


# Body
def print_hist_old(h):
    for c in h:
        print(c, h[c])


def print_hist_new(h):
    for h_key in sorted(h):
        print(h_key, h[h_key])


pledge_histogram = {}


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
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
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():
    """ Calls print_hist_new with the appropriate arguments to print the
    histogram of pledge.txt.
    """
    print_hist_new(histogram_new(get_pledge_list()))

if __name__ == '__main__':
    main()
