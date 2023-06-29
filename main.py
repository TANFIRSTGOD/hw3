class Monomial:
    def __init__(self, a, k:list) -> None:
        self.a = a
        self.k = k

    def is_monomial(self) -> bool:
        for exponent in self.k:
            if not(isinstance(exponent, int) and exponent >= 0):
                return False
        return True
    
    def file_max_exponent(self):
        return max(self.k)
    def is_constant(self) -> bool:
        return sum(self.k) == 0
    
    def find_number_of_vars(self) -> int:
        if self.is_constant():
            return 0
        return len(self.k)
    
    def __str__(self):
        result = ""
        result += str(self.a)
        for i,exponent in enumerate(self.k):
            result += f"x_{i}^{exponent}"
        return result