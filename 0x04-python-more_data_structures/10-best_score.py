#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        new_dictionary = [(value, key) for key, value in a_dictionary.items()]
        return(max(new_dictionary)[1])
