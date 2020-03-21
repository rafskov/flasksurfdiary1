from flask import render_template,request
from flask_sqlalchemy import SQLAlchemy
from buoyant import Buoy
from app import app
from models import Post
from app import db
import random


#views is where you access the model


@app.route('/',methods=['GET','POST'])
def index():

    if request.method == 'POST':
        
        #get ocean data from NOAA

        sfocean = Buoy(46237)
        sf_waves = sfocean.waves
        sf_height = sf_waves['sea_surface_wave_significant_height'] * 3
        sf_period = sf_waves['sea_surface_swell_wave_period']

        sfdata=[]

        sfdata.append(sf_height)
        sfdata.append(sf_period)
        
        
        #get form data
        postername = request.form.get('postername')
        sessionrank = request.form.get('session')

        #generate image
        img = random.randint(0,5)

        #add it to the db
        if postername:
            newpostobj = Post(name=postername,session_description=sessionrank,waveheight = sf_height,img=img,waveperiod=sf_period)
            db.session.add(newpostobj)
            db.session.commit()
        
    posts = Post.query.all()

    return render_template('index.html', posts = posts)


#first setup route, basic template
#then plug data in to template from route
#create sqlite db from cmd
#create table from python repl,
#check in sqllite that table was created 



