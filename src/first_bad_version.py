# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
        
    def firstBadVersion(self, n: int) -> int:
        def binary_search(first:int,end:int)-> int:
            if first < end:
                mid = first + ((end-first) / 2)
                if isBadVersion(mid):
                    return binary_search(first,mid)
                else:
                    return binary_search(mid+1,end)
            return int(first)
        return binary_search(1,n)