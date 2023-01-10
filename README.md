# La Poste Python (Version 0.1.1)

Bienvenue sur la page Github du projet *LaPostePython* ! Ce module permet d'intégrer les API de [La Poste](https://developer.laposte.fr/products) dans vos programmes Python de manière relativement simple. Il intègre à l'heure d'aujourd'hui l'[API de suivi de colis](https://developer.laposte.fr/products/suivi/2) uniquement, les autres APIs seront ajouté au code au fur et à mesure.
Le code est développé et maintenu uniquement par moi même.

## Installation

Le module *laposte* peut être installé via [pip](https://pypi.org/project/laposte/).

````bash
$ python -m pip install laposte
````

Il sera également nécessaire d'installer une version récente de *requests*. (Si il n'est pas installé automatiquement.)

````bash
$ python -m pip install requests
````

## Utilisation

Le module s'utilise de manière très simple. Tout d'abord, il faut vous connecter à l'API de La Poste avec votre clé *Okapi*.

````python
from laposte import LaPoste

client = LaPoste()
client.connect(okapi_key="okapi_key")
````

Vous pouvez ensuite faire un requête à l'API afin de récupérer les informations de votre suivi.

````python
from laposte import LaPoste

client = LaPoste()
client.connect(okapi_key="okapi_key")

informations = client.suivi(id_ship="id_ship")
````

La fonction *suivi()* de la classe LaPoste renvoie les informations du colis via une instance de la classe Suivi.

Les attributs de classe servant à récupérer les informations sont les suivants :

````python
Suivi().return_code
Suivi().scope
Suivi().holder
Suivi().id_ship
Suivi().product
Suivi().is_final
Suivi().entry_date
Suivi().event
Suivi().timeline
Suivi().context_data
Suivi().data # toutes les données au formats JSON
````

## Exemples

### 1

````python
from laposte import LaPoste

client = LaPoste()
client.connect(okapi_key="OKAPIKEY562NOVNVOVE7899C9CH")

informations = client.suivi(id_ship="2M04841131282")

print(informations.product)
print(informations.entry_date)
````

Renvoie dans la console :
````
Lettre expert
2019-07-17T00:00:00+02:00
````

### 2

````python
from laposte import LaPoste

client = LaPoste()

informations = client.suivi(id_ship="2M04841131282")

print(informations.data)
````

Renvoie dans la console :
````
LaPosteExeptions.UnauthorizedExeption: Non-autorisé (absence de la clé Okapi)
````

## Le projet

Bien que La Poste soit une entreprise connue et que le suivi de colis soit au coeur de notre quotidien, je n'ai trouvé aucun module Python répondant à mes attentes en matière d'accès à cette API. C'est pour cette raison que j'ai développé LaPostePython.

## Liens 

[La documentation](lapostepython.readthedocs.io/fr/latest/)

[Le projet sur Pypi](https://pypi.org/project/laposte/)
