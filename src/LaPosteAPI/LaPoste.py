import requests as req
import LaPosteExeptions as LaPostExept

class LaPoste():
    """
    This class allows you to retrieve the information of a package or a letter via the La Poste API
    """
    def __init__(self):
        self.__okapi_key = None
        self.lang = None
        self.__headers = None
    
    def __str__(self):
        if self.__okapi_key is None:
            return "LaPosteAPI (suivi) not connected"
        return "LaPosteAPI (suivi) connected"
    
    def connect(self, okapi_key:str, lang:str="fr_FR"):
        """Connect to the La Poste API

        Args:
            okapi_key (str): Okapi key provided by La Poste
            lang (str, optional): language. Defaults to "fr_FR".
        """
        self.__okapi_key = okapi_key
        self.__lang = lang
        self.__headers = {"Accept": "application/json", "X-Okapi-Key": okapi_key}
    
    def suivi(self, id_ship:str):
        """Track a package via the official La Poste API

        Args:
            id_ship (str): Parcel number

        Raises:
            LaPosteExeptions.InvalidNumberExeption: 400
            LaPosteExeptions.UnauthorizedExeption: 401
            LaPosteExeptions.ResourceNotFoundExeption: 404
            LaPosteExeptions.SystemErrorExeption: 500
            LaPosteExeptions.ServiceUnavailableExeption: 504
            LaPosteExeptions.LaPosteExeption: Error

        Returns:
            dict: Package Information
        """
        response = req.get(f"https://api.laposte.fr/suivi/v2/idships/{id_ship}?lang={self.__lang}", headers=self.__headers)
        response.encoding = "utf-8"
        data = response.json()
        
        if response.status_code == 200 or response.status_code == 207:
            return Suivi(return_code = data.get("returnCode"),
                         scope = data.get("scope"),
                         holder = data.get("shipment").get("holder"),
                         id_ship = data.get("shipment").get("idShip"),
                         product = data.get("shipment").get("product"),
                         is_final = data.get("shipment").get("isFinal"),
                         entry_date = data.get("shipment").get("entryDate"),
                         event = data.get("shipment").get("event"),
                         timeline = data.get("shipment").get("timeline"),
                         context_data = data.get("shipment").get("contextData"),
                         data = data)
        elif response.status_code == 400:
            raise LaPostExept.InvalidNumberExeption
        elif response.status_code == 401:
            raise LaPostExept.UnauthorizedExeption
        elif response.status_code == 404:
            raise LaPostExept.ResourceNotFoundExeption
        elif response.status_code == 500:
            raise LaPostExept.SystemErrorExeption
        elif response.status_code == 504:
            raise LaPostExept.ServiceUnavailableExeption
        else:
            raise LaPostExept.LaPosteExeption
    
    def close(self):
        """Disconnection of the La Poste API
        """
        self.__okapi_key = None
        self.__headers = None
            

class Suivi():
    def __init__(self, return_code, scope, holder, id_ship, product, is_final, entry_date, event, timeline, context_data, data):
        self.return_code = return_code
        self.scope = scope
        self.holder = holder
        self.id_ship = id_ship
        self.product = product
        self.is_final = is_final
        self.entry_date = entry_date
        self.event = event
        self.timeline = timeline
        self.context_data = context_data
        self.data = data
        
    def __str__(self):
        return f"Suivi {self.id_ship}"