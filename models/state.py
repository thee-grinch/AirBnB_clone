#!/usr/bin/python3
"""Defines the State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State Class

    This class represents a state object. It inherits from the
    BaseModel class and includes a 'name' attribute.

    Attributes:
    - name (str): The name of the state.

    """
    name: str = ""
