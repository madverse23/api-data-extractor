import requests
import pandas as pd

def extraire_donnees_api():
    # L'URL de l'API (ici, l'annuaire des universités françaises)
    url = "http://universities.hipolabs.com/search?country=France"
    print(" Connexion à l'API en cours...")

    
    reponse = requests.get(url)

    # Si l'API répond avec le code 200 
    if reponse.status_code == 200:
        donnees_json = reponse.json()
        print(f"✅ Succès ! {len(donnees_json)} universités trouvées.")

        # On transforme le texte brut (JSON) en un beau tableau de données avec Pandas
        df = pd.DataFrame(donnees_json)

        # on ne garde que les colonnes intéressantes
        df_nettoye = df[['name', 'web_pages']]
        df_nettoye.columns = ['Nom_Universite', 'Site_Web'] # On renomme les colonnes

        # Sauvegarde des données dans un fichier CSV
        nom_fichier = "donnees_universites.csv"
        df_nettoye.to_csv(nom_fichier, index=False, encoding='utf-8-sig', sep=';')
        
        print(f"📁 Tableau généré et sauvegardé sous : {nom_fichier}")
    
    else:
        print(f"❌ Erreur de connexion. Code erreur : {reponse.status_code}")

if __name__ == "__main__":
    extraire_donnees_api()