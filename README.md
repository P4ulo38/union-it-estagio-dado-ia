1. README.md (documentação principal)
# Union IT — Desafio Estágio em Dados e IA

## 📌 Objetivo
Este projeto foi desenvolvido como parte do processo seletivo para estágio em Dados e IA na **Union IT**.  
O desafio consiste em:
1. Traduzir um problema de negócio (baixa conversão de leads) em uma estratégia de Machine Learning.  
2. Desenvolver protótipos em Python para prever a probabilidade de conversão e gerar e-mails personalizados com IA generativa.  
3. Propor uma visão estratégica de como a solução poderia ser implementada em produção.

---

## 📂 Estrutura do Repositório


union-it-estagio-dados-ia/ 
├── README.md 
├── requirements.txt 
├── respostas_etapas.md 
├── leads.csv 
├── analise_segmento.py 
├── etapa2_modelo/ 
 │   
 ├── modelo_preditivo_prototipo.py 
 │   
 └── gerador_emails_prototipo.py

---

## ⚙️ Como configurar
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows PowerShell
pip install -r requirements.txt



▶️ Como executar
Modelo preditivo
python etapa2_modelo/modelo_preditivo_prototipo.py


IA generativa
python etapa2_modelo/gerador_emails_prototipo.py --setor "Tecnologia"
python etapa2_modelo/gerador_emails_prototipo.py --setor "Saúde"


Análise exploratória
python analise_segmento.py



📝 Respostas escritas
As respostas das Etapas 1 e 3 estão em respostas_etapas.md.

🚀 Entrega
- Repositório privado no GitHub
- Adicionado rh@unionit.com.br como colaborador
- Link enviado no sistema de seleção

---

## 2. `respostas_etapas.md` (respostas escritas)

```markdown
# Respostas — Desafio Union IT

## Etapa 1 — Análise de Dados e Diagnóstico

### Tarefa 1.1
Problema: baixa conversão de leads.  
Tradução para ML: classificação binária (converter ou não).  
Abordagem: aprendizado supervisionado, modelo de classificação (ex.: regressão logística, árvore de decisão).  
Saída: probabilidade de conversão.

### Tarefa 1.2
Features promissoras:
- tempo_navegacao_site
- paginas_visitadas
- setor_empresa
- cidade_lead  
(id_visitante não deve ser usado)

Overfitting → reduzir complexidade, regularizar, coletar mais dados.  
Underfitting → aumentar capacidade do modelo, criar novas features, ajustar hiperparâmetros.

---

## Etapa 3 — Visão Estratégica

### Tarefa 3.1
**Arquitetura sugerida:**  
- Ingestão de dados → Data Lake  
- Treinamento → Azure ML / SageMaker  
- Inferência → microsserviço (FastAPI) em container  
- Integração → CRM/Marketing  
- Monitoramento → métricas de conversão, drift, fairness

**Ferramentas Cloud:** Azure, AWS ou GCP (armazenamento, ML, deploy).  
**Desafio ético:** risco de viés (segmentos ou regiões). Mitigação: fairness checks, auditoria, revisão humana.

### Tarefa 3.2
Roteiro de defesa (10 min):  
1. Contexto e objetivo  
2. Dados e features  
3. Modelo e métricas  
4. Arquitetura de produção  
5. Riscos e ética  
6. Próximos passos



3. requirements.txt (dependências)
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.5.2
matplotlib==3.9.2
seaborn==0.13.2
transformers==4.44.2
torch==2.2.2

### Uso de IA no desenvolvimento

Alguns trechos de código e ideias de prototipagem foram apoiados por ferramentas de IA generativa, sempre com revisão e adaptação manual.  
O objetivo foi acelerar a prototipagem, mas todas as decisões de modelagem, métricas, features e arquitetura foram analisadas e validadas por mim.


