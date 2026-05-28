class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Изначально минимальная цена — это цена первого дня
        min_price = prices[0]
        # Максимальная прибыль в начале равна 0
        max_profit = 0
        
        # Начинаем со второго дня (индекс 1)
        for i in range(1, len(prices)):
            current_price = prices[i]
            
            # 1. Считаем возможную прибыль сегодня
            potential_profit = current_price - min_price
            
            # 2. Если она больше максимальной — обновляем рекорд
            if potential_profit > max_profit:
                max_profit = potential_profit
                
            # 3. Обновляем минимальную цену, если нашли цену еще ниже
            if current_price < min_price:
                min_price = current_price
                
        return max_profit
        