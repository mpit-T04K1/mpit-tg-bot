from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///metanit.db")
Session = sessionmaker(autoflush=False, bind=engine)

