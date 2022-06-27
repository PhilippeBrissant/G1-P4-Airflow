# G1-P4-Airflow
Pipeline Airflow para execução dos algoritmos de inputação de dados ausentes do framework Appraisal.

# Instalação
- [Instale o Docker](https://docs.docker.com/engine/install/)
- [Instale o Docker Compose](https://docs.docker.com/compose/install/)
- Baixe o projeto com o comando 
        
        git clone https://github.com/PhilippeBrissant/G1-P4-Airflow.git
- Compile e rode o container docker com os comandos abaixo:

        docker-compose build airflow-init
        docker-compose up airflow-init


# E agora?

Já é possível utilizar o airflow localmente. Acesse localhost:8080 para acessar a aplicação. Logue com **login** ``airflow`` e **senha** ``airflow``. Para mais informações, acesso a [documentação oficial](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html).

Obs: caso queira utilizar alguma lib python específica, é necessário adicioná-la na variável de ambiente _PIP_ADDITIONAL_REQUIREMENTS (linha 61) no arquivo [docker-compose.yaml](./docker-compose.yaml). Basta digitar o nome das libs desejadas seguidas de um espaço. 

    _PIP_ADDITIONAL_REQUIREMENTS: ${_PIP_ADDITIONAL_REQUIREMENTS:- scikit-learn pandas numpy}