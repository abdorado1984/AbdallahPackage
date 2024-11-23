from enum import Enum

class arEnumConfigType(Enum):
    connStrs   = "connectionStrings"
    defEnv     = "DefaultEnviroment"
    defConnStr = "DefaultConnectionString"    
    enableEcho = "EnableEcho"
    serverIP   = "ServerIP"
    serverPort = "ServerPort"
    fetchCount = "FetchCount"

class arEnumEncryptionType(Enum):
    etHash   = "hash -> Hashing is a one-way functio"    
    etFernet = "Fernet -> symmetric encryption"
    etAES    = "AES -> Advanced Encryption Standard"   
    # etToken  = "Bearer Token" 

class arEnumFetchType(Enum):
    ftOne  = 1
    ftMany = 2
    ftAll  = 3   