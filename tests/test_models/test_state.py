#!/usr/bin/python3
""" """
from models.city import City
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_cities_getter(self):
        """tests the cities getter attribute"""
        Florida = State(id='Florida', name='Florida')
        Miami = City(id='Miami', name='Miami', state_id='Florida')
        Orlando = City(id='Orlando', name='Orlando', state_id='Florida')
        New_York = State(id='NY', name='New York',)
        NYC = City(id='NYC', name='New York City', state_id='NY')

        objects = [
            Florida, Miami, Orlando, NYC, New_York
        ]
        for obj in objects:
            obj.save()

        florida_cities = Florida.cities

        id_list = []
        for city in florida_cities:
            id_list.append(city.id)
        self.assertNotIn('NYC', id_list)
