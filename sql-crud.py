from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessopm,ale, then point to our engine (the db)
Session = sessionmaker(db)
# open an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# Query 1 - select all records from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - select only the "Name" column from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# Query 3 - select only "Queen" from the "Artist" table
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - selct only the albums with "ArtistId" #51 on the "ALbum" table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, sep=" | ")

# Query 6 - select all tracks where the composer is 'Queen' from the "Track" table
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(track.TrackId, track.Name, track.AlbumId, track.MediaTypeId, track.GenreId, track.Composer, track.Milliseconds, track.Bytes, track.UnitPrice, sep=" | ")