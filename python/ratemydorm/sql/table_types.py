from __future__ import annotations
import datetime
from typing import NamedTuple
from collections import namedtuple
from decimal import Decimal

"""
Classes to be used as type annotations for Rows returned from the db
Only to be used with a cursor defined with named_tuple=True
ex: cursor = connection.cursor(named_tuple=True)
"""


class ReviewRow(NamedTuple):
    review_id: int
    user_id: int
    dorm_id: int
    timestamp: datetime.datetime
    rating: int
    review_text: str


class TagsRow(NamedTuple):
    dorm_id: int
    tag: str


class UsersRow(NamedTuple):
    user_id: int
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    profile_image: str
    status: str
    profile_bio: str
    user_role: str


class UserProfile(NamedTuple):
    username: str
    first_name: str
    last_name: str
    email: str
    profile_image: str
    status: str
    profile_bio: str
    user_role: str


class FeaturesRow(NamedTuple):
    feature_id: int
    feature: str
    data_type: str


class FeaturesLutRow(NamedTuple):
    dorm_id: int
    feature_id: int
    feature_value: str


class DormImageRow(NamedTuple):
    dorm_id: int
    user_id: int
    url: str


class DormRow(NamedTuple):
    dorm_id: int
    latitude: Decimal
    longitude: Decimal
    room_num: int
    floor: int
    building: str
    quad: str
    address: str

class AddDorm(NamedTuple):
    dorm_id: int
    latitude: Decimal
    longitude: Decimal
    room_num: int
    floor: int
    building: str
    quad: str
    address: str


Tables = namedtuple('Tables', 'dorm dorm_image features_lut features review tags reviews addDorm')


class TableRegistry:

    tables = Tables(
        dorm=DormRow,
        dorm_image=DormImageRow,
        features_lut=FeaturesLutRow,
        features=FeaturesRow,
        review=ReviewRow,
        tags=TagsRow,
        reviews=ReviewRow,
        addDorm=AddDorm,
    )


