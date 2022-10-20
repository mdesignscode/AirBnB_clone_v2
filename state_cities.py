#!/usr/bin/python3
"""Create dummy states and cities"""

from models import storage
from models.state import State
from models.city import City


# Create States
Palau = State(id='Palau', name='Palau')
Seychelles = State(id='Seychelles', name='Seychelles')
Australia = State(id='Australia', name='Australia')
Jordan = State(id='Jordan', name='Jordan')
Réunion = State(id='Réunion', name='Réunion')

# create Cities
Goojze = City(id='Goojze', name='Goojze', state_id='Palau')
Sivvafhud = City(id='Sivvafhud', name='Sivvafhud', state_id='Palau')
Afaracesi = City(id='Afaracesi', name='Afaracesi', state_id='Seychelles')
Rirdodis = City(id='Rirdodis', name='Rirdodis', state_id='Seychelles')
Virozite = City(id='Virozite', name='Virozite', state_id='Australia')
Jalufu = City(id='Jalufu', name='Jalufu', state_id='Australia')
Desfotfi = City(id='Desfotfi', name='Desfotfi', state_id='Réunion')
Gujjujbik = City(id='Gujjujbik', name='Gujjujbik', state_id='Réunion')
Linoju = City(id='Linoju', name='Linoju', state_id='Jordan')
Memilah = City(id='Memilah', name='Memilah', state_id='Jordan')

# saving objects
objects = [
    Palau, Seychelles, Australia,
    Jordan, Réunion, Memilah,
    Linoju, Gujjujbik, Desfotfi,
    Jalufu, Virozite, Rirdodis,
    Afaracesi, Sivvafhud, Goojze
]

for object in objects:
    object.save()

# all objects
# {print(f"{k} :: {v}\n\n") for k, v in storage.all().items()}

# get all cities from all states
print(Australia.cities)
