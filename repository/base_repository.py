from database.db import get_connection


class BaseRepository:

    @staticmethod
    def get_connection():
        return get_connection("aniservice_home")