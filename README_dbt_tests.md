# 🧪 Testes de Qualidade de Dados (DBT)

Este módulo documenta os testes aplicados sobre os modelos do DBT para garantir integridade e consistência, além das boas práticas de qualidade de dados no DBT, usando testes integrados 

## Tipos de testes aplicados
No DBT, é possível aplicar testes diretamente no arquivo `schema.yml` para garantir a integridade dos seus modelos.
- `not_null`: garante presença de dados
- `unique`: garante unicidade em campos chave
- `accepted_values`: (pode ser usado para validar valores específicos)

![mart_customer_lifetime_value](<imagens/test_dbt.png>)

## Modelos testados
- `mart_customer_lifetime_value`
- `mart_film_popularity`
- `mart_store_performance`

## Como rodar
```bash
dbt test --select nome_do_modelo
```


Desenvolvido por Elen de Bona ✨

Próximo passo >>[Etapa 2.2 - DBT build](<README_dbt build.md>)