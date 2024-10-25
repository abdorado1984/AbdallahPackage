# to get a string like this run: openssl rand -hex 32
jwt_SecretKey = "0b0de311e50faaf5fc8181547644b83fa55caa1c32d025ea0ed72feeccb04be5"       
jwt_Algorithm = "HS256"
jwt_ExpireHours = 24

class ardbSettings:
    dbType :str = "" 
    dbAlias :str = "" 
    dbName :str = ""
    dbUser :str = ""
    dbPass :str = ""
    dbHost :str = ""
    dbServiceName :str = ""
    dbPort :int = 0
    dbFetchCount :int = 0

class ardbResult:
    connected :bool=False
    isSuccess :bool=False
    message   :str=""
    columns   :dict={}
    rows      :object=None
    rowcount  :int=0
    data      :object=None