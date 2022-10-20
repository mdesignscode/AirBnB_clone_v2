#!/usr/bin/python3
""" """
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
from models.user import User
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    def test_reviews_getter(self):
        """tests the reviews getter attribute"""
        Florida = State(id='Florida', name='Florida')
        Miami = City(id='Miami', name='Miami', state_id='Florida')
        Isabelle_Houston = User(id="IsabelleHouston",
                                email="tonlaze@iz.cx",
                                password="XxeO7q")
        Coconut_Bay = Place(id="CoconutBay",
                            city_id="Miami",
                            user_id="IsabelleHouston",
                            name="Coconut_Bay",
                            number_rooms=1,
                            number_bathrooms=1,
                            max_guest=4,
                            price_by_night=280)
        Review_1 = Review(id="R1",
                          text="ujupipda_umikuhkog_wefbep_jezesuje.",
                          place_id="CoconutBay",
                          user_id="IsabelleHouston")
        Alfred_McCoy = User(id="AlfredMcCoy",
                            email="eb@panbawvu.la",
                            password="A34Zs4")
        Review_3 = Review(id="R3",
                          text="ca_hevho_vevaj_tum_ehtow_nerica_cuhab.",
                          place_id="CoconutBay",
                          user_id="AlfredMcCoy")
        New_York = State(id='NY', name='New York',)
        NYC = City(id='NYC', name='New York City', state_id='NY')
        Jesus_Stevenson = User(id="JesusStevenson",
                               email="vajip@uplu.sa",
                               password="mZgYew")
        Hampton = Place(id="Hampton",
                        city_id="NYC",
                        user_id="JesusStevenson",
                        name="Hampton",
                        number_rooms=2,
                        number_bathrooms=2,
                        max_guest=6,
                        price_by_night=360)
        Review_2 = Review(id="R2",
                          text="satzahif_dohazu_de_wenervo_dilfugsev_nidofti.",
                          place_id="Hampton",
                          user_id="JesusStevenson")

        objects = [
            Florida, Miami, NYC, New_York,
            Isabelle_Houston, Jesus_Stevenson, Review_1, Review_2,
            Hampton, Coconut_Bay, Alfred_McCoy, Review_3
        ]
        for obj in objects:
            obj.save()

        coconut_reviews = Coconut_Bay.reviews

        id_list = []
        for review in coconut_reviews:
            id_list.append(review.id)
        self.assertNotIn('R2', id_list)
