from src.merge_two_sorted_list import Solution, ListNode


sol = Solution()
def test_one():
    '''Test One'''
    list1 = [1,2,4] 
    list2 = [1,3,4]
    assert sol.mergeTwoLists(list1,list2) == [1,1,2,3,4,4]

def test_two():
    '''Test Two'''
    list1 = []
    list2 = []
    assert sol.mergeTwoLists(list1,list2) == []

def test_three():
    list1 = []
    list2 = [0]
    assert sol.mergeTwoLists(list1,list2) == [0]