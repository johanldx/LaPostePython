class LaPosteExeption(Exception):
    def __str__(self):
        return "Erreur inconnue s'est produite"

class InvalidNumberExeption(Exception):
    def __str__(self):
        return "Numéro invalide (ne respecte pas la syntaxe définie)"

class UnauthorizedExeption(Exception):
    def __str__(self):
        return "Non-autorisé (absence de la clé Okapi)"
        
class ResourceNotFoundExeption(Exception):
    def __str__(self):
        return "Ressource non trouvée"

class SystemErrorExeption(Exception):
    def __str__(self):
        return "Erreur système (message non généré par l’application)"
    
class ServiceUnavailableExeption(Exception):
    def __str__(self):
        return "Service indisponible (erreur technique sur service tiers)"