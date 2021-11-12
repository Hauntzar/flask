# basic1.py

## Create entries in the table

from models import db,Puppy,Owner,Toy

## creating 2 puppies
rufus=Puppy('Rufus')
fido=Puppy('Fido')

## add puppies to db
db.session.add_all([rufus,fido])
db.session.commit()

print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').all()[0]
print(rufus)
print(rufus.report_toys())

## create owner object
jose = Owner('Jose',rufus.id)

## give rufus some toys
toy1 = Toy('Chew Toy',rufus.id)
toy2 = Toy('Ballsack',rufus.id)

db.session.add_all([jose,toy1,toy2])
db.session.commit()

print(Puppy.query.all())
rufus = Puppy.query.filter_by(name='Rufus').all()[0]
print(rufus)
print(rufus.report_toys())