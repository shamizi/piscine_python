def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try :
        if len(height) != len(weight):
            raise ValueError("Height and weight lists must have the same length.")
        res =[]
        for h,w in zip (height, weight):
            if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
                raise TypeError("Height and weight must be integers or floats.")
            if h <= 0 or w <= 0:
                raise ValueError("Height and weight must be higher than 0.")
            res.append(w / (h * h))
        return res
    except Exception as e:
        print("Error:", e)
        return []
            
        
#raise typeError()
def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        if not isinstance(limit, float) and not isinstance(limit, int):
            raise TypeError(TypeError("Limit must be integers or floats."))
        res = []
        for x in bmi:
            if not isinstance(x, (float, int)):
                raise TypeError(TypeError("BMI must be integers or floats."))
            res.append(x > limit)
        return res
    except Exception as e:
        print("Error:", e)
        return []