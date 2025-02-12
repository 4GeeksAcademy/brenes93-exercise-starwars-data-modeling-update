import os
import sys
from typing import List
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from eralchemy2 import render_er
from sqlalchemy import ForeignKey, String, create_engine

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

class Usuarios(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    nombre: Mapped[str] = mapped_column(nullable=False)
    apellidos: Mapped[str] = mapped_column(nullable=False)
    ciudad: Mapped[str] = mapped_column(nullable=False)
    personaje_favorito: Mapped[List["Personajes_favoritos"]] = relationship(back_populates="usuario")
    planeta_favorito: Mapped[List["Planetas_favoritos"]] = relationship(back_populates="usuario")
    vehiculo_favorito: Mapped[List["Vehiculos_favoritos"]] = relationship(back_populates="usuario")
   
class Personajes(Base):
    __tablename__ = 'personaje'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    genero: Mapped[str] = mapped_column(nullable=False)
    edad: Mapped[int] = mapped_column(nullable=False)
    altura: Mapped[int] = mapped_column(nullable=False)
    color_de_ojos: Mapped[str] = mapped_column(nullable=False)
    color_de_pelo: Mapped[str] = mapped_column(nullable=False)
    personaje_favorito: Mapped[List["Personajes_favoritos"]] = relationship(back_populates="personaje")

class Planetas(Base):
    __tablename__ = 'planeta'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False, unique=True)
    clima: Mapped[str] = mapped_column(nullable=False)
    gravedad: Mapped[int] = mapped_column(nullable=False)
    terreno: Mapped[str] = mapped_column(nullable=False)
    planeta_favorito: Mapped[List["Planetas_favoritos"]] = relationship(back_populates="planeta")

class Vehiculos(Base):
    __tablename__ = 'vehiculo'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False, unique=True)
    modelo: Mapped[str] = mapped_column(nullable=False)
    capacidad: Mapped[str] = mapped_column(nullable=False)
    altura: Mapped[int] = mapped_column(nullable=False)
    vehiculo_favorito: Mapped[List["Vehiculos_favoritos"]] = relationship(back_populates="vehiculo")        
      


class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    street_name: Mapped[str]
    street_number: Mapped[str]
    post_code: Mapped[str] = mapped_column(nullable=False)

class Personajes_favoritos(Base):
    __tablename__ = 'personaje_favorito'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
    personaje_id: Mapped[int] = mapped_column(ForeignKey("personaje.id"))
    usuario: Mapped["Usuarios"] = relationship(back_populates="usuario")  
    personaje: Mapped["Personajes"] = relationship(back_populates="personaje_favorito")   

class Planetas_favoritos(Base):
    __tablename__ = 'planeta_favorito'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
    planeta_id: Mapped[int] = mapped_column(ForeignKey("planeta.id"))
    usuario: Mapped["Usuarios"] = relationship(back_populates="usuario")  
    planeta: Mapped["Planetas"] = relationship(back_populates="planeta_favorito")     

class Vehiculos_favoritos(Base):
    __tablename__ = 'vehiculo_favorito'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
    vehiculo_id: Mapped[int] = mapped_column(ForeignKey("vehiculo.id"))
    usuario: Mapped["Usuarios"] = relationship(back_populates="usuario")  
    vehiculo: Mapped["Vehiculos"] = relationship(back_populates="vehiculo_favorito")     
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
