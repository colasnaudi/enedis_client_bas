# Enedis Sandbox API

## Language:
[Français](#français) <br>
- [À savoir](#à-savoir) <br>
    - [Limites d'appels](#limites-dappels) <br>
- [Installation générale](#installation-générale) <br>
- [Installation pour cette partie](#installation-pour-cette-partie) <br>
- [Clients fictifs](#clients-fictifs) <br>
- [Fonctions de l'API](#fonctions-de-lapi) <br>
    - [Obtenir un jeton d'accès](#obtenir-un-jeton-daccès) <br>
    - [Interroger des données de mesure](#interroger-des-données-de-mesure) <br>
    - [Interroger des données clients](#interroger-des-données-clients) <br>
    - [Les cas d'erreurs](#les-cas-derreurs) <br>

[English](#english) <br>
- [About](#about) <br>
    - [Call limits](#call-limits) <br>
- [General setup](#general-setup) <br>
- [Setup for this part](#setup-for-this-part) <br>
- [Fake clients](#fake-clients) <br>
- [API functions](#api-functions) <br>
    - [Get an access token](#get-an-access-token) <br>
    - [Interrogate measurement data](#interrogate-measurement-data) <br>
    - [Interrogate customer data](#interrogate-customer-data) <br>
    - [Error cases](#error-cases) <br>

# Français
## À savoir
### Limites d'appels
Les quotas suivants sont fixés par Enedis. Ils sont partagés par tous les utilisateurs du service Conso API.

Maximum de 5 requêtes par seconde
Maximum de 1000 requêtes par heure

Même si ces quotas peuvent sembler élevés, le serveur de Conso API est limité en ressources, et ne pourra rester gratuit que si tous les utilisateurs se comportent raisonnablement.

## Installation générale
`pip install -r requirements.txt`

## Installation pour cette partie
Allez sur https://datahub-enedis.fr/mon-compte-tableau-de-bord/mon-compte-applications/

Créez une nouvelle application sandbox et récupérez le client id et le client secret depuis le dashboard.

**Important !** : Créez un fichier `.env` à la racine de ce projet.
Mettez le contenu suivant dedans et remplacez les valeurs par celles de votre application.
```
CLIENT_ID=votre_client_id
CLIENT_SECRET=votre_client_secret
```

## Clients fictifs

| ID | PRM | DESC |
|----|-----|------|
| 0 | 22516914714270 | Client qui ne possède qu’un seul point de livraison de consommation pour lequel il a activé la courbe de charge. Ses données sont remontées de manière exacte (sans « trou » de données) et son compteur a été mis en service au début du déploiement Linky. |
| 1 | 11453290002823 | Client qui ne possède qu’un seul point de livraison de consommation pour lequel il a activé la courbe de charge. Ses données sont remontées de manière exacte (sans « trou » de données) et son compteur a été mis en service le 27 août 2019. |
| 2 | 32320647321714 | Client qui ne possède qu’un seul point de livraison de consommation pour lequel il n’a pas activé la courbe de charge. Ses données sont remontées de manière exacte (sans « trou » de données) et son compteur a été mis en service au début du déploiement Linky.
| 3 | 12345678901234 <br> 10284856584123 | Client qui possède un point de livraison de consommation et un point de livraison de production pour lesquels il a activé les courbes de charge. Ses données sont remontées de manière exacte (sans « trou » de données) et ses compteurs ont été mis en service au début du déploiement Linky.
| 4 | 42900589957123 | Client qui possède qu’un  seul point de livraison de consommation pour lequel il a activé la courbe de charge. Ses données présentent des « trous » de données les mardis et mercredis et son compteur a été mis en service au début du déploiement Linky
| 5 | 24880057139941 | Client qui possède qu’un seul point de livraison de production pour lequel il a activé la courbe de charge. Ses données sont remontées de manière exacte (sans « trou » de données) et son compteur a été mis en service au début du déploiement Linky.
| 6 | 12655648759651 | Client qui possède un point de livraison d’ auto-consommation pour lequel il a activé la courbe de charge en production et en consommation. Pour chaque point prélevé, lorsque la consommation est supérieur à la production les données de consommation remontées correspondent à la consommation moins la production et la production est nulle. Inversement lorsque la production est supérieure à la consommation. Ses données sont remontées de manière exacte (sans « trou » de données) et son compteur a été mis en service au début du déploiement Linky.
| 7 | 64975835695673 <br> 63695879465986 <br> 22315546958763 | Client qui possède trois points de livraison de consommation  pour lesquels il a activé les courbes de charge. Ses données sont remontées de manière exacte (sans « trou » de données) et ses compteurs ont été mis en service au début du déploiement Linky.
| 8 | 26584978546985 | Client qui donne son consentement mais le révoque immédiatement après l’avoir donné. |

# Fonctions de l'API
Dans le bac à sable, des clients factices vous permettront d’utiliser les API. L’API Authorize permettant de donner un consentement ne sera nécessaire qu’en production avec les vrais clients. Dans le bac à sable, vous disposez d’office du consentement de tous les clients factices.

# Obtenir un jeton d'accès
> `get_access_token(self)`

Remplacez les champs :
- `client_id` et `client_secret` par l’identifiant et le secret de votre application reçus au moment de sa création.

En retour, vous récupérez le jeton d’accès (`access_token`) qui est la clé d’entrée auprès d’Enedis pour les données auxquelles le client vient de vous donner accès. Il a une durée de validité de 3h30.

<hr>

# Interroger des données de mesure

Une fois le consentement du client enregistré par Enedis et l’obtention d’un jeton d’accès, vous pouvez accéder aux différentes données de mesures exposées par les API Enedis Data Connect :

Consommation quotidienne,
- Puissance maximale de consommation quotidienne,
- Courbe de consommation au pas 30 minutes,
- Production quotidienne,
- Courbe de production au pas 30 minutes.

Ces données sont les éléments renvoyés par les sous-ressources de l’API appelée « Metering Data ». Voyons comment interroger chaque donnée.

### La consommation quotidienne
> `get_daily_consumption(self, access_token, start, end, usage_point_id)`

Cette sous-ressource renvoie la consommation d’énergie par jour, en Wh, sur les journées demandées.
Remplacez les champs :

- `start` et `end` par les jours de début et de fin de la période pour lesquels vous souhaitez obtenir des données, au format YYYY-MM-DD,
- `access_token` par le jeton d’accès,
- `usage_point_id` par l’identifiant du point d’usage de l’utilisateur fictif désiré.

Les appels sont unitaires, c’est à dire pour un seul client et un seul point d’usage. A chaque demande de votre part, on vérifiera si le consentement est toujours valide. En effet le client pourrait avoir changé d’avis entre temps et vous recevriez alors un message d’erreur vous avertissant de l’absence de consentement !


### La puissance maximale de consommation
>`get_daily_consumption_max_power(self, access_token, start, end, usage_point_id)`

La sous-ressource « puissance maximale de consommation» renvoie le pic de puissance instantanée consommée (en VA) atteint dans la journée, ainsi que l’heure d’atteinte du pic avec le fuseau horaire correspondant.

### La courbe de consommation
>`get_consumption_load_curve(self, access_token, start, end, usage_point_id)`

La courbe de consommation correspond à la puissance soutirée par le client moyennée sur des plages par défaut de 30 minutes, pour des raisons technique cet intervalle peut être différent et il est renseigné à travers le paramètre interval_length sous le format PT**M (avec ** le nombre de minutes). Elle est exprimée en Watt.

### La production quotidienne
>`get_daily_production(self, access_token, start, end, usage_point_id)`

Cette sous-ressource renvoie la production d’énergie par jour, en Wh, sur les journées demandées.

### La courbe de production
>`get_production_load_curve(self, access_token, start, end, usage_point_id)`

La courbe de consommation correspond à la puissance soutirée par le client moyennée sur des plages par défaut de 30 minutes, pour des raisons technique cet intervalle peut être différent et il est renseigné à travers le paramètre interval_length sous le format PT**M (avec ** le nombre de minutes). Elle est exprimée en Watt.

# Interroger des données clients

L’API Customers permet d‘obtenir les informations contractuelles et techniques d’un client ayant donné son consentement pour les partager. Cette API vous permet d’obtenir :

- L’identité du client,
- Les coordonnées du client,
- Les contrats du client,
- L’adresse de ses points d’usage.

Attention, les données clients sont uniquement disponibles pour les clients ayant au moins un point de livraison (PDL ou PRM) de consommation et ces données ne peuvent provenir qu’en faisant une requête sur un de leurs points de livraison de consommation.

### Récupération de l’identité d’un client :
>`get_identity(self, access_token, usage_point_id)`

Cette sous-ressource permet la récupération des données d’identité d’un client. La requête cURL pour obtenir cette information prend en paramètre le jeton d’autorisation et le numéro de point d’usage du client.

Remplacez le champ :

- `access_token` par le jeton d’accès,
- `usage_point_id` par l’identifiant du point d’usage de l’utilisateur fictif désiré.

### Récupération des données de contact d’un client
>`get_contact_data(self, access_token, usage_point_id)`

Cette sous-ressource permet de récupérer les données de contact d’un client. Comme la sous-ressource précédente, l’appel à l’API nécessite le jeton d’autorisation et l’identifiant du point d’usage.

### Obtention des données contractuelles d’un client
>`get_usage_points_contracts(self, access_token, usage_point_id)`

La sous-ressource contracts permet d’obtenir les données contractuelles d’un client par points d’usage. L’appel à cette sous-ressource peut se faire de la même manière que les appels précédents, c’est-à-dire en utilisant le jeton et l’identifiant du point d’usage.

Remplacez les champs :

- `access_token` par le jeton d’accès,
- `usage_point_id` par l’identifiant des points d’usage du client. 

### Obtention des adresses des points d’usage
>`get_usage_points_addresses(self, access_token, usage_point_id)`

Cette sous-ressource permet d’obtenir l’adresse du point de livraison ou de production du client. Comme pour l’appel précédent, l’appel se fait avec un jeton d’accès en rajoutant en paramètre le ou les identifiants des points souhaités.

# Les cas d'erreurs

Le bac à sable vous permettra aussi de voir comment sont gérés les cas d’erreur les plus courants. Pour plus de détails sur ces erreurs, nous vous invitons à consulter la [documentation technique](https://datahub-enedis.fr/services-api/data-connect/documentation/description-des-erreurs/).

# English

## About
### Call limits
The following quotas are set by Enedis. They are shared by all users of the Conso API service.

Maximum of 5 requests per second
Maximum of 1000 requests per hour

Even if these quotas may seem high, the Conso API server is limited in resources, and will only remain free if all users behave reasonably.

## General setup
`pip install -r requirements.txt`

## Setup for this part
Go to https://datahub-enedis.fr/mon-compte-tableau-de-bord/mon-compte-applications/

Create a new app sandbox and get the client id and client secret from the dashboard.

**Important !** : Create a `.env`file at the root of this project.
Put the following content in it and replace the values with the value of your app.
```
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
```

## Fake clients

| ID | PRM | DESC |
|----|-----|------|
| 0 | 22516914714270 | Client who has only one consumption delivery point for which he has activated the load curve. Its data is reported exactly (without "hole" of data) and its meter has been put into service at the beginning of the Linky deployment. |
| 1 | 11453290002823 | Client who has only one consumption delivery point for which he has activated the load curve. Its data is reported exactly (without "hole" of data) and its meter has been put into service on August 27, 2019. |
| 2 | 32320647321714 | Client who has only one consumption delivery point for which he has not activated the load curve. Its data is reported exactly (without "hole" of data) and its meter has been put into service at the beginning of the Linky deployment.
| 3 | 12345678901234 <br> 10284856584123 | Client who has a consumption delivery point and a production delivery point for which he has activated the load curves. Its data is reported exactly (without "hole" of data) and its meters have been put into service at the beginning of the Linky deployment.
| 4 | 42900589957123 | Client who has only one consumption delivery point for which he has activated the load curve. Its data has "holes" of data on Tuesdays and Wednesdays and its meter has been put into service at the beginning of the Linky deployment.
| 5 | 24880057139941 | Client who has only one production delivery point for which he has activated the load curve. Its data is reported exactly (without "hole" of data) and its meter has been put into service at the beginning of the Linky deployment.
| 6 | 12655648759651 | Client who has a self-consumption delivery point for which he has activated the load curve in production and consumption. For each point taken, when the consumption is greater than the production the consumption data reported corresponds to the consumption minus the production and the production is zero. Conversely when production is greater than consumption. Its data is reported exactly (without "hole" of data) and its meter has been put into service at the beginning of the Linky deployment.
| 7 | 64975835695673 <br> 63695879465986 <br> 22315546958763 | Client who has three consumption delivery points for which he has activated the load curves. Its data is reported exactly (without "hole" of data) and its meters have been put into service at the beginning of the Linky deployment.
| 8 | 26584978546985 | Client who gives his consent but revokes it immediately after giving it. |

# API functions
In the sandbox, fake clients will allow you to use the APIs. The Authorize API to give consent will only be necessary in production with real clients. In the sandbox, you have the consent of all fake clients.

# Get an access token
> `get_access_token(self)`

Replace the `client_id` and `client_secret` fields with the identifier and secret of your application received when it was created.

In return, you get the access token (`access_token`) which is the key to Enedis for the data to which the client has just given you access. It has a validity period of 3h30.

<hr>

# Interrogate measurement data

Once the client's consent has been registered by Enedis and the access token has been obtained, you can access the different measurement data exposed by the Enedis Data Connect APIs:

Daily consumption,
- Maximum daily consumption power,
- Consumption curve at 30 minute intervals,
- Daily production,
- Production curve at 30 minute intervals.

This data is the elements returned by the sub-resources of the API called "Metering Data". Let's see how to query each data.

### Daily consumption
> `get_daily_consumption(self, access_token, start, end, usage_point_id)`

This sub-resource returns the energy consumption per day, in Wh, on the requested days.

Replace the fields:

- `start` and `end` by the start and end days of the period for which you want to obtain data, in YYYY-MM-DD format,
- `access_token` by the access token,
- `usage_point_id` by the identifier of the usage point of the desired fictitious user.

Calls are unitary, i.e. for a single client and a single usage point. Each request from you will check if the consent is still valid. Indeed the client could have changed his mind in the meantime and you would receive an error message warning you of the absence of consent!

### Maximum consumption power
>`get_daily_consumption_max_power(self, access_token, start, end, usage_point_id)`

The sub-resource "maximum consumption power" returns the maximum instantaneous power consumed (in VA) reached in the day, as well as the time of reaching the peak with the corresponding time zone.

### Consumption curve
>`get_consumption_load_curve(self, access_token, start, end, usage_point_id)`

The consumption curve corresponds to the power drawn by the customer averaged over default 30-minute periods, for technical reasons this interval may be different and it is indicated through the interval_length parameter in the format PT**M (with ** the number of minutes). It is expressed in Watt.

### Daily production
>`get_daily_production(self, access_token, start, end, usage_point_id)`

This sub-resource returns the energy production per day, in Wh, on the requested days.

### Production curve
>`get_production_load_curve(self, access_token, start, end, usage_point_id)`

The consumption curve corresponds to the power drawn by the customer averaged over default 30-minute periods, for technical reasons this interval may be different and it is indicated through the interval_length parameter in the format PT**M (with ** the number of minutes). It is expressed in Watt.

# Interrogate customer data

The Customers API allows you to obtain the contractual and technical information of a customer who has given his consent to share them. This API allows you to obtain:

- The identity of the customer,
- The customer's contact details,
- The customer's contracts,
- The address of his usage points.

Attention, customer data is only available for customers with at least one consumption delivery point (PDL or PRM) and this data can only come from a request on one of their consumption delivery points.

### Retrieving a customer's identity:
>`get_identity(self, access_token, usage_point_id)`

This sub-resource allows the retrieval of a customer's identity data. The cURL request to obtain this information takes as parameters the authorization token and the customer's usage point number.

Replace the field:

- `access_token` by the access token,
- `usage_point_id` by the identifier of the usage point of the desired fictitious user.

### Retrieving a customer's contact data
>`get_contact_data(self, access_token, usage_point_id)`

This sub-resource allows you to retrieve a customer's contact data. As with the previous sub-resource, the call to the API requires the token and the usage point identifier.

### Obtaining a customer's contractual data
>`get_usage_points_contracts(self, access_token, usage_point_id)`

The contracts sub-resource allows you to obtain a customer's contractual data by usage points. The call to this sub-resource can be done in the same way as the previous calls, i.e. by using the token and the usage point identifier.

Replace the fields:

- `access_token` by the access token,
- `usage_point_id` by the identifier of the customer's usage points.

### Obtaining the addresses of the usage points
>`get_usage_points_addresses(self, access_token, usage_point_id)`

This sub-resource allows you to obtain the address of the customer's delivery or production point. As for the previous call, the call is made with an access token by adding the identifier(s) of the desired points as a parameter.

# Error cases

The sandbox will also allow you to see how the most common error cases are handled. For more details on these errors, please refer to the [technical documentation](https://datahub-enedis.fr/services-api/data-connect/documentation/description-des-erreurs/).