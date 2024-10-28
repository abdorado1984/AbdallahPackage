from pydantic import BaseModel , Field
from pydantic.json_schema import SkipJsonSchema
from typing import Optional

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
    name        :str  # Required field
    description :Optional[str] = None  # Optional field
    price       :Optional[float] = 0.0  # Optional with default value