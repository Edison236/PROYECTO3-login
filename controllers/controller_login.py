from flask import Blueprint, render_template, request, jsonify,redirect,url_for
from flask_login import LoginManager, login_user, login_required
from models.user import User
from tkinter import messagebox
import tkinter as tk

login_bp = Blueprint('user', __name__)

@login_bp.route('/login', methods=['GET','POST'])
def user_login():
    print("si esta llegando")
    if request.method == 'GET':
        return render_template('login.html',msg = '')
    else: 
        print(request.form["username"])
        username = request.form["username"]
        password = request.form["password"]
    list_user = User.query.all()
    for user in list_user:
        if user.username == username and user.password == password:
            if user.is_admin == True:
                print("admin") 
                return render_template('index.html')     
            else:
                print("no admin")   
                return render_template('login.html', msg= '¡Usuario o contraseña invalida!')
    print("no logueado")
    return render_template('login.html', msg= '¡Usuario o contraseña invalida!')
            
    
@login_bp.route('/ruta-logueada')
@login_required
def ruta():
    print("ruta login")
    return render_template("login.html")
