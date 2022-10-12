from app import db, app
from flask import Flask, jsonify, render_template, url_for, request, redirect, flash, request
from app.models import *
from flask_login import login_user, login_required, logout_user
from app.bot import send_msg


@app.route('/', methods=['POST', 'GET'])
def index():
    """Main page"""
    
    tg_user = ['1064201988', '1655138958']
    
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        
        # send notification tg
        for id in tg_user:
            try:
                send_msg(id, f'* New Application *\n\nName: {name}\nEmail: {email}\nPhone: {phone}')
            except Exception as e:
                pass
            
        # reload 
        return redirect(url_for('index'))
        
    
    
    return render_template('index.html')


# @app.route('/logout', methods=['POST', 'GET'])
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('auth'))


# @app.after_request
# def redirect_to_signin(response):
#     """Redirect user without authorization"""
#     if response.status_code == 401:
#         return redirect(url_for('auth') + '?next=' + request.url)
#     else:
#         return response
