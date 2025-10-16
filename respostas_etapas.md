# Union IT — Desafio Estágio em Dados e IA

## Etapa 1 — Análise de Dados e Diagnóstico

### Tarefa 1.1 — Diagnóstico e Abordagem de Machine Learning
- Problema: baixa conversão de visitantes em clientes pagantes.  
- Objetivo ML: estimar a probabilidade de conversão por lead (score 0–1).  
- Abordagem: aprendizado supervisionado — classificação binária.  
- Uso prático: priorização de leads e personalização de campanhas.

Métricas principais: AUC-ROC, Precision@k, recall, F1; calibrar probabilidade para uso em regras de negócio.

### Tarefa 1.2 — Análise e Preparação dos Dados
Features promissoras:
- tempo_navegacao_site (engajamento)
- paginas_visitadas (interesse)
- setor_empresa (segmentação)
- cidade_lead (diferenças regionais)
- id_visitante — identificador (remover do treino)

Prevenção de overfitting:
- regularização, poda de features, validação cruzada, early stopping.  
Mitigação de underfitting:
- engenh. de features, modelos mais expressivos, otimização de hiperparâmetros.

Processo de preparação:
1. Limpeza e deduplicação.  
2. Tratamento de missing e outliers.  
3. Encoding de categóricas (target/one‑hot/embedding).  
4. Split temporal (se aplicável) + validação cruzada.  
5. Balanceamento se classes muito desbalanceadas.

---

## Etapa 3 — Visão Estratégica e Comunicação

### Tarefa 3.1 — Proposta de Solução Completa
Objetivo: aumentar conversão via priorização e mensagens personalizadas.

Arquitetura sugerida:
- Ingestão: eventos do site → Data Lake (S3/Blob).  
- Feature Store: cálculo de agregados e janelas temporais.  
- Treinamento: pipelines (Azure ML / SageMaker / Vertex AI).  
- Inferência: microsserviço (FastAPI) expõe /predict.  
- IA generativa: motor separado para geração de e-mails por setor.  
- Integração: CRM/Marketing (HubSpot, Salesforce).  
- Monitoramento: métricas de desempenho, drift detection, logs e auditoria.

Ferramentas (sugestões):
- Azure: Blob, Azure ML, Functions, Power BI.  
- AWS: S3, SageMaker, Lambda, QuickSight.  
- GCP: Cloud Storage, Vertex AI, Cloud Run, BigQuery.

Riscos éticos:
- vieses regionais ou setoriais — mitigar com remoção/controle de atributos sensíveis, fairness tests e revisão humana.

### Tarefa 3.2 — Defesa do Projeto (roteiro ~10 min)
1. Contexto e objetivo.  
2. Dados, features e qualidade.  
3. Modelo, métricas e performance.  
4. Arquitetura de produção e integração.  
5. Riscos, ética e mitigação.  
6. Próximos passos: A/B tests, retraining, dashboards.

---

## Implementação rápida — checklist mínimo
- [ ] Coletar e amostrar dados rotulados.  
- [ ] Pipeline de pré‑processamento e validação temporal.  
- [ ] Prototipar modelo (LightGBM/Logistic/NN) e validar métricas.  
- [ ] Deploy do endpoint /predict (container + CI/CD).  
- [ ] Integração com CRM e testes A/B.  
- [ ] Monitoramento de drift e recalibração periódica.

Exemplo de contrato mínimo para /predict (JSON):
- Request: { "id_visitante": "str", "tempo_navegacao_site": float, "paginas_visitadas": int, "setor_empresa": "str", "cidade_lead": "str" }  
- Response: { "conversion_prob": float, "model_version": "v1" }

---

## Plano de avaliação e rollout
- Piloto com leads segmentados → A/B test (controle vs modelo).  
- Métricas: aumento de conversão, Lift@k, custo por aquisição.  
- Critério de sucesso: melhoria estatisticamente significativa nas taxas de conversão e ROI positivo.
