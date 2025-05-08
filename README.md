# QualityFlight


**QualityFlight** é um projeto para análise e validação de dados de voos, utilizando técnicas de geração de dados, validação, aprendizado de máquina e análise com modelos de linguagem (LLMs). O objetivo é identificar problemas operacionais e gerar insights para melhorias no setor de aviação.


## Funcionalidades

1. **Geração de Dados**:
   - Gera dados sintéticos de voos com a biblioteca `Faker`.
   - Introduz problemas como atrasos, cancelamentos e desvios.

2. **Validação de Dados**:
   - Valida a estrutura e os valores dos dados.
   - Gera relatórios de erros e alertas.

3. **Detecção de Anomalias**:
   - Utiliza `IsolationForest` e `RandomForestClassifier` para identificar voos problemáticos.
   - Gera relatórios de importância de features.

4. **Análise com LLMs**:
   - Integração com a API da OpenAI para gerar relatórios detalhados em linguagem natural.



## Requisitos

- Python 3.9+
- Dependências listadas em `requirements.txt`



## Uso

### 1. Geração de Dados
Execute o notebook `01_data_generation.ipynb` para gerar dados sintéticos e validar a estrutura inicial.

### 2. Validação de Dados
Execute o notebook `02_data_validation.ipynb` para validar os dados gerados e gerar relatórios.

### 3. Detecção de Anomalias
Execute o notebook `03_ml_anomaly_detection.ipynb` para treinar modelos de aprendizado de máquina e identificar anomalias.

### 4. Análise com LLMs
Execute o notebook `04_llm_analysis.ipynb` para gerar relatórios detalhados com insights operacionais.



## Relatórios Gerados

- **Distribuição de Status dos Voos**: `data/reports/flight_status_distribution.png`
- **Resumo da Validação**: `data/reports/validation_results.json`
- **Importância das Features**: `data/reports/feature_importance.png`
- **Relatório de Análise**: `data/reports/flight_analysis_report.md`


## Contato

Para dúvidas ou sugestões, entre em contato pelo [LinkedIn](https://www.linkedin.com/in/fcrispcoach/).
