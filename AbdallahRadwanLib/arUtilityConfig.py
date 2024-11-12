from AbdallahRadwanLib.arUtilityFile import arFile
from AbdallahRadwanLib.arUtilityEnum import arEnumConfigType
from AbdallahRadwanLib.arUtilityConst import ardbResult , ardbSettings
from AbdallahRadwanLib.arUtilitySettings import BasicSettings , VariableSettings

class arConfig:      
    __ConfigFileName, __ConfigFilePath = "Settings.json" , ""     
    __ConfigJsonData = {}
    __DbSettings = None

    __instance = None

    @staticmethod
    def CreateInstance():
        if (arConfig.__instance == None):
            arConfig.__instance = arConfig()
        return arConfig.__instance
    
    def __init__(self) -> None:    
        # print(f"Create Config : ")    
        self.CreateSettingFile()        
        self.__SetDbSettings()          
        

    def __SetConfigFilePath(self):
        fileUtility = arFile()
        self.__ConfigFilePath = fileUtility.GetCurrentDirectory(self.__ConfigFileName)        

    def __AddNewSetting(self, dictBasicData :dict, subKey :str, subValue :object):
        IsExistItem = False
        try:        
            for mainKey,mainValue in dictBasicData.items():
                if (mainKey == subKey):                
                    if (subValue != None):
                        IsExistItem = True                    
                        break                    
            if (not IsExistItem):
                dictBasicData.update( {subKey : subValue} )
        except Exception as e:
            print(f"__AddNewSetting.Exception : {e}")

    def __GetBasicData(self) -> dict:        
        import json
        dictBasicData    = BasicSettings
        dictVariableData = VariableSettings
        fileUtility = arFile()
        if (fileUtility.IsFileExist(self.__ConfigFilePath)):
            if (not fileUtility.IsEmptyFile(self.__ConfigFilePath)):
              file = open(self.__ConfigFilePath , "+r")            
              dictBasicData = json.load(file)              
              file.seek(0)
        else:            
            fileUtility.CreateFile(self.__ConfigFilePath)

        return dictBasicData, dictVariableData
    
    def __SetConfigJsonData(self):        
        result = ""
        try:                                    
            self.__ConfigJsonData, dictVariableData  = self.__GetBasicData()                                                            
            for Key,Value in dictVariableData.items():
                self.__AddNewSetting(self.__ConfigJsonData,Key,Value)            
            # Serializing json            
            import json
            JsonData = json.dumps(self.__ConfigJsonData, indent=4)
            fileUtility = arFile() 
            fileUtility.CreateFile(self.__ConfigFilePath, JsonData)
        except Exception as e:            
            result =""
            errorMsg = f"__SetConfigJsonData.Exception : {e}"
            print(errorMsg)

    def __SetDbSettings(self) -> None:        
        self.__DbSettings = ardbSettings()       
        self.__DbSettings.dbAlias = self.GetConfigValue(arEnumConfigType.defConnStr)
        self.__DbSettings.dbFetchCount =  self.GetConfigValue(arEnumConfigType.fetchCount)        
        if (len(self.__DbSettings.dbAlias) > 0):            
            connStrs = self.GetConfigValue(arEnumConfigType.connStrs)            
            try:                
                for connStr in connStrs :                    
                    connStrName = connStr.get("alias")                            
                    if (connStrName == self.__DbSettings.dbAlias):                           
                        self.__DbSettings.dbType        = connStr.get("type")
                        self.__DbSettings.dbName        = connStr.get("name")
                        self.__DbSettings.dbUser        = connStr.get("userName")
                        self.__DbSettings.dbPass        = connStr.get("password")
                        self.__DbSettings.dbHost        = connStr.get("host")                        
                        self.__DbSettings.dbPort        = connStr.get("port")
                        self.__DbSettings.dbService     = connStr.get("service")
                        break
            except Exception as e:
                errorMsg = f"__SetDbSettings.Exception : {e}"
                print(errorMsg)
        
    def CreateSettingFile(self):        
        self.__SetConfigFilePath()                
        self.__SetConfigJsonData()  

    def GetConfig(self, key :str) -> object:
        try:
            result = self.__ConfigJsonData.get(key)
        except Exception as e:            
            errorMsg = f"GetConfig.Exception : {e}"
            result = ""            
        return result
    
    def GetConfigValue(self, Enumkey :arEnumConfigType) -> object:
        # print(f"Enumkey : {Enumkey.name} : {Enumkey.value}")
        return self.GetConfig(Enumkey.value)
        
    def GetDbSettings(self) -> object:
        return self.__DbSettings
    
    @classmethod
    def ClassMethodReturnInstance(cls):
        return cls()        

config = arConfig.CreateInstance()