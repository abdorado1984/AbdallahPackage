from os import path , getcwd , stat

class arFile:        
    def GetCurrentDirectory(self, AsFolder :str = "") -> str:
        LsCurrPath = getcwd()
        if (AsFolder != ""):
            LsCurrPath = path.join(LsCurrPath, AsFolder)
        return LsCurrPath

    def IsFileExist(self , AsFilePath :str) -> bool:
        return path.exists(AsFilePath)

    def IsEmptyFile(self , AsFilePath :str) -> bool:
        return (stat(AsFilePath).st_size == 0)

    def CreateFile(self, AsFilePath :str, AsText :str = "") -> bool:
        try:
            file = open(AsFilePath, "w")
            file.write(AsText)                                               
            return True
        except Exception as e:
            print(f"Error creating file : {e}")
            return False      
