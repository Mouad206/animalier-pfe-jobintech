from services.log_service import LogService


class LoggerConfig:

    _instance = None

    def __init__(self):

        if LoggerConfig._instance is not None:
            raise Exception("Singleton already created")

    @classmethod
    def getInstance(cls):

        if cls._instance is None:
            cls._instance = LoggerConfig()

        return cls._instance

    def log(self, niveau, utilisateur_id, message):

        # envoyer vers service logs
        LogService.log(niveau, utilisateur_id, message)