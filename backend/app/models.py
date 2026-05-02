from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Ocorrencia(Base):
    __tablename__ = "ocorrencias"

    id = Column(Integer, primary_key=True, index=True)
    titulo_noticia = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)