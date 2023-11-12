#!/usr/bin/python3
"""Defines the Review class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class represents a city and inherits from the BaseModel class.

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.
    """
    state_id = ''
    name = ''
