#!/usr/bin/python3
"""Defines the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Defines the Review Class

    Attributes:
        place_id (str): The ID for the place associated with the review.
        user_id (str): The ID for the user who wrote the review.
        text (str): The text content of the review.
    """

    place_id: str = ''
    user_id: str = ''
    text: str = ''
