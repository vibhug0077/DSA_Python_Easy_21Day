from typing import List

class Solution_bf:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for v1 in range(n - 1):
            for v2 in range(v1 + 1, n):   # start after v1 to avoid same index + duplicates
                if nums[v1] + nums[v2] == target:
                    return [v1, v2]
        return []  # in case no pair is found

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d ={}
        for ind, num in enumerate(nums):
            if target - num in d:
                return(d[target - num], ind)
            else:
                d[num] =ind
        return []  # in case no pair is found

def main():
    l = [1, 2, 3, 4, 5]
    target = 9

    sol = Solution()
    result = sol.twoSum(l, target)

    print("nums =", l)
    print("target =", target)
    print("output indices =", result)

    if result:
        i, j = result
        print(f"values = {l[i]} + {l[j]} = {l[i] + l[j]}")


if __name__ == "__main__":
    main()

