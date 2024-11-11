#from pydantic.json_schema import SkipJsonSchema
from pydantic import BaseModel #, Field
from typing import Optional
from datetime import datetime

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
    refresh_token :Optional[str] = None
    token_type :str = "Bearer"
    created_at :datetime
    expires_in :datetime 

class TestModel(BaseModel):    
    name        :str  # Required field
    description :Optional[str] = None  # Optional field
    price       :Optional[float] = 0.0  # Optional with default value