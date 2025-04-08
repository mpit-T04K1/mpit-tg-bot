from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.settings import settings

engine = create_engine(settings.sqlite_url)
Session = sessionmaker(autoflush=False, bind=engine)

