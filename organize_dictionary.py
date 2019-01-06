#!/usr/bin/env python

from pprint import pprint

# HELPER FUNCTIONS --------------------------------------------------------------------------------

def append_to_dictionary(text):
    with open('./dictionary/{}'.format(len(text)), 'a') as dict_file:
        dict_file.write(text)

# MAIN --------------------------------------------------------------------------------------------

size_counts = {}
if __name__ == '__main__':
    with open('./dictionary_raw', 'r') as raw_dict:
        for i, line in enumerate(raw_dict):
            append_to_dictionary(line)

            # Create a summary of the dictionary elements created
            if not size_counts.get(len(line), 0):
                size_counts[len(line)] = 1
            else:
                size_counts[len(line)] = size_counts[len(line)] + 1
pprint(size_counts)
