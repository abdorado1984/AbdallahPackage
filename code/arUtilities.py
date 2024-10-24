class arutility:
    def GetRandomNumber(self, min :int, max:int) -> int:
        import random
        return random.randrange(min, max)