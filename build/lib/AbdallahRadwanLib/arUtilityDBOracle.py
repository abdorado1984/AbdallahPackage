from typing import Tuple
import cx_Oracle
from AbdallahRadwanLib.arUtilityConst import ardbResult , ardbSettings
from AbdallahRadwanLib.arUtilityEnum import arEnumFetchType


class arOracle:
    __oraUsername, __oraPassword, __oraHost, __oraServiceName,_ConnectionString = "","","","",""
    __oraPort , __fetchCount = 1521, 10

    def __init__(self, dbSettings :ardbSettings) -> None:    
        self.__oraUsername    = dbSettings.dbUser
        self.__oraPassword    = dbSettings.dbPass
        self.__oraHost        = dbSettings.dbHost
        self.__oraServiceName = dbSettings.dbServiceName
        self.__oraPort        = dbSettings.dbPort
        self.__fetchCount     = dbSettings.dbFetchCount        
        self.__SetConnectionString()
        # print(f"Connection String : {self.__GetConnectionString()}\n")

    def __SetConnectionString(self) -> None:      
        self._ConnectionString = f"{self.__oraUsername}/{self.__oraPassword}@{self.__oraHost}:{self.__oraPort}/{self.__oraServiceName}"

    def __GetConnectionString(self) -> str:                
        return self._ConnectionString
    
    def openConn(self) -> Tuple[object,bool]:
        try:            
            LoConn = cx_Oracle.connect(self.__GetConnectionString())            
        except:
            LoConn = None
        finally:
            LbConnected = (LoConn != None)
        return LoConn , LbConnected
    
    def closeConn(self , AoConn :object) -> None:
        try:
            if (AoConn != None):
                AoConn.close()
        except:
            pass
    
    def __getColumns(self, AoCursor :object) -> dict:
        return { cd[0]:i for i , cd in enumerate(AoCursor.description) }
    
    def testConnection(self):
        dbResult = ardbResult()
        try:
            LoConn , dbResult.connected = self.openConn()
        except Exception as e:
            dbResult.isSuccess,dbResult.message = False,f"Exception : {e}"
        finally:
            self.closeConn(LoConn)        
        return dbResult
                    
    def fetchData(self, AsSQL :str, AtpValue :tuple, AoFetchType :arEnumFetchType = arEnumFetchType.ftMany) -> ardbResult:
        dbResult = ardbResult()
        try:            
            dbResult.message = "Open database connection"
            LoConn , dbResult.connected = self.openConn()
            if (dbResult.connected):
                dbResult.message = "Open cursor"
                LoCursor = LoConn.cursor()                
                dbResult.message = "Execute Data"
                LoCursor.execute(AsSQL,[AtpValue])
                dbResult.message = "Get list of column name"
                dbResult.columns = self.__getColumns(LoCursor)
                dbResult.message = "Fetch data ..."
                if (AoFetchType == arEnumFetchType.ftMany):
                    dbResult.rows = LoCursor.fetchmany(self.__fetchCount)
                else:
                    dbResult.rows = LoCursor.fetchall()
                dbResult.rowcount = LoCursor.rowcount
        except Exception as e:
            dbResult.isSuccess,dbResult.message,dbResult.columns,dbResult.rows,dbResult.rowcount = False,f"Exception : {e}",None,None,0
        finally:
            if (dbResult.connected):
                LoCursor.close()                
            self.closeConn(LoConn)        
        return dbResult
         
    def executeData(self, AoSQLList :list[str], AoValueList :list[tuple]) -> ardbResult:
        '''
            Cursor.execute(SQL as str)
            Cursor.execute(SQL as str, Row as tuple) # you can passing value by position or by name
            Cursor.executemany(SQL as str, Rows as List[tuple])
        '''
        dbResult = ardbResult()
        try:
            dbResult.message = "Open database connection"
            LoConn , dbResult.connected = self.openConn()
            if (dbResult.connected):
                dbResult.message = "Open cursor"
                LoCursor = LoConn.cursor()
                dbResult.message = "Execute Data"
                for LsSQL in AoSQLList:
                    LtpValue = AoValueList[AoSQLList.index(LsSQL)]
                    LoCursor.execute(LsSQL, (LtpValue))                    
                LoConn.commit()                
                dbResult.rowcount = LoCursor.rowcount
                dbResult.isSuccess = True
        except Exception as e:
            if (dbResult.connected):
                LoConn.rollback()
            dbResult.isSuccess,dbResult.message,dbResult.rowcount = False,f"Exception : {e}",0            
        finally:
            if (dbResult.connected):
                LoCursor.close()                
            self.closeConn(LoConn) 
        return dbResult
        

    def CallProc(self, AsName :str, AoParams :list) -> ardbResult:
        dbResult = ardbResult()
        try:            
            dbResult.message = "Open database connection"
            LoConn , dbResult.connected = self.openConn()
            if (dbResult.connected):
                dbResult.message = "Open cursor"
                LoCursor = LoConn.cursor()                
                dbResult.message = "Execute Data"
                LoCursor.callproc(AsName , AoParams)
                dbResult.isSuccess,dbResult.message = True, "Procedure Exceuted ..."                 
        except Exception as e:
            dbResult.isSuccess,dbResult.message,dbResult.columns,dbResult.rows,dbResult.rowcount = False,f"Exception : {e}",None,None,0
        finally:
            if (dbResult.connected):
                LoCursor.close()                
            self.closeConn(LoConn)        
        return dbResult

    def CallFun(self, AsName :str, AoParams :list, AoType :type) -> ardbResult:
        dbResult = ardbResult()
        try:            
            dbResult.message = "Open database connection"
            LoConn , dbResult.connected = self.openConn()
            if (dbResult.connected):
                dbResult.message = "Open cursor"
                LoCursor = LoConn.cursor()                
                dbResult.message = "Execute Data"
                dbResult.data = LoCursor.callfunc(AsName , AoType, AoParams)                
                dbResult.isSuccess,dbResult.message = True, "Function Exceuted ..."                 
        except Exception as e:
            dbResult.isSuccess,dbResult.message,dbResult.columns,dbResult.rows,dbResult.rowcount = False,f"Exception : {e}",None,None,0
        finally:
            if (dbResult.connected):
                LoCursor.close()                
            self.closeConn(LoConn)        
        return dbResult