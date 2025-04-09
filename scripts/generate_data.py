import pandas as pd
import numpy as np
from faker import Faker
import random


fake = Faker()
np.random.seed(42)


N = 1000


data = {
    "id_paciente": range(1, N + 1),
    "edad": np.random.randint(18, 90, size=N),
    "sexo": np.random.choice(["M", "F"], size=N),
    "hipertension": np.random.choice([0, 1], size=N, p=[0.6, 0.4]),
    "diabetes": np.random.choice([0, 1], size=N, p=[0.7, 0.3]),
    "visitas_ultimo_mes": np.random.poisson(lam=2, size=N),
    "fecha_consulta": [fake.date_between(start_date='-90d', end_date='today') for _ in range(N)],
}

df = pd.DataFrame(data)


df["hospitalizado_en_30d"] = df.apply(
    lambda row: int(
        (row["edad"] > 65 and row["hipertension"] and row["diabetes"]) or
        (row["visitas_ultimo_mes"] > 4)
    ), axis=1
)


df.to_csv("data/historico.csv", index=False)

print("✅ Dataset generado con éxito en 'data/historico.csv'")
