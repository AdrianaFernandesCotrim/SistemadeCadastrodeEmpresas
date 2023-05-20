from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine= create_engine('mysql+pymysql://u221579840_inf_warehouse:Inf_warehouse123@sql775.main-hosting.eu/u221579840_inf_warehouse')
base = declarative_base()

class empresas(base):
    __tablename__ = 'Empresa'

    cnpj = Column(String(15), primary_key=True)
    Nome = Column(String(250))
    Logradouro = Column(String(250))
    Numero = Column(String(250))
    Bairro = Column(String(250))
    Municipio = Column(String(250))
    UF = Column(String(250))
    CEP = Column(String(250))
    TELEFONE = Column(String(250))
    EMAIL = Column(String(250))

    def __init__ (self, cnpj, Nome, Logradouro, Numero, Bairro, Municipio, UF, CEP, TELEFONE, EMAIL):
        self.cnpj = cnpj
        self.Nome = Nome
        self.Logradouro = Logradouro
        self.Numero = Numero
        self.Bairro = Bairro
        self.Municipio = Municipio
        self.UF = UF
        self.CEP = CEP
        self.TELEFONE = TELEFONE
        self.EMAIL = EMAIL

base.metadata.create_all(engine)