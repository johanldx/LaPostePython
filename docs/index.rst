La Poste Python
=======

Bienvenue sur la documentation du module Python **laposte**. Il permet d'insérer les APIs de La Poste en Python et de simplifier ses utilisations. Il est développé par Johan Ledoux (ldx) en Open Source pour un besoin personnel à la base. Il ne contient acctueleemnt que l'API de suivi de colis mais les autres API seront par la suite implémentés.

.. important::

    Seule l'API de suivi de colis est actuellement implémenté.

Installation
----------

Le module **laposte** peut être installé avec `pip <https://pypi.org/project/laposte/>`_

.. code-block:: bash

  $ python -m pip install requests
  
  $ python -m pip install laposte
  
Il peut aussi être téléchargé depuis la page `github <https://github.com/444ldx/LaPostePython/releases/>`_ du projet.

Utilisation
-----

Le module peut être utilisé de deux manières différentes via la class *Suivie()*. 

Tout d'abord, on peut récupérer le résultat de la requête directement comme un dictionnaire python.

.. code-block:: python
  
  client = laposte.Suivi()
  client.connect("okapi_key")
  
  informations = client.suivi("id_ship")
  
Une autre manière d'utiliser la classe pour récupérer les données d'un colis, est d'utiliser les attributs de classe.

.. code-block:: python
  
  client = laposte.Suivi()
  client.connect("okapi_key")
  client.suivi("id_ship")
  
  informations = [client.id_ship, client.product, client.timeline]
  
  # Cette ligne permet de réinitialiser les attributs afin qu'ils ne soient plus accessibles et ainsi faire une nouvelle requête.
  # L'argument client permet de réinitialiser également le client.
  client.reset(client=False)


Bien sûr, il est aussi possible de combiner les deux manières de récupérer les informations.

Les attributs de classe servant à récupérer les informations sont les suivants :

.. code-block:: python

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

License
-------

**laposte** est mis à disposition sous la licence MIT. Pour plus de détails, voir `LICENSE.txt <https://github.com/444ldx/LaPostePython/blob/main/LICENSE>`_.
