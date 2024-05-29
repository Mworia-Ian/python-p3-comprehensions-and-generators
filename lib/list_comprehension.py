#!/usr/bin/env python3

def return_evens(num_list):
    return [nums for nums in num_list if (nums % 2 == 0)] 

pass

def make_exclamation(sentence_list):
    return [sentence.strip() + "!" for sentence in sentence_list] if sentence_list else []