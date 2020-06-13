#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from app import db

from flask import Flask
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app,db)

#============================================================================#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(), nullable=False)
    state = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), default="-")
    image_link = db.Column(db.String())
    genres = db.Column(db.ARRAY(db.String()), default=['Other'])
    facebook_link = db.Column(db.String())
    website = db.Column(db.String())
    seeking_talent = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.String())
    shows = db.relationship('Show', backref='venue', lazy=True)

    def __repr__(self):
      return f'<Venue {self.id} name: {self.name}>'

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(), nullable=False)
    state = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), default="Number not listed")
    genres = db.Column(db.ARRAY(db.String()), default=['Other'])
    days_available = db.Column(db.ARRAY(db.String(10)), nullable=False, default=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
    image_link = db.Column(db.String())
    facebook_link = db.Column(db.String())
    shows = db.relationship('Show', backref='artist', lazy=True)


    def __repr__(self):
      return f'<Artist {self.id} name: {self.name}>'


class Show(db.Model):
    __tablename__ = 'Show'

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
      return f'<Show {self.id}, Artist {self.artist_id}, Venue {self.venue_id}>'

db.create_all()



#-------------------------------------------------------------------------------#
# Feeding Real Data
#-------------------------------------------------------------------------------#

venue1 = Venue(
    name="9:30 Club",
    city="Washinton",
    state="Washington",
    address="815 V St NW, Washington, DC 20001, United States",
    phone="202.265.0930",
    image_link="https://i.pinimg.com/originals/f1/68/91/f16891613a64d40e3ba48c286921281b.jpg",
    genres = ["ALTERNATIVE","BLUES","FOLK","JAZZ","ROCK N ROLL"], 
    facebook_link="https://www.facebook.com/930club/",
    seeking_description="9:30 Club a nightclub and concert venue in Washington, D.C. ",
    website="https://www.930.com/",
    seeking_talent=True)
    

venue2 = Venue(
    name="First Avenue",
    city="Minneapolis",
    state="Minnesota",
    address="701 First Avenue North",
    phone="(612) 332-1775",
    image_link="https://specials-images.forbesimg.com/imageserve/476036534/960x0.jpg?fit=scale",
    genres = ["ALTERNATIVE","BLUES","FOLK","JAZZ","ROCK N ROLL"], 
    facebook_link="https://www.facebook.com/firstavenue/",
    seeking_description="First Avenue & 7th St Entry (locally known as The Mainroom and The Entry) are two music venues housed in the same landmark building in downtown Minneapolis, Minnesota.",
    website="https://first-avenue.com/venue/first-avenue",
    seeking_talent=True)


venue3 = Venue(
    name="Tower Theater",
    city="Philadelphia",
    state="Pennsylvania",
    address="S 69th St &, Ludlow St, Upper Darby, PA 19082",
    phone="(541) 317-0700",
    image_link="https://specials-images.forbesimg.com/imageserve/476036534/960x0.jpg?fit=scale",
    genres = ["ALTERNATIVE","BLUES","FOLK","JAZZ","ROCK N ROLL"], 
    facebook_link="https://www.facebook.com/TowerPhilly/",
    seeking_description="The Tower Theater has been a popular venue for music acts since the 1970s. In 2018, the Tower Theater was named one of the 10 best live music venues in America by Rolling Stone Magazine.",
    website="https://www.towertheatre.org/",
    seeking_talent=True)

venue4= Venue(
    name="Tower Theater",
    city="Los Angeles",
    state="California",
    address="2301 N. Highland Ave., Los Angeles, CA 90078",
    phone="323 850 2000",
    image_link="https://ucarecdn.com/8ae9952d-6848-4d2a-9b5b-69c5578c2e9d/",
    genres = ["ALTERNATIVE","BLUES","FOLK","JAZZ","ROCK N ROLL"], 
    facebook_link="https://www.facebook.com/HollywoodBowl/",
    seeking_description="The Hollywood Bowl is an amphitheatre in the Hollywood Hills neighborhood of Los Angeles.",
    website="https://www.hollywoodbowl.com/",
    seeking_talent=True)
  
  
venue5 = Venue(
    name="Rose Bowl stadium",
    city="Pasadena",
    state="California",
    address="1001 Rose bowl Dr, Pasadena, CA 91103, United States",
    phone="1 626-577-3100",
    image_link="https://pbs.twimg.com/media/D6JuLx4UIAAvRTW.jpg",
    genres = ["ALTERNATIVE","BLUES","FOLK","JAZZ","ROCK N ROLL"], 
    facebook_link="https://www.facebook.com/RoseBowlStadium/",
    seeking_description="The Rose Bowl is an American outdoor athletic stadium, located in Pasadena, California",
    website="http://www.rosebowlstadium.com/",
    seeking_talent=True)

  
venue6 = Venue(
    name="MetLife stadium",
    city="East Rutherford",
    state="New Jersey",
    address="1 met Life stadium Dr, East Rutherford, NJ, 07073, United States",
    phone="1 201-559-1515",
    image_link="https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Metlife_stadium_%28Aerial_view%29.jpg/1024px-Metlife_stadium_%28Aerial_view%29.jpg/",
    genres = ["ALTERNATIVE","BLUES","FOLK","JAZZ","ROCK N ROLL"], 
    facebook_link="https://www.facebook.com/MetLifeStadium/",
    seeking_description="MetLife Stadium is an American sports stadium located at the Meadowlands Sports Complex",
    website="https://www.metlifestadium.com/",
    seeking_talent=True)

venue7 = Venue(
    name="AT&T Stadium",
    city="Arlington",
    state="Texas",
    address="1 AT&T way, Arlington, TX 76011, United States",
    phone="1 817-892-4000",
    image_link="https://pbs.twimg.com/media/DrfeP1WWsAELuF3.jpg",
    genres = ["ALTERNATIVE","BLUES","FOLK","JAZZ","ROCK N ROLL"], 
    facebook_link="https://www.facebook.com/ATTStadium/",
    seeking_description="AT&T Stadium, formerly Cowboys Stadium, is a retractable roof stadium in Arlington, Texas, United States.",
    website="https://attstadium.com/",
    seeking_talent=True)

venue8 = Venue(
    name="Soldier field",
    city="Chicago",
    state="illinois",
    address="1410 museum campus Dr, Chicago, IL 60605, United States",
    phone="1 312-235-7000",
    image_link="https://cdn.britannica.com/65/132265-050-48C4CE64/view-Soldier-Field-Chicago.jpg",
    genres = ["ALTERNATIVE","BLUES","FOLK","JAZZ","ROCK N ROLL"], 
    facebook_link="https://www.facebook.com/SoldierFieldChicago/",
    seeking_description="Soldier Field is an American football and soccer stadium located in the Near South Side of Chicago, Illinois, near Downtown Chicago",
    website="https://soldierfield.net/",
    seeking_talent=True)


venue9 = Venue(
    name="Levi's stadium",
    city="santa Clara",
    state="California",
    address="4900 Marie P Debartolo way, santa Clara, CA 95054, United States",
    phone="1 415-464-9377",
    image_link="https://www.levisstadium.com/wp-content/uploads/2015/12/TL11405.jpg",
    genres = ["ALTERNATIVE","BLUES","FOLK","JAZZ","ROCK N ROLL"], 
    facebook_link="https://www.facebook.com/levisstadium/",
    seeking_description="an American football stadium located in Santa Clara, California, in the San Francisco Bay Area.",
    website="https://www.levisstadium.com/",
    seeking_talent=True)


venue10 = Venue(
    name="hard rock stadium",
    city="Miami",
    state="Florida",
    address="347 Don shula Dr, Miami gardens, FL 33056, United States",
    phone="1 305-943-8000",
    image_link="https://ik.imagekit.io/grgdihc3l/crm/simpleview/image/upload/w_1440,h_900,c_fit/crm/miamifl/Hard-Rock-Stadium01_0221f18f-5056-a36a-0b96ae3a598c2b33.jpg",
    genres = ["ALTERNATIVE","BLUES","FOLK","JAZZ","ROCK N ROLL"], 
    facebook_link="https://www.facebook.com/HardRockStadium1/",
    seeking_description="a football stadium located in Miami Gardens, Florida, a city north of Miami. ",
    website="https://hardrockstadium.com/",
    seeking_talent=True)

venue11 = Venue(
    name="Mercedes Benz Superdome",
    city="new Orleans",
    state="Louisiana",
    address="1500 sugar bowl Dr, New Orleans, LA 70112, United States",
    phone="1 504-587-3663",
    image_link="https://seatgeek.com/images/performers-landscape/new-orleans-saints-3c7e5e/2069/720x450.jpg",
    genres = ["ALTERNATIVE","BLUES","FOLK","JAZZ","ROCK N ROLL"], 
    facebook_link="https://www.facebook.com/MBSuperdome/",
    seeking_description="The Mercedes-Benz Superdome, often referred to simply as the Superdome, is a domed sports and exhibition stadium",
    website="http://www.mbsuperdome.com/",
    seeking_talent=True)

db.session.add(venue1)
db.session.add(venue2)
db.session.add(venue3)
db.session.add(venue4)
db.session.add(venue5)
db.session.add(venue6)
db.session.add(venue7)
db.session.add(venue8)
db.session.add(venue9)
db.session.add(venue10)
db.session.add(venue11)


#Artists
#---------------------------------------------------------------------------#


artist1 = Artist(
    name = "Ed O'Brien",
    city = "Washinton",
    state = "Washington",
    genres = ['Soul','Rock n roll','Jazz'],
    days_available = ['Sunday','Monday'] ,
    image_link = "https://upload.wikimedia.org/wikipedia/commons/f/fa/Ed_O%27brien_2017.jpeg",
    facebook_link = "https://www.facebook.com/EOBBandOfficial/") 

artist2 = Artist(
    name = "Lady Gaga",
    city = "East Rutherford",
    state = "New Jersey",
    image_link="https://static01.nyt.com/images/2020/04/17/arts/17livestreaming-art/merlin_165419088_91aa9c0a-4695-4f1b-b4f8-ca0c80db740e-mediumSquareAt3X.jpg",
    facebook_link = "https://www.facebook.com/EOBBandOfficial/")


artist3 = Artist(
    name = "BTS",
    city = "Pasadena",
    state = "California",
    image_link = "https://www.nme.com/wp-content/uploads/2019/08/BTSSY_0518US_09.jpg",
    facebook_link = "https://www.facebook.com/bangtan.official/")
  
artist4 = Artist(
  name = "Kenny Chesney",
  city="Arlingtoon",
  state="Texas",
  image_link="https://a.vsstatic.com/mobile/app/concerts/kenny-chesney.jpg",
  facebook_link = "https://www.facebook.com/KennyChesney/")

artist5 = Artist(
  name="Ed Sheeran",
  city="Chicago",
  state="Illionis",
  image_link="https://images.sk-static.com/images/media/profile_images/artists/2083334/huge_avatar",
  facebook_link = "https://www.facebook.com/EdSheeranMusic/")

artist6 = Artist(
  name = "The Rolling Stones",
  city = "Santa Clara",
  state = "California",
  image_link = "https://image.cnbcfm.com/api/v1/image/105955225-1559919970926gettyimages-1134666717.jpeg?v=1560171885&w=678&h=381",
  facebook_link = "https://www.facebook.com/therollingstones/")

artist7 = Artist(
  name = "Green Day",
  city = "Miami",
  state = "Florida",
  image_link = "https://en.wikipedia.org/wiki/Green_Day#/media/File:Green_Day_2017_Germany.png",
  facebook_link = "https://www.facebook.com/GreenDay/")

    

db.session.add(artist1)
db.session.add(artist2)
db.session.add(artist3)
db.session.add(artist4)
db.session.add(artist5)
db.session.add(artist6)
db.session.add(artist7)


db.session.commit()