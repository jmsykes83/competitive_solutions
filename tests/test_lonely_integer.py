''' Test for the lonely integer challenge on hacker rank
'''
from src.lonely_integer import lonelyinteger

def test_one():
    '''Test to see if lonelyinteger return the number for
    on the data set'''
    assert lonelyinteger([1,2,3,4,3,2,1]) == 4
