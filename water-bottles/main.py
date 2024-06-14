# https://leetcode.com/problems/water-bottles/

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        currentFull = numBottles
        currentEmpty = 0
        totalDrink = 0

        while currentFull > 0:
            # Drink
            totalDrink += currentFull
            currentEmpty += currentFull
            # Exchange
            currentFull = currentEmpty // numExchange
            currentEmpty = currentEmpty % numExchange
        return totalDrink
