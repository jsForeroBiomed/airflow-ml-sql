FROM apache/airflow:2.6.1     

USER airflow                 

RUN pip install pandas scikit-learn joblib faker  

USER airflow                   

