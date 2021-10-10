from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def get_line_attr(line):
    return line[:-1].split('=')[1]


with open('database.config', 'r') as db:
    engine = create_engine(get_line_attr(db.readline())) # you must insert your path here
    schema = get_line_attr(db.readline())


session_factory = sessionmaker(bind=engine)
Base = declarative_base()
Base.__table_args__ = {'schema': schema}


def build_db_session():
    Base.metadata.create_all(engine)
    return session_factory()


