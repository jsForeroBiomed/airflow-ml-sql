import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()
np.random.seed(123)

N = 100

data = {
    "id_paciente": range(1001, 1001 + N),
    "edad": np.random.randint(18, 90, size=N),
    "sexo": np.random.choice(["M", "F"], size=N),
    "hipertension": np.random.choice([0, 1], size=N, p=[0.6, 0.4]),
    "diabetes": np.random.choice([0, 1], size=N, p=[0.7, 0.3]),
    "visitas_ultimo_mes": np.random.poisson(lam=2, size=N),
    "fecha_consulta": [fake.date_between(start_date='-7d', end_date='today') for _ in range(N)]
}

df = pd.DataFrame(data)


df.to_csv("data/nuevas_consultas.csv", index=False)
print("✅ Nuevos datos generados en 'data/nuevas_consultas.csv'")

