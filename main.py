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
            if exponent == 1:
                result += f"x_{i}"
            elif exponent == 0:
                continue
            else:
                result += f"x_{i}^{exponent}" 
        return result
    
def is_addable(m1: Monomial, m2: Monomial) -> bool:
    return m1.k == m2.k

def add_to_monomial(m1: Monomial, m2: Monomial) -> Monomial:
    if not is_addable(m1,m2):
        return None
    
    result_coeficient = m1.a + m2.a
    
    return Monomial(a=-6, k=[1,4,,8])

def multiply_2_monomial(m1: Monomial, m2: Monomial) -> Monomial:
    result_coeficient = m1.a * m2.a
    result_exponents = []

    for i in range(len(m1.k)):
        result_exponents.append(m1.k[i] + m2.k[i])

    return Monomial(a=result_coeficient, k=result_exponents)