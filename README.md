# Civision - Interview Technique
## Application
- **Description**: Simple API Flask qui interroge l'API de France Travail pour requêter les offres d'emplois et 
calculer des statistiques sur l'évolution du marché du travail dans différentes communes et départements de France

## Démarrage
1. Exécuter la commande suivante pour installer les requirements:
`pip install -r requirements.txt`

2. Suivre les instructions sur le site pour générer un acces_token
    - `client_id`: PAR_jobtracker_067554f69afea6c4c87e8627899108efe3c03aea8c4fc26d7b2f2e9f664633a5
    - `client_secret`: 1162340281a8cfbfe42942691fb951abf88fe400b904aa9bc482100c80a9ed4b
    - `scope`: api_offresdemploiv2 o2dsoffre

3. Remplace le access_token à la ligne 13 du fichier `app.py` par le code nouvellement généré

4. Lancer le serveur avec la commande: `python app.py`

5. Faire une requête au endpoint `/fetch_today_jobs` pour obtenir les offres d'emplois postés lors de la journée en cours

6. Faire une requête au endpoint `/job_stats` pour obtenir des statistiques par rapport aux offres d'enplois des 3 derniers mois
