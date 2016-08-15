#!/usr/bin/env python3
# HW08_ch11_ex02d.py
# (1) Write a more concise version of invert_dict_old.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Update print_hist_new from HW08_ch11_ex02b.py to be able to print
# a sorted version of the dict (print key/value pairs from 0 through the
# largest key values, (and those in between))
# Ex. If d = {1:["this, that"], 3: ["the"]}, it prints:
#    '1: ["this", "that"]'
#    '2:'
#    '3: ["the"]'
###############################################################################
# Imports

# Body
def invert_dict_old(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

def invert_dict_new(d):
    inverse = dict()
    for key in d:
        inverse.setdefault(d[key], []).append(key)
    return inverse


def print_hist_newest(d):
    d_max = max(d)
    for d_key in range(1, d_max+1):
        if d_key in d:
            print(d_key, d[d_key])
        else:
            print(d_key)


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

        punct = ',.:'
    for idx in range(0, len(pledge_list)):
        # search punctuation marks (p_mark) in pledge_list list of words
        # and remove the punctuation if present
        if any((p_mark in punct) for p_mark in pledge_list[idx]):
            pledge_list[idx] = pledge_list[idx][:-1]

    return pledge_list


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():  # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    pledge_invert = invert_dict_new(pledge_histogram)
    print_hist_newest(pledge_invert)

if __name__ == '__main__':
    main()
