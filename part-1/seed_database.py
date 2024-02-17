from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import User, Movie, Rating, connect_to_db, db

DATABASE_URI = 'postgresql:///ratings'

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

def create_user(email, password):
    user = User(email=email, password=password)
    session.add(user)
    session.commit()
    return user

def create_movie(title, overview, release_date, poster_path):
    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)
    session.add(movie)
    session.commit()
    return movie

def create_rating(score, movie, user):
    rating = Rating(score=score, movie=movie, user=user)
    session.add(rating)
    session.commit()
    return rating

def seed_database():
    user1 = create_user(email='user1@example.com', password='password1')
    user2 = create_user(email='user2@example.com', password='password2')

    movie1 = create_movie(title='Movie 1', overview='Overview of Movie 1', release_date=datetime.now(), poster_path='/path/to/poster1.jpg')
    movie2 = create_movie(title='Movie 2', overview='Overview of Movie 2', release_date=datetime.now(), poster_path='/path/to/poster2.jpg')

    create_rating(score=5, movie=movie1, user=user1)
    create_rating(score=4, movie=movie1, user=user2)
    create_rating(score=3, movie=movie2, user=user1)
    create_rating(score=2, movie=movie2, user=user2)

if __name__ == "__main__":
    connect_to_db(db.app)
    seed_database()
