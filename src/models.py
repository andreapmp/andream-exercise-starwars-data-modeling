import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
   

    def __repr__(self):
        return '<User %r>' % self.username

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    favorite_character = Column(String(250), nullable=False)
    favorite_planet = Column(String(250), nullable=False)
    favorite_vehicle = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

    def __repr__(self):
        return '<Favorite %r>' % self.id
    
class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    gender = Column(String(250))
    height = Column(String(250))
    weight = Column(String(250))
    eye_color = Column(String(250))
    favorite_id = Column(Integer, ForeignKey('favorites.id'))
    favorite = relationship(Favorite)

    def __repr__(self):
        return '<Character %r>' % self.character_name

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    terrain = Column(String(250))
    population = Column(String(250))
    climate = Column(String(250))
    favorite_id = Column(Integer, ForeignKey('favorites.id'))
    favorite = relationship(Favorite)

    def __repr__(self):
        return '<Planet %r>' % self.planet_name
    
class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    vehicle_class = Column(String(250))
    passengers = Column(String(250))
    speed = Column(String(250))
    favorite_id = Column(Integer, ForeignKey('favorites.id'))
    favorite = relationship(Favorite)

    def __repr__(self):
        return '<Vehicle %r>' % self.vehicle_name

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
