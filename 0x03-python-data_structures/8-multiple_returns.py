#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        firstrchar = None
    else:
        firstchar = sentence[0]
    return (len(sentence), firstchar)
