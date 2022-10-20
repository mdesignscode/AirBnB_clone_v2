#!/usr/bin/python3
"""DataBase Storage for Project"""

from os import getcwd, getenv, system
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """DataBase Storage for Project"""
    __engine = None
    __session = None

    def __init__(self):
        """creates the database engine"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        url = f'mysql+pymysql://{user}:{pwd}@{host}:3306/{db}'

        self.__engine = create_engine(url, pool_pre_ping=True)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

        if getenv('HBNB_ENV') == 'test':
            com = "echo 'DROP DATABASE IF EXISTS hbnb_dev_db;'"
            system(f"{com} | sudo mysql -u root -p")
            system(f'cat setup_mysql_dev.sql | sudo mysql -u root -p')

    def all(self, cls=None):
        """retrieves all objects related to a class"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        if cls is not None:
            objs = self.__session.query(cls).all()
            c = cls.__name__
            objs_dict = {f'{c}.{obj.id}': obj for obj in objs}
            return objs_dict

        else:
            classes = [City, State, User, Place, Review, Amenity]
            all_dict = {}
            for table in classes:
                query = self.__session.query(table).all()
                for obj in query:
                    c = table.__name__
                    all_dict[f'{c}.{obj.id}'] = obj

            return all_dict

    def new(self, obj):
        """adds the object to the database"""
        self.__session.add(obj)

    def save(self):
        """saves the object to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an obj from the database"""
        if obj is not None:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """create all tables in the database"""
        from models.base_model import Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)

    def close(self):
        """removes a session"""
        self.__session.remove()
