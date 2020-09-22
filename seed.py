"""Seed file to make sample data for db."""

from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()

Pet.query.delete()

p1 = Pet(name="Tala", species="Maine Coon",
         photo_url='https://images.unsplash.com/photo-1552944249-481c99e23e97?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80')

p2 = Pet(name='Lucky', species='Russian Tortoise',
         photo_url='https://images.unsplash.com/photo-1553272021-83514d6ac53d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60', available=False)


db.session.add_all([p1, p2])
db.session.commit()
