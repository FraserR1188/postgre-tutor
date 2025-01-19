from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the chinook database
db = create_engine("postgresql:///chinook")
base = declarative_base()

class FavouritePlace(base):
    __tablename__ = "FavouritePlace"
    id = Column(Integer, primary_key=True)
    country_name = Column(String)
    capital = Column(String)
    population = Column(Integer)
    favourite_food = Column(String)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

# creating our records for the countrys

germany = FavouritePlace(
    country_name = "Germany",
    capital = "Berlin",
    population = 83000000,
    favourite_food = "Bratwurst"
)

italy = FavouritePlace(
    country_name = "Italy",
    capital = "Rome",
    population = 59000000,
    favourite_food = "Pizza"
)


spain = FavouritePlace(
    country_name = "Spain",
    capital = "Madrid",
    population = 47000000,
    favourite_food = "Paella"
)

switzerland = FavouritePlace(
    country_name = "Switzerland",
    capital = "Bern",
    population = 8800000,
    favourite_food = "Fondue"
)

# session.add(italy)
# session.add(germany)
# session.add(spain)
# session.add(switzerland)

city = session.query(FavouritePlace)
for place in city:
    place.capital = place.capital.upper()
session.commit()

favourite_places = session.query(FavouritePlace)
for favourite_place in favourite_places:
    print(
        favourite_place.id,
        favourite_place.country_name,
        favourite_place.capital,
        favourite_place.population,
        favourite_place.favourite_food,
        sep=" | "
    )