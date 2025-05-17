# 📊 Análise exploratória e Queries de negócio - KPIs | Visualização e Queries Analíticas

A partir daqui, será onde o esforço deste projeto será aplicado com maior propriedade por mim. O projeto **MovieStream Analytics**, foca em análise da base de dados, definição de KPIs prioritários e preparação para construção do DataViz no Qlik Sense ou Power BI.

Este módulo completa 3 etapas principais, 2 voltadas a etapa de Análise de Dados e toda a suas subdivisões e a última etapa, voltada ao BI e Storytelling, criando ao final o dashboard baseado em tudo que foi preparado anteriorente.

| Análise de Dados        | Análise exploratória e queries de negócio |
| BI       | Criação de dashboards e storytelling      |


## Objetivo
- Entregar indicadores visuais e interpretáveis KPIs
- Utilizar dados das tabelas `mart_...`
- Limpeza por dbt tests
- Automação por dbt build
- Queries Analíticas .sql
- Insights acionáveis ao negócio

## Ferramenta escolhida
- Qlik Sense Cloud - foi testado, porém, declinou-se desta ferramenta porque precisava de um e-mail corporativo e/ou convite.
- Power BI

## Status
Etapa em preparação, após validação dos marts com sucesso.


## 🧩 Visão Geral das Tabelas (Principais para o Projeto)
Entendimento das principais Tabelas mais relevantes dentro do banco de dados `dbinterview.sql`:

| Tabela                       | Descrição                                                   |
| ---------------------------- | ----------------------------------------------------------- |
| `customer`                   | Informações dos clientes (nome, endereço, data de cadastro) |
| `rental`                     | Registro de locações de filmes feitas pelos clientes        |
| `payment`                    | Pagamentos relacionados às locações                         |
| `film`                       | Detalhes dos filmes (título, duração, idioma)               |
| `inventory`                  | Cópias físicas (ou unidades disponíveis) dos filmes         |
| `store`                      | Informações das lojas                                       |
| `category`                   | Categorias dos filmes (ex: ação, comédia)                   |
| `film_category`              | Tabela ponte entre `film` e `category`                      |
| `address`, `city`, `country` | Informações geográficas dos clientes e lojas                |



## 🛠️ Exploração e Relações do Dados
Agora pode:

1. Explorar relacionamentos entre tabelas<br>
>Exemplo: de payment → rental → customer → city

2. Escrever queries para as perguntas de negócio

>Quais são os 5 clientes que mais geraram receita no último ano?

>Qual a média de dias entre o aluguel e a devolução por categoria?

>Quais as 3 cidades com maior volume de locações?

>Qual o ticket médio por loja?

>Gere uma visão agregada de receita mensal para os últimos 24 meses com dados.


3. Selecionar os KPIs principais para o dashboard<br>
>Receita mensal, clientes ativos, locações por categoria, etc.

______________________________
> [!NOTE]
> Vamos explorar as relações entre as tabelas do banco dbinterview. Com isso, entende-se como montar as joins nas queries, e também como estruturar os indicadores e modelo analítico.

___
## - Modelagem de Dados 

## 🔗 Relacionamento entre as principais tabelas
Diagrama textual:

🎬 1. customer (cliente)
🔗 se relaciona com:

- address → city → country (localização do cliente)

- rental (histórico de locações)

- payment (pagamentos realizados)



📽️ 2. rental (locações)
🔗 se relaciona com:

- customer (quem alugou)

- inventory (qual cópia do filme foi alugada)

- staff (quem atendeu)

- payment (pagamento da locação)


🎞️ 3. inventory (estoque de filmes)
🔗 se relaciona com:

- film (qual filme está em estoque)

- store (em qual loja está disponível)

- rental (quem alugou o quê)


💰 4. payment (pagamentos)
🔗 se relaciona com:

- rental (qual locação foi paga)

- customer (quem pagou)

- staff (quem processou o pagamento)


🎬 5. film (filmes)
🔗 se relaciona com:

- inventory (em quais lojas está)

- film_category → category (gênero)

- language (idioma do filme)

- film_actor → actor (atores do filme)


🏬 6. store (lojas)
🔗 se relaciona com:

- staff (quem trabalha ali)

- inventory (quais filmes tem)

- customer (clientes da loja)


## 🗺️ Caminhos comuns para análises

