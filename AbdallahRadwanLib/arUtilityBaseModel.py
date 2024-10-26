from pydantic import BaseModel , Field
from pydantic.json_schema import SkipJsonSchema

class OutputModel(BaseModel):
    isSuccess :bool = False
    message   :str = ""
    data      :object = {}

class CommonMessageModel(BaseModel):
    subject :str
    message :str

class TokenPayloadModel(BaseModel):            
    user :str
    sub  :str    
    iss  :str    
    env  :str    
    cre  :str
    exp  :str
    
class TokenModel(BaseModel):
    access_token :str
    refresh_token :str
    token_type :str
    created_At :str #datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    expires_in :str

class TestModel(BaseModel):    
    item :str
    price :int