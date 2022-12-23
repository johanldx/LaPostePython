import requests as req
import laposte.LaPosteExeptions as LaPostExept

class Suivi():
    """
    This class allows you to retrieve the information of a package or a letter via the La Poste API
    """
    def __init__(self):
        self.__okapi_key = None
        self.lang = None
        self.__headers = None
        
        self.return_code = None
        self.scope = None
        self.holder = None
        self.id_ship = None
        self.product = None
        self.is_final = None
        self.entry_date = None
        self.event = None
        self.timeline = None
        self.context_data = None
        self.data = None
        
        self.__set_attributes_values(LaPostExept.UnauthorizedExeption())
    
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
        self.__set_attributes_values(LaPostExept.InvalidNumberExeption())
        
    def __set_attributes_values(self, exeption):
        """Set attribute values when empty

        Args:
            exeption (class): la_poste_exeptions
        """
        self.return_code = exeption
        self.scope = exeption
        self.holder = exeption
        self.id_ship = exeption
        self.product = exeption
        self.is_final = exeption
        self.entry_date = exeption
        self.event = exeption
        self.timeline = exeption
        self.context_data = exeption
        self.data = exeption
    
    def __update_data(self, data):
        """Updated package information data

        Args:
            data (dict): JSON response from La Poste API
        """
        self.return_code = data.get("returnCode")
        self.scope = data.get("scope")
        self.holder = data.get("shipment").get("holder")
        self.id_ship = data.get("shipment").get("idShip")
        self.product = data.get("shipment").get("product")
        self.is_final = data.get("shipment").get("isFinal")
        self.entry_date = data.get("shipment").get("entryDate")
        self.event = data.get("shipment").get("event")
        self.timeline = data.get("shipment").get("timeline")
        self.context_data = data.get("shipment").get("contextData")
        self.data = data
    
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
            self.__update_data(data)
            return data
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
    
    def reset(self, client:bool=False):
        """Reset the information of the previous package

        Args:
            client (bool, optional): Also reset Client informations. Defaults to False.
        """
        if client:
            self.__okapi_key = None
            self.lang = None
            self.__headers = None
            self.__set_attributes_values(LaPostExept.UnauthorizedExeption())
        else:
            self.__set_attributes_values(LaPostExept.InvalidNumberExeption())