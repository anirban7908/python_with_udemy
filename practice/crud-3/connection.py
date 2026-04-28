from pymongo import MongoClient
from marshmallow import ValidationError, Schema, fields
from dotenv import load_dotenv
import os

load_dotenv()

class UserSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)
    gender = fields.String(required=True)
    address = fields.String(required=True)
    occupation = fields.String(required=True)


class DbConnection:
    def __init__(self):
        uri = os.getenv("MONGO_URI")
        self.client = MongoClient(uri, tlsAllowInvalidCertificates=True)
        self.db=self.client["practice_db"]
        self.collection=self.db['crud_3']

    