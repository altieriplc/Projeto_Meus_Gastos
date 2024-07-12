import sqlalchemy
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, Integer, ForeignKey

Base = declarative_base() # Base = estrutura modelo que vai ser utilizada para criar as classes da aplicação
                            # declarative_base: É uma função que retorna uma classe base especial do SQLAlchemy chamada DeclarativeMeta. Esta classe base é utilizada para criar classes de mapeamento de objetos (ORM) que representam tabelas no banco de dados. Ela permite definir estruturas de dados Python que são automaticamente mapeadas para tabelas no banco de dados, facilitando a interação entre objetos Python e dados persistidos em um banco de dados relacional.

class User(Base):
    __tablename__ = 'user_account' # __tablename__ não é uma função, mas sim uma convenção
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(100))
    
    
class Addres(Base):
    __tablename__ = 'user_address'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False) # address precisa estar linkado a algum usuário
    