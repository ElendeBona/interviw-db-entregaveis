# 🧹 Case Técnico Vox Tecnologia: Projeto Pipeline ETL de Dados - MovieStream Analytics - Elen de Bona

## 🎮 Sobre o Projeto

A **MovieStream Analytics** é uma empresa fictícia especializada em soluções analíticas para o mercado de locação e streaming de filmes. Este projeto tem como objetivo construir uma **pipeline robusta e escalável de dados**, desde a ingestão até a visualização, para suportar decisões estratégicas baseadas em dados reais de uso da plataforma. \
A orquestradora deste projeto fictício criado pela empresa Vox Tecnologia, aqui chamada apenas de Elen, estará trazendo sua linha de raciocínio para este projeto, seguindo sua expertise como **Analista de Dados e Automações**, e concentrando seus esforços para a tradução de dados em valor para o negócio, ou seja, no processo de ETL, o foco será no LOAD. Ao longo deste projeto, será evidenciado o olhar estratégico e investigativo que um analista de dados e BI precisa adotar em cada etapa de uma pipeline analítica, desde a exploração de dados até a entrega visual e interpretativa dos indicadores.
Isso não quer dizer que as demais etapas nãp foram feitas, pelo contrário, foram de forma robusca e absorvendo o conhecimento e bagagem como profissional proativa e dinâmica ao mercado, trazido ao longo da minha tragetória. 
Ainda uma surpresa, a cereja do bolo, para para validar ainda mais meu conhecimento, compromisso, maturidade perante um desafio novo, criei **um Agente de IA atrelado ao projeto para validar ainda mais meu conhecimento, compromisso, maturidade perante um desafio novo**. 

## 🚀 Objetivos

- Realizar ingestão de dados de um dump PostgreSQL com estratégia de CDC
- Modelar e transformar os dados com boas práticas de engenharia
- Criar tabelas derivadas (data marts) para consumo analítico
- Executar queries analíticas respondendo perguntas de negócio
- Expor insights via dashboards interativos

## 🛠️ Tecnologias Utilizadas

- PostgreSQL - DBeaver
- Airflow (orquestração de pipelines)
- DBT (modelagem de dados)
- Qlik Sense/Power BI (visualização)
- Git/GitHub (versionamento)

## 🧱 Orquestração e Estrutura de Diretórios

entregaveis/<br>
├── airflow/ # DAGs do Airflow<br>
├── dbt/<br>
│ ├── models/ # Modelos DBT (staging, marts)<br>
│ └── dbt_project.yml # Configuração do projeto DBT<br>
├── análise de dados exploratória / # banco relacional (tabelas)<br>
    ├── modelagem de dados - UML (conceitual, lógico e físico)<br>
│   └── star schema<br>
├── sql_queries/ # SQLs analíticos do desafio<br>
├── dashboard/ # Capturas ou links dos dashboards<br>
├── README.md <br>
└── demais READMEs.md<br>


## 📌 Entregáveis
[README main](README.md)<br>
[Etapa 1 - Airflow](README_airflow.md)<br>
[Etapa 2 - DBT](README_dbt.md)<br>
[Etapa 2.1 - DBT testes](README_dbt_tests.md)<br>
[Etapa 2.2 - DBT build](<README_dbt build.md>)<br>
[Etapa 3 - FOCO DESTE PROJETO](README_analise_explor.md)<br>
[ETAPA 4 - FOCO DESTE PROJETO 1](<README_dash BI.md>)<br>
[PLUS do Projeto - Agente de IA](inteligencia/README_agente_IA.md)<br>


## 📌 Entregáveis Técnicos
>[Dashboard](<imagens/power bi dash movie stream elen case.png>)

>[PDF Dashboard](<pdf/Relatório Técnico de Análise de Dados MovieStream Analytics (1).pdf>)

>[Case Técnico](<pdf/case elen vox tech movie stream.pdf>)

>>[PLUS do Projeto - Criação de Agente de IA especialista em Streaming de Filmes](inteligencia)


## 🧠 Funções Envolvidas no Projeto

| Função                   | Responsabilidades                         |
| ------------------------ | ----------------------------------------- |
| Engenheiro de Dados      | Ingestão, CDC, Airflow                    |
| Analytics Engineer (DBT) | Modelagem e transformação de dados        |
| Analista de Dados        | Análise exploratória e queries de negócio |
| Especialista em BI       | Criação de dashboards e storytelling      |

## ❓ Alinhamento Inicial com o Cliente

Antes de iniciar qualquer desenvolvimento, é fundamental entender as reais intenções do projeto. Este projeto foi estruturado para abranger todas as frentes de um pipeline  de dados, normalmente executado por um time multidisciplinar de engenharia, análise e visualização. Neste projeto, eu Elen de Bona, concentrei as entregas assumindo a função estratégica de Analista de Dados e BI, com foco em boas práticas e escalabilidade, portanto, é importante ter um alinhamento inicial com o cliente e que segue nos questionamentos a seguir.

O papel do Analista de Dados e BI neste projeto é fundamental, pois exige não apenas habilidades técnicas, mas também visão de negócio, pensamento crítico, capacidade de comunicar descobertas e de transformar dados brutos em insights acionáveis e compreensíveis para o cliente final. Essa atuação se destaca por alinhar objetivos estratégicos às possibilidades reais do uso dos dados.

### Sobre os Objetivos de Negócio

1. Qual é o principal objetivo deste projeto de dados?
2. Quais áreas ou equipes vão consumir esses dados?
3. Quais decisões a empresa deseja tomar com base nas análises?
4. Há metas ou indicadores que precisam ser monitorados?

### Sobre os Dados

5. Existe alguma preocupação com qualidade, atraso ou confiabilidade nos dados?
6. Quais tabelas ou eventos representam comportamento real do cliente?
7. Há alguma sazonalidade ou comportamento esperado que eu deva considerar?

### Sobre Entregas e Visualizações 

8. Qual o formato ideal de entrega para vocês?
9. Quais são os 2 ou 3 indicadores mais importantes para vocês?
10. O público que vai consumir os dashboards tem familiaridade com ferramentas interativas?

## 📌 Link da Base de Dados

[https://hub.docker.com/r/voxtecnologiahub/dbinterview](https://hub.docker.com/r/voxtecnologiahub/dbinterview)

## 📄 Licença

Este projeto é fictício e tem fins educacionais e demonstrativos e não pode ser usado para qualquer outro fim.
Criado por Elen de Bona Johann ✨

## 📞 **Suporte**

Caso tenha dúvidas ou precise de suporte, entre em contato comigo:
- **E-mail**: edsoolbj@gmail.com


## 🌟 **Contribuição**

Contribuições são bem-vindas! Se você deseja melhorar o Dash BI ou adicionar novas funcionalidades, siga os passos abaixo:

1. Faça um fork deste repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova feature'`).
4. Envie um pull request para revisão.


Próximo passo >>[Etapa 1 - Airflow](README_airflow.md)

"""
_____
