from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# Write your classes below
class Artist(Base):
	__tablename__ = 'artists'
	id = Column(Integer, primary_key=True)
	name = Column(String)

	songs = relationship('Song', back_populates='artist')
	genres = relationship('Genre', secondary='songs', back_populates='artists')


class Genre(Base):
	__tablename__ = 'genres'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	
	songs = relationship('Song', back_populates='genre')
	artists = relationship('Artist', secondary='songs', back_populates='genres')

class Song(Base): 
	__tablename__ = 'songs'
	id = Column(Integer, primary_key=True)
	name = Column(String)

	artist_id = Column(Integer, ForeignKey('artists.id'))
	genre_id = Column(Integer, ForeignKey('genres.id'))

	artist = relationship('Artist', back_populates='songs')
	genre = relationship('Genre', back_populates='songs')

# ###
# 	an artist attribute that establishes the relationship to the Artist model and back_populates to an Artist's songs property
# a genre attribute that establishes the relationship to the Genre model and back_populates to a Genre's songs property






# engine = create_engine('sqlite:///:memory:')

engine = create_engine('sqlite:///songs_lab.db')

Base.metadata.create_all(engine)
