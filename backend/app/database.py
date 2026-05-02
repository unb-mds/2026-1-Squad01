from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# A URL de conexão para o Docker rodando na sua máquina
SQLALCHEMY_DATABASE_URL = "postgresql://admin:123@localhost:5432/safestreets"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()