| Análise                             | Caminho de Joins                                               |
| ----------------------------------- | -------------------------------------------------------------- |
| Receita por cliente                 | `payment` → `customer`                                         |
| Receita por loja                    | `payment` → `staff` → `store`                                  |
| Filmes mais alugados                | `rental` → `inventory` → `film`                                |
| Filmes mais populares por categoria | `rental` → `inventory` → `film` → `film_category` → `category` |
| Locações por cidade                 | `rental` → `customer` → `address` → `city`                     |
| Tempo médio de locação              | `rental.rental_date` até `rental.return_date`                  |



## UML - Whiteboard do Diagrama ER simplificado 

![Diagrama ER](</imagens/diagrama ER.png>)


### 🔗 Diagrama ER Simplificado – Banco `dbinterview`


```text
[customer]───┬────────────┐
            │            │
         (1:N)         (1:N)
            │            │
        [rental]────(1:N)──[payment]
            │              │
         (N:1)           (N:1)
            │              │
      [inventory]──────┐   │
         │      │        │   │
      (N:1)  (N:1)     (N:1)
         │      │        │
     [film]  [store] [staff]
         │
      (N:M)
         │
[film_category]──(N:1)──[category]
         │
      (N:M)
         │
   [film_actor]──(N:1)──[actor]

[customer]──(N:1)──[address]──(N:1)──[city]──(N:1)──[country]
[film]──(N:1)──[language]
```

**Legendas:**
- `(1:N)` = um para muitos
- `(N:M)` = muitos para muitos
- As tabelas centrais do negócio são: `customer`, `rental`, `payment`, `film`, `store`
- As tabelas de apoio são: `address`, `category`, `language`, `actor`, etc.

---

### 🌟 Star Schema Proposto – Foco em Fato de Pagamento

![Star Schema](<imagens/star schema.png>)

```text
             [dim_customer]
                  ▲
                  │
             [dim_date]         [dim_film]
                  ▲               ▲
                  │               │
          [fact_payment]◄────[dim_store]
                  ▲
                  │
            [dim_staff]
```

**Fato central:**
- `fact_payment` – informações de pagamento realizadas por clientes

**Dimensões:**
- `dim_customer` – dados do cliente (nome, cidade, país)
- `dim_date` – datas relacionadas ao pagamento (data, mês, ano)
- `dim_film` – filme alugado via ligação com rental → inventory → film
- `dim_store` – loja responsável
- `dim_staff` – atendente responsável

Este Star Schema é ideal para construir KPIs como:
- Receita por cliente
- Receita por filme
- Receita por loja
- Receita por atendente
- Receita mensal/por ano

## 📊 Definição de KPIs principais
Indicadores:
| **Nome do KPI**                   | **Descrição**                                   |
| --------------------------------- | ----------------------------------------------- |
| Receita Total Mensal              | Soma dos pagamentos por mês                     |
| Top 5 Clientes por Receita        | Clientes que mais pagaram no último ano         |
| Locações por Categoria            | Número de aluguéis por categoria de filme       |
| Tempo Médio de Devolução          | Média de dias entre aluguel e devolução         |
| Cidades com Mais Locações         | Top 3 cidades com maior número de aluguéis      |
| Número de Clientes Ativos Mensais | Contagem de clientes únicos com locações no mês |


## SQLs analíticos
As onsultas em SQL padrão PostgreSQL para responder às perguntas do projeto MovieStream Analytics.

✅ 1. Top 5 clientes que mais geraram receita no último ano
![query top 5](<imagens/query 5 top.png>)
![resultado top 5](<imagens/query 5 top.png>)

✅ 2. Média de dias entre aluguel e devolução por categoria de filme
![query days avg by cat](<imagens/query avg por categ.png>)
![resultado days avg by cat](<imagens/resultado avg por categ.png>)

✅ 3. Top 3 cidades com maior volume de locações
![query top 3 cities](<imagens/query top 3 cidades aluguel.png>)
![resultado top 3 cities](<imagens/resultado top 3 cidades aluguel.png>)

✅ 4. Ticket médio por loja
![query tkm by store](<imagens/query tkm por loja.png>)
![resultado tkm by store](<imagens/resultado tkm por loja.png>)

✅ 5. Receita mensal nos últimos 24 meses
![query budget 24 months](<imagens/query 24 meses.png>)
![resultado budget 24 months](<imagens/resultado 24 meses.png>)


Desenvolvido por Elen de Bona ✨


Próximo passo >>[ETAPA 4 - FOCO DESTE PROJETO 1](<README_dash BI.md>)