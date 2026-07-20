class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        runtime: 0 ms, memory: 20.30 mB
        """
        nums[:] = list(dict.fromkeys(nums)) # this is the new way of doing it to do it in place.
        # could do something like this too, 
        # nums[:] = sorted(list(set(nums))) 
        # nums[:] is the whole list, set() removes duplicates, back to a list(), then sorted() to put it in order
