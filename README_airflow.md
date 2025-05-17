# 📡 Orquestração de Pipeline com Apache Airflow

Esta etapa descreve como o projeto **MovieStream Analytics** utiliza o Apache Airflow para orquestrar a execução do pipeline de dados com DBT, garantindo agendamentos automáticos, modularidade e controle total do fluxo.

## ✅ Objetivo

Orquestrar a execução dos modelos do DBT (staging, marts, testes) de forma automatizada e escalável via DAGs no Airflow.

## 🧱 Estrutura

- DAG `dbt_pipeline_dag` e `dbt_pipeline_dag_modular` com as tarefas:
  - `run_dbt_staging`
  - `run_dbt_marts`
  - `run_dbt_tests`
- Agendamento diário às 8h UTC e também @daily
- Comandos executados diretamente no container Docker via `BashOperator`

## 📁 Local dos arquivos

- DAG definida em: `airflow/dags/dbt_pipeline_dag.py` `airflow/dags/dbt_pipeline_dag_modular.py`
- Projeto DBT disponível em: `airflow/dags/movie_stream_dbt/`

## 🐳 Docker e Airflow

O ambiente foi configurado com `docker-compose`, contendo os serviços:
- `postgres`: banco de metadados
- `airflow-webserver`: interface web
- `airflow-scheduler`: orquestrador
- `airflow-init`: inicializador do Airflow

## 🧪 Testes e Logs

A interface permite execução manual, agendada e visualização de logs por tarefa.
![Iniciar Airflow](<imagens/airflow instal.png>)
---

Desenvolvido por Elen de Bona ✨

Próximo passo >>[Etapa 2 - DBT](README_dbt.md)