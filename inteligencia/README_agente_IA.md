# Agente de IA para Análise de Dados MovieStream

## 🤖 O que é o agente de IA?

O agente de IA deste projeto foi desenvolvido para atuar como um especialista em análise de dados do mercado de streaming de filmes, utilizando modelos de linguagem natural e integração direta com o banco de dados PostgreSQL da solução MovieStream Analytics. Ele responde perguntas complexas, gera análises detalhadas e executa queries SQL automaticamente, facilitando a extração de insights e a tomada de decisão baseada em dados.

---
## ⚙️ Como funciona?

O agente foi implementado com as seguintes tecnologias:

- **Python**: Linguagem principal do agente.
- **Agno**: Framework para agentes inteligentes e integração com LLMs.
- **Groq (Llama-3.3-70b-versatile)**: Modelo de linguagem natural para geração de respostas e análises.
- **PostgresTools**: Ferramenta para conexão e execução de queries no banco de dados PostgreSQL.
- **dotenv**: Gerenciamento seguro de variáveis de ambiente.

O agente é inicializado com acesso ao banco de dados local, podendo consultar tabelas como `payment`, `customer`, `rental`, `category`, `store`, `inventory` e outras. Ele entende perguntas em linguagem natural e pode tanto responder com análises textuais quanto gerar queries SQL para buscar informações diretamente no banco.

---

## 📝 Exemplos de perguntas e respostas

### Pergunta enviada ao agente:
>>Faça uma análise super complexa sobre o mercado de filmes

### Resposta gerada pelo agente (exemplo real do terminal):

> O mercado de filmes, especialmente no contexto do streaming, passou por transformações profundas na última década. A digitalização do conteúdo e a popularização de plataformas como Netflix, Amazon Prime Video, Disney+ e outras, alteraram significativamente o comportamento do consumidor e a dinâmica competitiva do setor.
>
> **Tendências principais:**
>
> 1. **Fragmentação do mercado:** O aumento do número de plataformas levou à fragmentação do catálogo, exigindo que consumidores assinem múltiplos serviços para acessar todo o conteúdo desejado.
> 2. **Produção de conteúdo original:** Plataformas investem pesadamente em produções próprias para diferenciar seus catálogos e fidelizar assinantes.
> 3. **Personalização e recomendação:** O uso de IA e algoritmos de recomendação tornou-se essencial para engajar usuários e aumentar o tempo de permanência nas plataformas.
> 4. **Internacionalização:** Conteúdos locais e internacionais ganham espaço, com legendas e dublagens ampliando o alcance global.
> 5. **Desafios regulatórios:** Questões de direitos autorais, distribuição e tributação digital são cada vez mais relevantes.
>
> **Impactos nos dados:**
>
> - Crescimento exponencial no volume de dados de consumo, permitindo análises detalhadas de preferências, horários de pico, churn e engajamento.
> - Necessidade de infraestrutura robusta para armazenar, processar e analisar grandes volumes de dados em tempo real.
>
> **Conclusão:** O mercado de filmes em streaming é dinâmico, competitivo e orientado por dados. Empresas que investem em tecnologia, experiência do usuário e conteúdo relevante tendem a se destacar e capturar maior fatia de mercado.

---


## 💡 O que o agente pode fazer?

- Responder perguntas sobre o mercado de filmes e streaming com análises detalhadas.
- Gerar queries SQL para buscar informações específicas no banco de dados.
- Explicar tendências, métricas e resultados com base nos dados reais da plataforma.
- Auxiliar na tomada de decisão estratégica para negócios de streaming.

---

## 🚀 Como usar

1. Edite o arquivo `agent.py` para ajustar perguntas ou comandos.
2. Execute o agente pelo terminal: `python...agent.py`
3. Veja as respostas diretamente no terminal, podendo copiar análises ou queries para uso em relatórios, dashboards ou apresentações.

---

## 📞 Suporte

Dúvidas ou sugestões? Entre em contato pelo e-mail: edsoolbj@gmail.com

---

Desenvolvido por Elen de Bona ✨