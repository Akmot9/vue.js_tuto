import psycopg2

# Paramètres de connexion à la base de données PostgreSQL
host = "localhost"
database = "messages"
user = "postgres"
password = "1706"

# Connexion à la base de données
conn = psycopg2.connect(host=host, database=database, user=user, password=password)

# Création d'un curseur pour exécuter des commandes SQL
cur = conn.cursor()

# Ajout d'une ligne à la table "mess"
cur.execute("INSERT INTO mess (id, text) VALUES (3, 'bonjour3')")

# Validation de la transaction
conn.commit()

# Fermeture du curseur et de la connexion à la base de données
cur.close()
conn.close()