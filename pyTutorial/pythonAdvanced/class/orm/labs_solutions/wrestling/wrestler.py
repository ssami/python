"""Class describing the wrestler.
"""


import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Turn echo to True to see the created SQL statements.
engine = create_engine('sqlite:///test.db3', echo=False)

# Create a database session (connection) for getting/saving wrestlers.
session = sessionmaker(bind=engine)()

# Allow use of declarative models.
Base = declarative_base(bind=engine)

# Model/db table as Python class.
class Wrestler(Base):
    __tablename__ = 'wrestlers'

    id = Column(Integer, primary_key=True)
    name = Column(String, default="NOBODY", unique=True, nullable=False)
    brawn = Column(Integer, default=5, nullable=False)
    finesse = Column(Integer, default=5, nullable=False)
    wins = Column(Integer, default=0, nullable=False)
    losses = Column(Integer, default=0, nullable=False)
    
    def __repr__(self):
        """Pretty print.
        """
        return "(%s) %s" % (self.id, self.name)

    def attrs_as_dict(self):
        """Returns a copy of our base attributes as a dictionary.
        """
        return {
            "id": self.id,
            "name": self.name,
            "brawn": self.brawn,
            "finesse": self.finesse,
            "wins": self.wins,
            "losses": self.losses,
        }

    def save(self):
        """Attempt to persist the wrestler in the database.
        
        First attempt to create the wrestler. If this fails, attempt to
        update wrestler, assuming that a failure means wrestler already
        exists in the database.
        """
        # Try to create ourselves in the database first.
        try:
            session.add(self)
            session.commit()
        except sqlalchemy.exc.SQLAlchemyError:
            session.rollback()
            session.commit()


# Create the tables if they don't exist.
Base.metadata.create_all()



def get_wrestlers():
    """Grabs a list of all of the wrestlers from the database.
    
    @return A list of Wrestler objects, or an empty list if no 
    wrestlers have been created.
    """
    return session.query(Wrestler).all()
