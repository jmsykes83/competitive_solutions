'''TODO'''
from src.counting_valleys import countingValleys

def test_one():
    assert countingValleys(8,'UDDDUDUU') == 1

def test_two():
    assert countingValleys(12,'DDUUDDUDUUUD') == 2