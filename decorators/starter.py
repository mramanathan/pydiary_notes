# _*_ coding: utf-8 _*_

#!/usr/bin/env/python


def jewel(crown):

    ''' Novice decorator function '''
    
    def necklace(*args, **kwargs):
        print("necklace is always below the crown {}".format(jewel.__name__))
        return crown(*args, **kwargs)
    return necklace

def funcLog(crowns):

    ''' Real world application '''

    import logging
    logging.basicConfig(filename='{}.log'.format(crowns.__name__), level=logging.INFO)

    def necklace(*args, **kwargs):
        logging.info("Ran with args: {}, and kwargs: {}".format(args, kwargs))
        print("necklace is always below the crown {}".format(jewel.__name__))
        return crowns(*args, **kwargs)
    return necklace
    


@jewel
def king():
    print("King was crowned without necklace")

@jewel
def queen(orn1, orn2):
    print("Queen was crowned with ({}, {})".format(orn1, orn2))


@funcLog
def king():
    print("King was crowned without necklace")

@funcLog
def queen(orn1, orn2):
    print("Queen was crowned with ({}, {})".format(orn1, orn2))


king()
queen('pearl-chain', 'gold-chain')
