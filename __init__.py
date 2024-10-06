# __init__.py
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
# import supabase
import os
from supabase import create_client, Client
import supabase
from dotenv import load_dotenv
from pathlib import Path




# db = SQLAlchemy()
# DB_NAME = "database.db"

# load_dotenv("supanova.env")



env_path = Path(__file__).parent / 'supanova.env'

load_dotenv(env_path)

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")


supabase = create_client(url, key)



class User:
    def __init__(self, id):
        self.id = id

def load_user(user_id):

    # Replace this with your logic to get a user from Supabase or your user database
    return User(user_id)

class SupabaseUser:
    def __init__(self, email, first_name, password) -> None:
        self.email = email
        self.first_name = first_name 
        self.password = password

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # db.init_app(app)


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    def load_user(id):
        response = supabase.table("users").select("*").eq("id", id).execute()
        if response.data:
            user_data = response.data[0]
            return SupabaseUser(email=user_data['email'], 
                                 first_name=user_data['first_name'],
                                 last_name=user_data['last_name'])
        return None
        




    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # from .models import User, Note
    
    # with app.app_context():
        # db.drop_all()
        # db.create_all()
        
    



    def get_user_by_id(id):
        response = supabase.table("users").selecdt("*").eq("id", id).execute()
        return response.data[0] if response.data else None


    # @login_manager.user_loader


# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app=app)
#         print('Created Database!')