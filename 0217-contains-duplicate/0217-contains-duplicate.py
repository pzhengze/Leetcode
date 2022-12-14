class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = set()
        for n in nums:
            if n in count:
                return True
            else:
                count.add(n)