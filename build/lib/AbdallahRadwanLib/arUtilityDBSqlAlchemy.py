from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from AbdallahRadwanLib.arUtilityConst import ardbSettings

"""
    1. Create new engine
    2. create new declarative base
    3. base with metadata and assign engine
    4. create new session maker
    5. Inherit from new object from session maker
"""

# Database configuration
Base = declarative_base()

class arSQLAlchemyManager:
    __instance = None
    @staticmethod
    def CreateInstance(dbSetting :ardbSettings):
        if (arSQLAlchemyManager.__instance == None):
            arSQLAlchemyManager.__instance = arSQLAlchemyManager(dbSetting)
        return arSQLAlchemyManager.__instance
    
    def __init__(self, dbSetting :ardbSettings):
        """Initialize the database manager with the provided database URL."""        
        EnableEcho,dbType = dbSetting.EnableEcho, dbSetting.dbType.upper()
        if (dbType == "ORACLE"):        
            database_url = f"oracle+cx_oracle://{dbSetting.dbUser}:{dbSetting.dbPass}@{dbSetting.dbHost}:{dbSetting.dbPort}/{dbSetting.dbService}"
        elif (dbType == "SQLITE"):        
            database_url = f"sqlite:///{dbSetting.dbPath}\\Database\\SQLite\\{dbSetting.dbName}.db"
        elif (dbType == "MONGODB"):        
            database_url = f"mongodb://{dbSetting.dbHost}:{dbSetting.dbPort}/"          
        else:
            database_url = ""  
        print(f"Welcome to SqlAlchemy : Database [{dbType}] => Alias [{dbSetting.dbAlias}] => URL [{database_url}]")
        # إعداد الاتصال بقاعدة البيانات
        self.engine = create_engine(database_url, echo=EnableEcho)
        self.Base = declarative_base()
        self.SessionMaker = sessionmaker(bind=self.engine)        
        self.create_tables()  # Create tables if they don't exist  

    def get_base(self):
        return self.Base
    
    def create_tables(self):
        """Create the database tables."""
        # إنشاء الجداول
        self.Base.metadata.create_all(bind=self.engine)

    def get_session(self):
        # إنشاء جلسة للتفاعل مع قاعدة البيانات
        """Return a new session."""        
        return self.SessionMaker()