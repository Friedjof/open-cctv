from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modules.model.models import User, Base

engine = create_engine('sqlite:///../../database/database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

user: User = User(username="friedjof", password="Testen123")
session.add(user)
session.commit()
