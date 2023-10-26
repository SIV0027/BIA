from typing import List

class Reference_point:
    def __init__(self,
        params: List[float],
        value: float):

        self.params: List[float] = params
        self.value: float = value

    def __add__(self, other):
        other_params: List[float] = other.get_params()

        params: List[float] = []
        for i, param in enumerate(self.params):
            other_param: float = other_params[i]
            add: float = param + other_param
            params.append(add)

        add_point = Reference_point(params, None)
        return add_point

    def __sub__(self, other):
        other_params: List[float] = other.get_params()

        params: List[float] = []
        for i, param in enumerate(self.params):
            other_param: float = other_params[i]
            sub: float = param - other_param
            params.append(sub)

        sub_point = Reference_point(params, None)
        return sub_point
    
    def __mul__(self, other: float):
        params: List[float] = []
        for param in self.params:
            mul: float = other * param
            params.append(mul)

        mul_point = Reference_point(params, None)
        return mul_point

    def get_params(self) -> List[float]:
        return self.params
 
    def get_value(self) -> float:
        return self.value
  
    def get_dimension(self) -> int:
        return len(self.params)