class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        memory = {}
        ans = []

        for i in nums1:
            if i in memory:
                memory[i] += 1
            else:
                memory[i] = 1
        
        for i in nums2:
            if i in memory:
                memory[i] -= 1
                ans.append(i)
                if memory[i] == 0:
                    del memory[i]
        
        # Time: O(m+n)
        # Space: O(m+n)
        return ans

# What if the given array is already sorted? How would you optimize your algorithm?
## Using binary search Time: O(m*log(n))
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
## m + n No matter a + b = b + a, better than O(m * n) also a * b = b * a
## Using binary search Time: O(m*log(n))
### try to put minimize in (m) linear function
### try to put maximize in (n) log
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
## All implement techinque if non-sored, should be memorize thing. Saying that loading during some function during execute time.
