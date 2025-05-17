# 🚧 Modelagem com DBT - Projeto 

Este módulo é responsável pela transformação e modelagem dos dados brutos em tabelas analíticas (marts), utilizando o framework DBT no DBeaver com PostgreSQL. 

## Estrutura

![Estrutura da modelagem](<imagens/estrutura_dbt.png>)
- `models/staging/`: limpeza e padronização
- `models/marts/`: tabelas derivadas de negócio


## Comandos úteis
- `dbt run`: roda os modelos
- `dbt test`: executa testes de integridade
- `dbt build`: compila, roda e testa automaticamente

## Modelos criados:

![staging e marts no DBT](<imagens/dbt_stag e mart.png>)

- `stg_customer`, `stg_payment`, `stg_film`, `stg_rental`
- `mart_customer_lifetime_value`
- `mart_film_popularity`
- `mart_store_performance`


## 🧹 Staging models

São camadas intermediárias, criadas para:

 - Padronizar nomes de colunas

 - Fazer joins ou filtros básicos

 - Deixar o código modular, limpo e reutilizável


Desenvolvido por Elen de Bona ✨


Próximo passo >>[Etapa 2.1 - DBT testes](README_dbt_tests.md)