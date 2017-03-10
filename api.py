from config import Configure

class IntranetAPI():
    """
    Simple AutoLogin API
    """

    def __init__(self, config):
        if not isinstance(config, Configure):
            raise TypeError("Invalid instance of Configure")
        if config.getAuth() == "None":
            raise ValueError("Please check auth key")
        self._config = config
        self._host = "https://intra.epitech.eu/"
        self._format = "json"

    def getHost(self):
        return self._host

    def getConfig(self):
        return self._config

    def getFormat(self):
        return self._format

    def setHost(self, host):
        self._host = host

    def setConfig(self, config):
        self._config = config

    def setFormat(self, format):
        self._format = format

    def urlFormated(self, middle):
        return self._host + self._config.getAuth() + "/" + middle + "?format=" + self._format

    def urlFormatedWithUser(self, middle, login):
        return self._host + self._config.getAuth() + "/user/" + login + "/" + middle + "?format=" + self._format