#!/usr/bin/env python3
# HW08_ch11_ex01
# Write a function that reads the words in words.txt and stores them as keys
# in a dictionary (returning the dictionary). It doesn’t matter what the
# values are. Then you can use the in operator as a fast way to check whether
# a string is in the dictionary.
###############################################################################
# Imports


# Body
def store_to_dict(file_name):
    with open(file_name,'r') as fin:
        lines = fin.readlines()
    value = 0
    wrd_dict = {}
    for line in lines:
      #  set default values  for every key
        wrd_dict[line.strip()] = value
        value +=1
    return wrd_dict


###############################################################################
def main():  # DO NOT CHANGE BELOW
    words_dict = store_to_dict('words.txt')
    #print(words_dict)
    if "this" in words_dict:
        print("Yup.")
    if "qwertyuiop" in words_dict:
        print("Hmm.")

if __name__ == '__main__':
    main()
