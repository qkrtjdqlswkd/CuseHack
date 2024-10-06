# auth.py
from flask import Blueprint, render_template, request, flash, redirect, url_for
import supabase
# from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
# from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
import os
from supabase import create_client, Client



auth = Blueprint('auth', __name__)


def get_user_by_email(email):
    
    response = supabase.table("users").select("*").eq("email", email).execute()
    return response.data[0] if response.data else None


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # response = supabase.table("users").select("*").eq("email", email).execute()
        # user_data = response.data[0] if response.data else None

        user_data = get_user_by_email(email)


        if user_data:
            if check_password_hash(user_data['password'], password):
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
        # print(password, email)

    #     user = User.query.filter_by(email=email).first()

    return render_template("login.html", user=current_user)




@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # user = User.query.filter_by(email=email).first()

        response = supabase.table("users").select("*").eq("email", email).execute()
        
        user_data = response.data[0] if response.data else None

        if user_data:
            # if user_data match, password 2nd check
            # if check_password_hash(user_data['password'], password1):
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # new_user = User(email=email, first_name=first_name, password=generate_password_hash(
            #     password1, method='sha256'))
            # db.session.add(new_user)
            # db.session.commit()
            # login_user(new_user, remember=True)


            new_user = {
                "email": email,
                "first_name": first_name,
                "password": generate_password_hash(password1, method='sha256')
            }

            response = supabase.table("users").insert(new_user).execute()

            if response.status_code == 201:


                user_data = supabase.table("users").select("*").eq("email", email).execute().data[0]
                flash('Account created!', category='success')
                login_user(user_data, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Error creating account: ' + str(response.error), category='error')

    return render_template("sign_up.html", user=current_user)