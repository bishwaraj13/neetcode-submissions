# Every smash is effectively subtracting one stone’s weight from another. 
# final_stone = ±stones[0]±stones[1]±stones[2]…

# So instead of simulating all possible smash orders, we can decide for each stone:
# put it in group A → treat it as +stone
# put it in group B → treat it as -stone

# Then we want to minimize:
# ∣sum(A)−sum(B)∣

# This is a minimum subset sum difference in disguise
# sum(A) + sum(B) = total
# For |sum(A)-sum(B)| to be less, sum(A) should be <= total//2

# This problem then reduces to subset sum where target approximately <= total//2

# SO we explore all the ways where subset sum <= total//2 and then take max of it
# Taking max of it will make sure ∣sum(A)−sum(B)∣ is minimum

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) // 2
        memo = {}

        def dfs(i, current_sum):
            # all stones have been considered
            if i == len(stones):
                return current_sum

            if (i, current_sum) in memo:
                return memo[(i, current_sum)]

            # skip the current stone
            best = dfs(i + 1, current_sum)

            # take the current stone if we stay within target
            if current_sum + stones[i] <= target:
                best = max(
                    best,
                    dfs(i + 1, current_sum + stones[i])
                )

            memo[(i, current_sum)] = best
            return best

        # largest subset sum <= total // 2
        best_subset = dfs(0, 0)

        # return sum(group A) - sum(group B)
        return (sum(stones) - best_subset) - best_subset
        