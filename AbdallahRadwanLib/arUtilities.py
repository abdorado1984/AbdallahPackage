class arUtility:    
    def GetRandomNumber(self, AiFrom :int=1, AiTo :int=100) -> int:
        import random
        return random.randrange(start=AiFrom, stop=AiTo)