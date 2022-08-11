'''
tEST: File for testing the camel_case project
'''

from src.three_month_prep_camel_case import set_string

def test_camelcase():
    '''
    camel case assertions
    '''
    assert set_string("S;M;plasticCup()") == "plastic cup"

def test_mobilephone():
    '''
    camel case assertions
    '''
    assert set_string("C;V;mobile phone") == "mobilePhone"

def test_coffeemachine():
    '''
    camel case assertions
    '''
    assert set_string("C;C;coffee machine") == "CoffeeMachine"

def test_largesoftwarebook():
    '''
    camel case assertions
    '''
    assert set_string("S;C;LargeSoftwareBook") == "large software book"

def test_whitesheetofpaper():
    '''
    camel case assertions
    '''
    assert set_string("C;M;white sheet of paper") == "whiteSheetOfPaper()"

def test_pictureframe():
    '''
    camel case assertions
    '''
    assert set_string("S;V;pictureFrame") == "picture frame"

def test_ipad():
    '''
    camel case assertions
    '''
    assert set_string("S;V;iPad") == "i pad"

def test_mousepad():
    '''
    camel case assertions
    '''
    assert set_string("C;M;mouse pad") == "mousePad()"

def test_codeswarm():
    '''
    camel case assertions
    '''
    assert set_string("C;C;code swarm") == "CodeSwarm"

def test_orangehighlighter():
    '''
    camel case assertions
    '''
    assert set_string("S;C;OrangeHighlighter") == "orange highlighter"
