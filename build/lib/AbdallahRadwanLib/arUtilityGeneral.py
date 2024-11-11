from datetime import datetime , timedelta
from AbdallahRadwanLib.arUtilityEncryption import arEncryption, arEnumEncryptionType
from AbdallahRadwanLib.arUtilityConst import jwt_ExpireHours
from typing import Tuple
from uuid import uuid4

class arUtility:    
    def GetRandomNumber(self, AiFrom :int=1, AiTo :int=100) -> int:
        import random
        return random.randrange(start=AiFrom, stop=AiTo)
    
    def GetCurrentDatetime(self) -> datetime:        
        return datetime.now()
    
    def GetCurrentTimestamp(self) -> float:        
        return datetime.now().timestamp()
    
    def GetDatefromTimestamp(self, stamp :float) -> datetime:
        return datetime.fromtimestamp(stamp)
    
    def GetTimestampfromDate(self, dt :datetime) -> float:        
        return dt.timestamp()
        
    def EncryptDate(self, dt) -> str:
        Enc = arEncryption()
        return Enc.encodeText(str(dt), arEnumEncryptionType.etAES)        
        
    def GetTimestampCurDateAndExpired(self) -> Tuple[str,str]:
        dt = self.GetCurrentDatetime()                
        ex = dt + timedelta(hours=jwt_ExpireHours)                                
        createdAt,expireIn = str(int(self.GetTimestampfromDate(dt))), str(int(self.GetTimestampfromDate(ex)))
        return createdAt,expireIn
    
    def GetDateAndExpiredFromTimestamp(self,dt :str,ex :str) -> Tuple[datetime|datetime]:
        if ( (dt == None) | (ex == None) ):
              return None,None        
        dtValue,exValue = float(dt),float(ex)
        createdAt,expireIn = self.GetDatefromTimestamp(dtValue),self.GetDatefromTimestamp(exValue)        
        return createdAt,expireIn
    
    def IsExpiredDate(self, dt :str) ->bool :        
        if (dt == None):
            return True        
        try:                    
            dtValue = datetime.strptime(dt,"%Y-%m-%d %H:%M:%S")
            IsExpired = (dtValue < datetime.now())
        except:
            IsExpired = False
        return IsExpired

    def GetGUID(self, removeDash :bool) -> str:
        value = str(uuid4())
        if (removeDash):
            value = value.replace("-","")
        return value