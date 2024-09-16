from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://lakshit722_user:C1eWdJiyEMciUKysAjb6xEmHSqhNvHA4@dpg-crg39djqf0us73dg3090-a.oregon-postgres.render.com/lakshit722" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
