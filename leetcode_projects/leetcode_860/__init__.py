from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hand_money = defaultdict(int)
        lemon_price = 5
        for money in bills:
            diff = money - lemon_price
            while diff > 0:
                if diff >= 10 and hand_money[10] > 0:
                    diff -= 10
                    hand_money[10] -= 1
                elif diff >= 5 and hand_money[5] > 0:
                    diff -= 5
                    hand_money[5] -= 1
                else:
                    break
            if diff == 0:
                hand_money[money] += 1
            else:
                return False
        return True

