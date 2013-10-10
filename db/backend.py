#!/usr/bin/env python
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from abstract_backend import AbstractBackend
from tornado.options import options

class Backend(AbstractBackend):

    """
    The simple implementation of data access layer
    """

    def __init__(self):
        self._engine = create_engine('sqlite:///' + options.db, echo=True)
        self._metadata = MetaData(bind=self._engine)
        self._sessionmaker = sessionmaker(bind=self._engine)

    @classmethod
    def instance(self):
        if not hasattr(self, "_instance"):
            self._instance = self()
        return self._instance

    def get_metadata(self):
        return self._metadata

    def get_sessionmaker(self):
        return self._sessionmaker

    def get_engine(self):
        return self._engine
