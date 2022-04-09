from sqlalchemy import String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

SqliteDecimal = String  # Sqlite cannot deals with Decimal perfectly (as opposed to say Postgres
# https://stackoverflow.com/questions/68417903/very-long-integers-in-sqlalchemy-with-sqlite)
