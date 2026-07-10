class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        runtime: 0 ms, memory: 19.31 mB
        """
        del nums1[m:]
        del nums2[n:]
        nums1.extend(nums2)
        nums1.sort()
