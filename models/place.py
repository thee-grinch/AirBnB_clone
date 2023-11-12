#!/usr/bin/python3
"""Defines the Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Defines the State class.

    Attributes:
        city_id (str): The ID of city.
        user_id (str): The ID of user.
        name (str): The name of the state.
        description (str): A brief description of the state.
        number_rooms (int): The number of rooms available
        number_bathrooms (int): The number of bathrooms available.
        max_guest (int): The maximum number of guests allowed.
        price_by_night (int): The price per night.
        latitude (float): The latitude coordinate of the state.
        longitude (float): The longitude coordinate of the state.
        amenity_ids (list): A list of IDs representing amenities available.
    """

    city_id: str = ''
    user_id: str = ''
    name: str = ''
    description: str = ''
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: list = []
