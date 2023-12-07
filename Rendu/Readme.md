# I. Faire joujou avec l'asynchrone
# 1. Premiers pas
# 🌞 sleep_and_print.py

Voici le fichier avec le code :)

[Click Here bro](sleep_and_print.py)

# 🌞 sleep_and_print_async.py

Voici le fichier avec le code ou on commence l'asynchrone :

[Click pour voir du asynchrone :)](sleep_and_print_async.py)

# 2. Web Requests
# 🌞 web_sync.py

Voici le fichier pour l'exo du web_sync ;)

[Je crois que c'est vers ici](web_sync.py)

# 🌞 web_async.py

J'ai rencontré des soucis de certificat lors de cet exercice, donc j'ai dû effectuer cette commande :

```bash
florentinfallon@MacBook-Pro-de-Florentin TP6 % brew install openssl
```

Après avoir effectué cette commande, tout est rentré dans l'ordre.

Voici le fichier avec le code pour le web async :

[ web_async.py]( web_async.py)

# 🌞 web_sync_multiple.py

voici le résultat de mon script :

```bash
florentinfallon@MacBook-Pro-de-Florentin TP6 % python3 web_sync_multiple.py url.txt
Processing URL: http://www.ynov.com
Writing content to: ./tmp/web_www.ynov.com.html
Writing content to file: ./tmp/web_www.ynov.com.html
Write complete
Done
Processing URL: http://generalairsoft.fr
Writing content to: ./tmp/web_generalairsoft.fr.html
Writing content to file: ./tmp/web_generalairsoft.fr.html
Write complete
Done
Processing URL: http://www.google.com
Writing content to: ./tmp/web_www.google.com.html
Writing content to file: ./tmp/web_www.google.com.html
Write complete
Done
```

Voici le fichier avec les commandes nécéssaire :

[Faut clicker ici ;)](web_sync_multiple.py)

# 🌞 web_async_multiple.py

J'ai eu encore le problème de certificat, mais cette fois je ne pouvais pas faire la commande donc j'ai fais cette ligne qui me permet de le désactiver mais je sais que ce n'est pas bien car la sécurité n'est plus la :

```bash
async with session.get(url, ssl=False) as response:
```

Voici le résultat au lancement du script :

```bash
florentinfallon@MacBook-Pro-de-Florentin TP6 % python3 web_async_multiple.py ici.txt
Processing URL: https://www.youtube.com
Processing URL: https://icones8.fr
Writing content to: ./tmp/web_www.youtube.com.html
Writing content to file: ./tmp/web_www.youtube.com.html
Write complete
Done
Writing content to: ./tmp/web_icones8.fr.html
Writing content to file: ./tmp/web_icones8.fr.html
Write complete
Done
```

Voici le fichier avec tout le code !

[web_async_multiple.py](web_async_multiple.py)

# 🌞 Mesure !

Voici les résultats :

* Pour le synchrone : ***Temps d'exécution (synchrone): 2.3495781421661377 secondes***

* Pour l'asynchrone : ***Temps d'exécution (asynchrone): 0.5203959941864014 secondes***


Voici les fichiers ou le code pour la mesure et disponible :

[web_sync_multiple.py](web_sync_multiple.py)

[web_async_multiple.py](web_async_multiple.py)

# II. Chat room
# 1. Intro
# 2. Première version
# 🌞 chat_server_ii_2.py

Voici le fichier pour le serveur :

[chat_server_ii_2.py](chat_server_ii_2.py)

# 🌞 chat_client_ii_2.py

Voici le fichier du client :

[chat_client_ii_2.py](chat_client_ii_2.py)

# 3. Client asynchrone
# 🌞 chat_client_ii_3.py

Voici le fichier pour le client :

[Client](chat_client_ii_3.py)

# 🌞 chat_server_ii_3.py

Voici le fichier pour le serveur :

[Serveur](chat_server_ii_3.py)


# 4. Un chat fonctionnel
# 🌞 chat_server_ii_4.py



# 5. Gérer des pseudos
# 🌞 chat_client_ii_5.py



# 🌞 chat_server_ii_5.py



# 6. Déconnexion
# 🌞 chat_server_ii_6.py et chat_client_ii_6.py



