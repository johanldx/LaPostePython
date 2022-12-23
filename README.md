# La Poste Python

Bienvenue dans le ReadMe du module Python *laposte*. Le module permet d'intégrer les APIs de [La Poste](https://developer.laposte.fr/products) en Python de manière simple. Il est développé uniquement par moi-même Johan Ledoux et intègre pour l'instant uniquement l'[API de suivi de colis](https://developer.laposte.fr/products/suivi/2). Les autres APIs seront ajouté au code au fur et à mesure.

## Installation

*laposte* peut être installé via [pip](https://pypi.org/project/laposte/).

````bash
$ python -m pip install laposte
````

Il sera également nécessaire d'installer une version récente de *requests*.

````bash
$ python -m pip install requests
````

## Utilisation

Le module peut être utilisé de deux manières différentes via la class *Suivie()*.

Tout d'abord, on peut récupérer le résultat de la requête directement comme un dictionnaire python.

````python
client = laposte.Suivi()
client.connect("okapi_key")

informations = client.suivi("id_ship")
````

Une autre manière d'utiliser la classe pour récupérer les données d'un colis, est d'utiliser les attributs de classe.

````python
client = laposte.Suivi()
client.connect("okapi_key")
client.suivi("id_ship")

informations = [client.id_ship, client.product, client.timeline]

# Cette ligne permet de réinitialiser les attributs afin qu'ils ne soient plus accessibles et ainsi faire une nouvelle requête.
# L'argument client permet de réinitialiser également le client.
client.reset(client=False)
````

Bien sûr, il est aussi possible de combiner les deux manières de récupérer les informations.

Les attributs de classe servant à récupérer les informations sont les suivants :

````python
client.lang
client.return_code
client.scope
client.holder
client.id_ship
client.product
client.is_final
client.entry_date
client.event
client.timeline
client.context_data
client.data
````

## Le projet

Bien que les APIs de La Poste soient connus et utilisés, je n'ai pas trouvé de modules sur Pypi me convenant afin de les insérer dans mes projets. Je développe donc ce module afin de partager une manière simple et rapide à tous d'accéder aux APIs de La Poste.
