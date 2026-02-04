from typing import List

class solution_bf:
    def maxProfit(self, price:List[int])-> int:
        n = len(price)
        best =0

        for i in range(n):
            for j in range(i+1,n):
                profit= price[j]- price[i]
                if profit > best:
                    best = profit
                
        return best

class solution:
    def maxProfit(self, prices:List[int])->int:
        min_pr = float("inf")
        max_pr = 0
        for price in prices:
            if price < min_pr:
                min_pr = price
            profit = price - min_pr

            if profit > max_pr:
                max_pr = profit
        return max_pr

def main():
    prices = [7,1,5,3,6,4]

    sol = solution()
    result = sol.maxProfit(prices)

    print("Price =", prices)
    
    print("Maximum Profit =", result)


if __name__ == "__main__":
    main()
    

