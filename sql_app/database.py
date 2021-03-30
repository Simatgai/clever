from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import urllib
host_server = os.environ.get('host_server', 'bdarnyoo1zvhftbmglvs-postgresql.services.clever-cloud.com')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '5432')))
database_name = os.environ.get('database_name', 'bdarnyoo1zvhftbmglvs')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'uuhihfpokyjr5u90msul')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', 'PLxR9DbmSZBFXqdg3qQf')))
ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode','prefer')))
SQLALCHEMY_DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host_server, db_server_port, database_name, ssl_mode)
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgres://xsboezwp:leMY5iTxf9ABe94Phic37RZPmkdiS-Ca@satao.db.elephantsql.com:5432/xsboezwp"

engine = create_engine(
    # SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    SQLALCHEMY_DATABASE_URL ,
    pool_size = 3,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()