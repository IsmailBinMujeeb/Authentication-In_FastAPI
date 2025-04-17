from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

MYSQL_CONN_URI = "mysql+mysqlconnector://root:UNIVO@localhost:3306/Authenticator"

engine = create_engine(MYSQL_CONN_URI)
Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)