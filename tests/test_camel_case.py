'''
tEST: File for testing the camel_case project
'''

from src.three_month_prep_camel_case import get_camel_case

def test_camelcase():
    '''
    camel case assertions
    '''
    assert get_camel_case("S;M;plasticCup()") == "plastic cup"

def test_mobilephone():
    '''
    camel case assertions
    '''
    assert get_camel_case("C;V;mobile phone") == "mobilePhone"

def test_coffeemachine():
    '''
    camel case assertions
    '''
    assert get_camel_case("C;C;coffee machine") == "CoffeeMachine"

def test_largesoftwarebook():
    '''
    camel case assertions
    '''
    assert get_camel_case("S;C;LargeSoftwareBook") == "large software book"

def test_whitesheetofpaper():
    '''
    camel case assertions
    '''
    assert get_camel_case("C;M;white sheet of paper") == "whiteSheetOfPaper()"

def test_pictureframe():
    '''
    camel case assertions
    '''
    assert get_camel_case("S;V;pictureFrame") == "picture frame"
