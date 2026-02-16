import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyse_portefeuille():
    # 1. Chargement
    path = 'data/kiva_loans.csv'
    if not os.path.exists(path):
        print("❌ Fichier introuvable !")
        return
        
    df = pd.read_csv(path)
    
    # 2. Calculs (KPIs)
    df['taux_financement'] = (df['funded_amount'] / df['loan_amount']) * 100
    df['est_a_risque'] = df['taux_financement'] < 90
    
    # 3. Groupement
    rapport = df.groupby('sector').agg({
        'loan_id': 'count',
        'taux_financement': 'mean',
        'est_a_risque': 'sum'
    }).rename(columns={'loan_id': 'Nombre de Prêts', 'est_a_risque': 'Prêts à Risque'})
    
    # 4. Affichage texte
    print("\n--- ANALYSE DÉCISIONNELLE KIVA ---")
    print(rapport)

    # 5. Visualisation (Doit être INDENTÉ à l'intérieur de la fonction)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=rapport.index, y='taux_financement', data=rapport, palette='viridis')
    plt.title('Taux de Financement moyen par Secteur')
    plt.ylabel('Taux de Financement (%)')
    plt.xlabel('Secteur d\'activité')
    
    # Sauvegarde
    plt.savefig('data/kiva_report_viz.png')
    print("\n✅ Graphique généré avec succès dans : data/kiva_report_viz.png")

if __name__ == "__main__":
    analyse_portefeuille()