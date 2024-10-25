from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
from pathlib import Path
dirPath = str(Path(__file__).resolve().parent.parent)
sys.path.append(dirPath)
from arUtilityConfig import arConfig
from arUtilityConst import ardbSettings

"""
    1. Create new engine
    2. create new declarative base
    3. base with metadata and assign engine
    4. create new session maker
    5. Inherit from new object from session maker
"""

# config = arConfigUtility()  
config   = arConfig.CreateInstance() 
dbSetting :ardbSettings = config.GetDbSettings()
dbType,dbAlias,dbName,dbUser,dbPass,dbHost,dbPort,dbService = dbSetting.dbType.upper(), dbSetting.dbAlias, dbSetting.dbName, dbSetting.dbUser, dbSetting.dbPass, dbSetting.dbHost, dbSetting.dbPort, dbSetting.dbServiceName

oracle_db_url = f"oracle+cx_oracle://{dbUser}:{dbPass}@{dbHost}:{dbPort}/{dbService}"
sqlite_db_url = f"sqlite:///{dirPath}\\Database\\SQLite\\{dbName}.db" 
mongo_db_url  = f"mongodb://{dbHost}:{dbPort}/"

if (dbType == "ORACLE"):
    default_db_url = oracle_db_url
elif (dbType == "SQLITE"):
    default_db_url = sqlite_db_url    
elif (dbType == "MONGODB"):
    default_db_url = mongo_db_url        
else:
    default_db_url = ""

print("Welcome to SqlAlchemy\n", end=" ")
print(f"\nDatabase [{dbType}] => Alias [{dbAlias}] => URL [{default_db_url}]")

# إعداد الاتصال بقاعدة البيانات
# EnableEcho = True
EnableEcho = False
engine = create_engine(default_db_url , echo=EnableEcho)
Base = declarative_base()

# إنشاء الجداول
Base.metadata.create_all(engine)

# إنشاء جلسة للتفاعل مع قاعدة البيانات
SessionMaker = sessionmaker(bind=engine)
session = SessionMaker()