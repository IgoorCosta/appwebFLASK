from services.pbiembedservice import PbiEmbedService
from utils import Utils
from flask import Flask, render_template, send_from_directory, redirect, url_for, request, session, Markup
import json

import pandas as pd
import os
import re

from operator import le


# Inicializar o aplicativo Flask
app = Flask(__name__)

# Load configuration
app.config.from_object('config.BaseConfig')
#app.config['UPLOAD_FOLDER']='static/files'
#app.config['SALES']='static/sales'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getembedinfo', methods=['GET'])
def get_embed_info():
    '''Returns report embed configuration'''

    config_result = Utils.check_config(app)
    if config_result is not None:
        return json.dumps({'errorMsg': config_result}), 500

    try:
        embed_info = PbiEmbedService().get_embed_params_for_single_report(app.config['WORKSPACE_ID'], app.config['REPORT_ID'])
        return embed_info
    except Exception as ex:
        return json.dumps({'errorMsg': str(ex)}), 500

@app.route('/favicon.ico', methods=['GET'])
def getfavicon():
    '''Returns path of the favicon to be rendered'''

    return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/form_login', methods=['POST','GET'])
def login():
    #when POST request is made
    if request.method=='POST':
        #when the user uploads a custom file
        if request.form['switch']=="123":
            
            return render_template('temp1.html')

        #when the login button is clicked, main page gets loaded
        elif request.form['switch']=="456":
            name=request.form['u']
            psd1=request.form['v']
            print(name+" "+psd1)
            if name != "user":
                return render_template('index.html',info="Usuário Desconhecido!")
            elif psd1 != "user":
                return render_template('index.html',info="Senha Incorreta!")
            else:
                return render_template('temp.html')

        #back button is clicked
        elif request.form['switch']=='goback':

            return render_template('temp.html')

        #when button to create new graph is clicked
        elif request.form['switch']=="graph":
            
            return render_template('temp1.html')
    
    #when GET request is made
    else:
        df=[]
        list1=[]
        list2=[]
        return render_template('temp.html')

if __name__ == '__main__':
    app.run()