# 🚧 Automatizar com DBT - `dbt build`

## 🛠️ O que dbt build faz?

````dbt build
````

Esse comando executa em sequência automática:

1. dbt run → constrói os modelos

2. dbt test → roda os testes definidos no schema.yml

3. (opcional) dbt seed, dbt snapshot, dbt docs generate (se configurado)


Ele irá:

Executar seus modelos de `marts`

Rodar os testes de integridade.


Desenvolvido por Elen de Bona ✨


Próximo passo >>[Etapa 3 - FOCO DESTE PROJETO](README_analise_explor.md)