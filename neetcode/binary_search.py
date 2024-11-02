# Binary Search Solutions

class Solutions:
	# Solution Functions

        def search(self, nums: List[int], target: int) -> int:
                '''Binary Search in a list

                Space Complexity: O(1) -> Pointers
                Time Complexity: O(log n) -> Binary Search

                Args:
                        nums (list): Iterable of numbers
                        target (int): Number to find

                Returns:
                        mid (int): Index of solution
                '''
                l, r = 0, len(nums) - 1

                while l <= r:
                        mid = (l + r) // 2

                        if nums[mid] == target:
                                return mid
                        elif nums[mid] < target:
                                l = mid + 1
                        else:
                                r = mid - 1
                return -1
