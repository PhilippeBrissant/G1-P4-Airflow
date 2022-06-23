from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA


def loadDataset():
    print('Carregando o iris dataset')
    iris = load_iris()
    data = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                        columns=iris['feature_names'] + ['target'])


def minMaxScaler():
    print('Carregando o iris dataset')
    iris = load_iris()
    data = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                        columns=iris['feature_names'] + ['target'])
    X = data.drop(['target'], axis=1)
    y = data.target

    print('Aplicando MinMaxScaler')
    X = MinMaxScaler().fit_transform(X)


def pca():
    print('Carregando o iris dataset')
    iris = load_iris()
    data = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                        columns=iris['feature_names'] + ['target'])
    X = data.drop(['target'], axis=1)
    y = data.target

    print('Aplicando PCA')
    X = PCA().fit_transform(X)


def knn():
    print('Carregando o iris dataset')
    iris = load_iris()
    data = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                        columns=iris['feature_names'] + ['target'])
    X = data.drop(['target'], axis=1)
    y = data.target

    print('Aplicando MinMaxScaler')
    X = MinMaxScaler().fit_transform(X)
    print('Aplicando MinMaxScaler')
    X = PCA().fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=20, stratify=y)
    knn1 = KNeighborsClassifier(7)
    knn1.fit(X_train, y_train)
    print("Train score", knn1.score(X_train, y_train), "%")
    print("Test score", knn1.score(X_test, y_test), "%")


with DAG(dag_id="appraisal",
         start_date=datetime(2022, 6, 23),
         schedule_interval="@hourly",
         catchup=False) as dag:

    task = PythonOperator(
        task_id="load",
        python_callable=loadDataset)

    task1 = PythonOperator(
        task_id="minmaxscaler",
        python_callable=minMaxScaler)

    task2 = PythonOperator(
        task_id="pca",
        python_callable=pca)

    task3 = PythonOperator(
        task_id="knn",
        python_callable=knn)

task >> task1 >> task2 >> task3
