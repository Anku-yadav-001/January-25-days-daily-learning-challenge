class Solution:
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            
            if nums[start] == nums[mid] == nums[end]:  
                start += 1
                end -= 1
                continue
            
            if nums[start] <= nums[mid]:  
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] <= nums[end]:  
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return False

nums = [2, 5, 6, 0, 0, 1, 2]
target = 0

solution = Solution()
output = solution.search(nums, target)
print(output)
