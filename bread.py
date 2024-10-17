
import mysql.connector

# je me connecte à la base de données
connexion = mysql.connector.connect(
        host="localhost",
        user="your username",
        password="your password",
        database="name of your database"
    )
print("Connexion établie à la base de données")



def create_user(name, email):
    cursor = connexion.cursor()
    # Insertion des données dans la table
    cursor.execute("""
            INSERT INTO utilisateurs (name, email)
            VALUES (%s, %s)
        """, (name, email))

    # Validation de la transaction
    connexion.commit()

    # Vérification de l'insertion
    print("Données insérées avec succès")
    

    # Fermeture du curseur
    cursor.close()

# Appel de la fonction
create_user("kevin", "kevin@gmail.com")

# Fermeture de la connexion
connexion.close()