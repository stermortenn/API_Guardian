from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:dias2004@localhost:5432/API_Guardian"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

