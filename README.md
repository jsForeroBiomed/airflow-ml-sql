# Proyecto Airflow - Predicción de Hospitalización

## Descripción
Este proyecto utiliza **Airflow** para orquestar dos flujos:
1. **Entrenamiento de un modelo de predicción** basado en datos históricos.
2. **Predicción de riesgo de hospitalización** en pacientes utilizando datos nuevos.

El proyecto usa **PostgreSQL** para almacenar los datos de entrada y las predicciones.

## Requisitos

- Docker y Docker Compose
- Python 3.7+
- Acceso a base de datos PostgreSQL (usado en contenedor)

## Pasos para ejecutar el proyecto

### 1. Clonar el repositorio
Clona el repositorio a tu máquina local:

```
git clone <tu-repositorio>
cd <tu-repositorio>
```

### 2. Crear y activar el entorno virtual
Es recomendable crear un entorno virtual para gestionar las dependencias:

```
python -m venv airflow-env
source airflow-env/bin/activate
```

### 3. Instalar las dependencias
Instala todas las dependencias necesarias:
```
pip install -r requirements.txt
```

### 4. Levantar los contenedores con Docker
El proyecto utiliza Docker para levantar Airflow y PostgreSQL. Usa el siguiente comando para levantar los contenedores:
```
docker compose up --build
```

Este comando construirá y levantará todos los servicios necesarios (Airflow, PostgreSQL).

### 5. Acceder a la interfaz de Airflow
Una vez que los contenedores estén corriendo, abre tu navegador y accede a la interfaz web de Airflow en:

```
http://localhost:8081
```

### 6. Ejecutar el DAG de entrenamiento
En la interfaz de Airflow, ejecuta el DAG train_model_dag para entrenar el modelo. Este DAG utilizará los datos históricos para entrenar el modelo de predicción de hospitalización.

### 7. Ejecutar el DAG de predicción
Después de entrenar el modelo, ejecuta el DAG predict_model_dag para predecir el riesgo de hospitalización en nuevos pacientes. Las predicciones se guardarán en la base de datos PostgreSQL en la tabla predicciones.

### 8. Verificar los resultados
Para verificar los datos de entrada, usa la consulta:
```
SELECT * FROM datos_entrada;
```

Para verificar las predicciones, usa la consulta:
```
SELECT * FROM predicciones;
```

### 9. Detener los contenedores
Cuando hayas terminado, puedes detener los contenedores con:
```
docker compose down
```

## Estructura del Proyecto
```
.
├── dags/
│   ├── train_model_dag.py       # DAG para entrenar el modelo
│   └── predict_model_dag.py     # DAG para predecir con el modelo entrenado
├── data/
│   ├── historico.csv            # Datos históricos para entrenar el modelo
│   └── nuevas_consultas.csv     # Nuevas consultas para predicción
├── scripts/
│   └── cargar_historico_a_db.py # Script para cargar datos históricos en la DB
├── models/
│   └── modelo_entrenado.pkl     # Modelo entrenado guardado
└── docker-compose.yml           # Configuración de contenedores (Airflow, PostgreSQL)
```

### Notas
* Airflow está configurado para correr en localhost:8081.
* PostgreSQL está configurado para usar la base de datos airflow con el usuario y la contraseña airflow.
