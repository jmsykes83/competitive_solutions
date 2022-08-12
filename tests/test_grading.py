'''Hacker Rank: Grade'''
from src.grading import gradingStudents


def test_one():
    '''test:one'''
    assert gradingStudents([4,73,67,38,33][1:]) == [75,67,40,33]
