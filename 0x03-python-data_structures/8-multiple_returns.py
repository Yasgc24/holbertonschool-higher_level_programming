#!/usr/bin/python3
def multiple_returns(sentence):
    sentencel = len(sentence)
    if sentencel == 0:
        firstrchar = None
    else:
        firstchar = sentence[0]
    return (sentencel, firstchar)
