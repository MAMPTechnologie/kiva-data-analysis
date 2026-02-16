import pandas as pd
import numpy as np

# Simulation de la structure Kiva
data = {
    'id': range(1001, 1101),
    'funded_amount': np.random.randint(100, 1000, 100),
    'loan_amount': np.random.randint(100, 1200, 100),
    'activity': np.random.choice(['Agriculture', 'Food', 'Retail', 'Services'], 100),
    'sector': np.random.choice(['Food', 'Agriculture', 'Arts'], 100),
    'country': np.random.choice(['Kenya', 'Philippines', 'Cambodia', 'Peru'], 100),
    'term_in_months': np.random.randint(6, 24, 100),
    'lender_count': np.random.randint(1, 40, 100),
}

df = pd.DataFrame(data)
# Sauvegarde dans le dossier data
df.to_csv('data/kiva_loans.csv', index=False)
print("✅ Fichier kiva_loans.csv (échantillon) créé dans le dossier data/ !")