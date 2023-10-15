from typing import List

class Reference_point:
    def __init__(self,
        params: List[float],
        value: float):

        self.params: List[float] = params
        self.value: float = value

    def get_params(self) -> List[float]:
        return self.params
 
    def get_value(self) -> float:
        return self.value
  
    def get_dimension(self) -> int:
        return len(self.params)    