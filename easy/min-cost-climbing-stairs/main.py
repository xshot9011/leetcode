class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 1 100 1 1 1 0 | 
        # 1 100 1(pointer) [1 1] 0 | 1 |||||| 1 2 3 [1*(4) 1] -> 1 2 3 4 1 cost[len(cost)-1]
        # 1 100 [1 1] 1 0 | 2 |||||| 1 2 [1*(3) 1] 1 
        # 1 [100 1] 1 1 0 | 3 |||||| 1 [100*(2) 1] 1 1 
        # [1 100] 1 1 1 0 | 4 |||||| [1*(1) 100] 1 1 1
        # top to bot, or bot to top is ok
        cost.append(0)
        for i in range(len(cost) -3, -1, -1):
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
            # print(f'After cost({i}): {cost}')
        return min(cost[0], cost[1])
