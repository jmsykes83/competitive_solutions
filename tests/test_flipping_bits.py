
from src.flipping_bits import flippingBits

def test_one():
    assert flippingBits([3,2147483647,1,0]) == [2147483648, 4294967294, 4294967295]