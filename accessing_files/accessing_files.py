#!/usr/bin/env python

import os, sys

def list_of_directory(list_of_directory):

    for directory in list_of_directory:
        get_filename(directory)
    return

def test_modifiction(directory):

    prior_state = get_filename(directory)
    after_state = get_filename(directory)

    for k in after_state.keys():
        if prior_state[k][0] == after_state[k][0]:
            print "no update necessary"
        else:
            print "update necessary"

def get_filename(directory):
    '''
    get_filename(directory):

    This function takes a directory and records the last modification time
    (since epoch) and size of the file.

    Return:
    It returns a dictionary with the file name is the key, modification time
    and size.

    {'filename': [modification_time, size], ... }
    '''
    
    file_dictionary = {}
    
    for filename in os.listdir(directory):
        full_path = directory + filename

        #ToDo use regex instead
        if filename == '.DS_Store' or filename == '.git':
            continue
        else:
            #print filename, full_path, os.path.getmtime(full_path), os.path.getsize(full_path)
            file_dictionary[filename] = [os.path.getmtime(full_path),
                                         os.path.getsize(full_path)]

    print file_dictionary
    return file_dictionary

def main():

    # get_filename("/Users/Kelechi/bin/utilities/")
    #list_of_directory(['/Users/Kelechi/programming/', '/Users/Kelechi/bin/'])
    test_modifiction("/Users/Kelechi/bin/utilities/")

if __name__ == '__main__':
    main()
