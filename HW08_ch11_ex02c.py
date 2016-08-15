#!/usr/bin/env python3
# HW08_ch11_ex02c.py
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
###############################################################################
# Imports


# Body
def reverse_lookup_old(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError


def reverse_lookup_new(d, v):
    reverse_new = {}

    for k in d:
        d_val = d[k]
        if d_val not in reverse_new:
            reverse_new[d_val] = [k]
        else:
            reverse_new[d_val].append(k)
    if v in reverse_new:
        return reverse_new[v]
    else:
        return []


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
def main():   # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    print(reverse_lookup_new(pledge_histogram, 1))
    print(reverse_lookup_new(pledge_histogram, 9))
    print(reverse_lookup_new(pledge_histogram, "Python"))

if __name__ == '__main__':
    main()
