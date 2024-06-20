from databases import Database
import sqlalchemy
from sqlalchemy import create_engine, ForeignKey

DATABASE_URL = 'sqlite:///moto_service.db'
database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

clients = sqlalchemy.Table(
    'clients',
    metadata,
    sqlalchemy.Column('client_id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('document', sqlalchemy.String(128), nullable=False, unique=True),
    sqlalchemy.Column('surname', sqlalchemy.String(128), nullable=False),
    sqlalchemy.Column('firstname', sqlalchemy.String(128), ),
    sqlalchemy.Column('patronymic', sqlalchemy.String(128)),
    sqlalchemy.Column('birthday', sqlalchemy.Date, nullable=False),
)

motorcycle = sqlalchemy.Table(
    'motorcycle',
    metadata,
    sqlalchemy.Column('motorcycle_id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('client_id', sqlalchemy.Integer, ForeignKey('clients.client_id'), nullable=False),
    sqlalchemy.Column('name', sqlalchemy.String(128)),
    sqlalchemy.Column('birthday', sqlalchemy.Date, nullable=False),
)

consultation = sqlalchemy.Table(
    'consultation',
    metadata,
    sqlalchemy.Column('consultation_id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('client_id', sqlalchemy.Integer, ForeignKey('clients.client_id'), nullable=False),
    sqlalchemy.Column('motorcycle_id', sqlalchemy.Integer, ForeignKey('motorcycle.motorcycle_id'), nullable=False),
    sqlalchemy.Column('consultation_date', sqlalchemy.Date),
    sqlalchemy.Column('description', sqlalchemy.String(128)),
)

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
