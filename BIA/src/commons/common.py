from typing import List

class Common:
    @staticmethod
    def check_kwargs(
        error_text: str,
        allowed_keys: List[str] = [],
        **kwargs) -> None:
        
        len_args_keys = len(kwargs.keys())
        len_allowed_keys = len(allowed_keys)
        if(len_args_keys < len_allowed_keys):
            raise ValueError(f"Not all arguments have been entered to {error_text}.")
        elif(len_args_keys > len_allowed_keys):
            raise ValueError(f"Too much arguments have been entered to {error_text}.")
        for key in kwargs.keys():
            if key not in allowed_keys:
                raise ValueError(f"Arguments {key} is not allowed in {error_text}.")