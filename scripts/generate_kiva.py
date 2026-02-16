import pandas as pd
import numpy as np
import os

def generate_mock_kiva(n=1000):
    np.random.seed(42)
    data = {
        'loan_id': range(1, n + 1),
        'sector': np.random.choice(['Agriculture', 'Food', 'Retail', 'Services', 'Education'], n),
        'country': np.random.choice(['Kenya', 'Philippines', 'Cambodia', 'Peru', 'Senegal'], n),
        'loan_amount': np.random.randint(100, 2000, n),
        'funded_amount': [0] * n,
        'status': np.random.choice(['funded', 'in_progress', 'expired'], n, p=[0.7, 0.2, 0.1])
    }
    
    df = pd.DataFrame(data)
    # Simulation du montant financé : les 'funded' sont à 100%, les autres varient
    df['funded_amount'] = df.apply(lambda x: x['loan_amount'] if x['status'] == 'funded' 
                                   else np.random.randint(0, x['loan_amount']), axis=1)
    
    output_path = '/app/data/kiva_loans.csv'
    df.to_csv(output_path, index=False)
    print(f"✅ Dataset simule cree avec {n} lignes dans {output_path}")

if __name__ == "__main__":
    generate_mock_kiva()