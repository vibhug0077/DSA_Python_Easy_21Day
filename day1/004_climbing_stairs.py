class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        a, b = 1, 2  # ways(1), ways(2)

        for _ in range(3, n + 1):
            print("Value before assignment of a :", a )
            a = b
            print("Value after assignmentof a:", a )
            print("Value before assignment of b:", b)
            b = a + b  # shift forward
            print("Value after assignment of b:", b)

        return b
    
def main():
    n = 4
    v_obj = Solution()
    print("The N values are :",v_obj.climbStairs(n))
    
if __name__ == "__main__":
    main()
