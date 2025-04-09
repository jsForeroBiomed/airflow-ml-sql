import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_model():
    df = pd.read_csv("/opt/airflow/data/historico.csv")

    df["sexo"] = df["sexo"].map({"M": 0, "F": 1})

    X = df[["edad", "sexo", "hipertension", "diabetes", "visitas_ultimo_mes"]]
    y = df["hospitalizado_en_30d"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    joblib.dump(clf, "models/modelo_entrenado.pkl")

    print("✅ Modelo entrenado y guardado correctamente.")

