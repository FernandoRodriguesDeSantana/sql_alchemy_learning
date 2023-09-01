# LINK TO VIEW THIS CODE IN COLAB: 
# https://colab.research.google.com/drive/1MOeX7YyLfW6ITqB6Al2Pu2lBXbLmVMT1?usp=sharing
import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('sqlite:///enterprise.db', echo = True)
#enterprise.db foi criado neste instante

Base = declarative_base()

class User(Base):
  __tablename__ = 'users'
  #__tablename__ é obrigatório
  id = Column(Integer, primary_key=True)
  #id = Column é obrigatório
  name = Column(String(50))
  fullname = Column(String(50))
  age = Column(Integer)

  def __repr__(self):
    return "<User(name={}, fullname={}, age{})>".format(self.name, self.fullname, self.age)

Base.metadata.create_all(engine)

user = User(name='Fernando', fullname='Fernando Rodrigues de Santana', age=20)

type(user)
user.name
user.fullname
user.age
Session = sessionmaker(bind=engine)
Session
session = Session()
session.add(user)
session.commit()

session.add_all([
    User(name='Jair', fullname='Jair Messias Bolsonaro', age=22),
    User(name='Luiz', fullname='Luiz Inácio Lula da Silva', age=13),
    User(name='Cabo', fullname='Cabo Daociolo', age=45),
    User(name='Luciano', fullname='Hang Véio da Havan', age=22),
    User(name='Kim', fullname='Kim Kataguiri', age=24)
])

session.new
session.commit()

query_user = session.query(User).filter_by(name='Jair').first()
query_user.name
query_user.fullname
query_user.age
for instance in session.query(User).order_by(User.id):
  print(instance.name, instance.fullname)

for info in session.query(User.name, User.age).filter_by(name='Luiz'):
    print(info)

user.fullname
user.fullname = 'Fernando Rodrigues'
user
session.dirty
# histórico de dados alterados
session.commit()

user = session.query(User).filter_by(name='Cabo').first()
user
session.delete(user)
session.commit()

session.query(User).filter_by(name='Kim').count()
# realiza a contagem da quantidade de dados com nome 'Kim'
