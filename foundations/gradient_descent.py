class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places

        old_val = init
        for iter in range(iterations):
            old_val = old_val - learning_rate * ( 2 * old_val)
            
        return round(old_val, 5)
