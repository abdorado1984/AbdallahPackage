import jwt 
from cryptography.fernet import Fernet
from typing import Tuple
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from arUtilityEnum import arEnumEncryptionType
from arUtilityConst import jwt_SecretKey, jwt_Algorithm

class arEncryption:
    def GenerateToken(self, payload :dict) -> str:
        try:        
            token = jwt.encode(payload , jwt_SecretKey, jwt_Algorithm)
        except Exception as e:
            token = ""
            errorMessage = f"Error : {e}"
        return token   

    def ReadToken(self, token :str) -> dict:
        payload = {}
        try:                           
            payload = jwt.decode(token , jwt_SecretKey, jwt_Algorithm, options={"verify_aud": False})
        except Exception as e:
            payload = {}
            errorMessage = f"Exception : {e}"
        return payload   

    def __EncHash(self,text :str) -> str:        
        try:
            value = str(hash(text))
        except:
            value = ""            
        return value
            
    def __EncFernet(self,text :str) -> Tuple[str,str]:#using salt 
        try:            
            value,key = "",""
            key = Fernet.generate_key()  
            fernet = Fernet(key)
            value = fernet.encrypt(text.encode()).decode()                        
            key = key.decode()            
        except:
            value,key = "",""
        return value,key

    def __DecFernet(self,text :str, key :str) -> str:
        try:
            value = ""
            value = Fernet(key).decrypt(text).decode()
        except:
            value = ""
        return value    
    
    def __EncAES(self,text :str) -> Tuple[str,str,str,str]:#using salt         
        try:    
            value,key,tag,nonce = "","","",""
            # AES requires a key of 16, 24, or 32 bytes        
            key = get_random_bytes(16)  # Generate a random 16-byte key 
            cipher = AES.new(key, AES.MODE_EAX)
            nonce = cipher.nonce
            value, tag = cipher.encrypt_and_digest(text.encode("ascii"))        
            value,key,tag,nonce = value.hex(), key.hex(), tag.hex(), nonce.hex()
        except Exception as e:
            error = f"EncAES : {e}"
            value,key,tag,nonce = "","","",""
        return value,key,tag,nonce

    def __DecAES(self,text :str, key :str, tag :str, nonce :str) -> str:        
        try:
            value = ""
            text,key,tag,nonce = bytes.fromhex(text),bytes.fromhex(key),bytes.fromhex(tag),bytes.fromhex(nonce)

            cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
            value = cipher.decrypt(text)   
            cipher.verify(tag)   
            value = value.decode("ascii")                 
        except Exception as e:
            error = f"DecAES : {e}"
            value = ""
        return value   
    
    def encodeText(self,text :str, encType: arEnumEncryptionType) -> Tuple[str,str,str,str]:        
        value,key,tag,nonce = "","","",""
        match encType: 
            case arEnumEncryptionType.etFernet:
                value,key = self.__EncFernet(text)
            case arEnumEncryptionType.etAES:
                value,key,tag,nonce = self.__EncAES(text)                
        return value,key,tag,nonce
            
    def decodeText(self,text :str, key :str, tag :str, nonce :str, encType: arEnumEncryptionType) -> str:
        value = ""
        match encType: 
            case arEnumEncryptionType.etFernet:
                value = self.__DecFernet(text, key)
            case arEnumEncryptionType.etAES:
                value = self.__DecAES(text, key, tag, nonce)                    
        return value
