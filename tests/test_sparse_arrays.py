'''TODO
'''

from src.sparse_arrays import matchingStrings

def test_one():
    assert matchingStrings(['aba','baba','aba','xzxb'],['aba','xzxb','ab']) == [2,1,0]

def test_two():
    assert matchingStrings(['def','de','fgh'],['de','lmn','fgh']) == [1,0,1]

def test_three():
    assert matchingStrings(['abcde','sdaklfj','asdjf','na','basdn','sdaklfj','asdjf','na','asdjf','na','basdn','sdaklfj','asdjf'],['abcde','sdaklfj','asdjf','na','basdn']) == [1,3,4,3,2]
