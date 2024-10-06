# from . import db
# from flask_login import UserMixin
# from sqlalchemy.sql import func


# class Note(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     data = db.Column(db.String(10000))
#     date = db.Column(db.DateTime(timezone=True), default=func.now())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(150), unique=True)
#     password1 = db.Column(db.String(150))
#     first_name = db.Column(db.String(150))
#     notes = db.relationship('Note')

# models.py

from supabase import create_client, Client
import os
from dotenv import load_dotenv
# from pathlib import Path
from .__init__ import url, key


# Creating absolute path to find env file which has URL and Key
# env_path = Path(__file__).parent / 'supanova.env'

# load_dotenv(env_path)


print("Environment Variables:")
print(f"SupaBase URL: {os.environ.get('SUPABASE_URL')}")
print(f"SupaBase Key: {os.environ.get('SUPABASE_KEY')}")






# class SupabaseUser:
#     def __init__(self, email, first_name, last_name, password) -> None:
#         self.email = email
#         self.first_name = first_name 
#         self.last_name = last_name
#         self.password = password

def create_supanoba_user() -> Client:
    
    # url: str = os.environ.get("https://pompeddkhfsoiauturyc.supabase.co")
    # key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBvbXBlZGRraGZzb2lhdXR1cnljIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjgxOTk5MjgsImV4cCI6MjA0Mzc3NTkyOH0.teaiGA3Q1sVAK-Q84MX27AINuCB7rLJVzrRNGUqTuQU")

    # url: str = os.environ.get("SUPABASE_URL")
    # key: str = os.environ.get("SUPABASE_KEY")

    print(f"Supabase URL: {url}")
    print(f"Supabase Key: {key}")

    if not url or not key:
        raise ValueError("Supabase URL and key must be set in environment variables.")
    
    return create_client(url, key)

supabase = create_supanoba_user()