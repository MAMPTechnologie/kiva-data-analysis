import pandas as pd
from datetime import datetime
import os

def generate_monthly_report():
    # 1. Chargement des données
    data_path = 'data/kiva_loans.csv'
    if not os.path.exists(data_path):
        print("❌ Erreur : Pas de données à analyser.")
        return

    df = pd.read_csv(data_path)
    
    # 2. Calculs stratégiques
    df['taux_financement'] = (df['funded_amount'] / df['loan_amount']) * 100
    global_rate = df['taux_financement'].mean()
    risky_loans = (df['taux_financement'] < 90).sum()
    
    # 3. Préparation du contenu du rapport
    date_str = datetime.now().strftime("%Y-%m-%d")
    report_filename = f"data/rapport_financier_{date_str}.txt"
    
    report_content = f"""
    ===========================================
    RAPPORT STRATÉGIQUE KIVA - {date_str}
    ===========================================
    
    SYNTHÈSE GLOBALE :
    ------------------
    - Taux de financement moyen : {global_rate:.2f}%
    - Nombre total de prêts à risque (PAR) : {risky_loans}
    
    ANALYSE PAR SECTEUR :
    --------------------
    {df.groupby('sector')['taux_financement'].mean().to_string()}
    
    RECOMMANDATION :
    ---------------
    L'audit montre que les secteurs ayant un taux inférieur à 85% 
    nécessitent une révision urgente des garanties.
    
    Document généré automatiquement par le Labo MAMPETechnologie.
    ===========================================
    """
    
    # 4. Écriture du fichier
    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write(report_content)
        
    print(f"✅ Rapport généré avec succès : {report_filename}")

if __name__ == "__main__":
    generate_monthly_report()