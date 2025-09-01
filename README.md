# 💰 Projeto 02 — Análise Exploratória de Criptomoedas (Bitcoin & Ethereum)

## 📌 Descrição
Este projeto tem como objetivo analisar o desempenho histórico do **Bitcoin (BTC)** e do **Ethereum (ETH)**, avaliando:
- Evolução dos preços ao longo do tempo
- Retornos diários, mensais e anuais
- Volatilidade
- Comparação direta entre BTC e ETH

Foram aplicadas técnicas de **manipulação de dados com Pandas** e **visualização com Matplotlib/Seaborn**, resultando em insights sobre valorização, riscos e padrões de comportamento das duas principais criptomoedas do mercado.

---

## 📂 Estrutura do Projeto
- **`PROJETO_02_crypto.py`** → script principal com todo o fluxo de análise.  
- **`/files/`** → dados brutos e processados (CSVs exportados).  
- **`/img/`** → gráficos gerados durante a execução.  
- **`analise_cripto.txt`** → resumo textual dos principais resultados.  

---

## ⚙️ Tecnologias Utilizadas
- Python 3.x  
- Pandas  
- Matplotlib

---

## 📑 Etapas da Análise
### 1. Tratamento inicial
- Importação dos datasets de BTC e ETH  
- Conversão de datas  
- Criação de métricas derivadas (retorno diário, acumulado e volatilidade)  

### 2. Análises principais
- **Série temporal dos preços (BTC vs ETH)**  
- **Distribuição dos retornos (histograma)**  
- **Volatilidade anual (desvio padrão dos retornos)**  
- **Boxplot comparando retornos mensais BTC vs ETH**  

### 3. Exportações
- CSVs com métricas (ex: `BTC_preco_medio.csv`, `BTC_retorno_ano.csv`)  
- Arquivo `.txt` com resumo da análise (`analise_cripto.txt`)  
- Gráficos em `.png` salvos em `/img/`  

---

## 📊 Resultados Principais
- O **Bitcoin valorizou +23.585%** entre 2014 e 2024  
- O **Ethereum valorizou +308.489%** no mesmo período  
- O **ETH foi mais volátil** do que o BTC, mas também apresentou retornos mais agressivos  
- Ambos seguem apresentando forte oscilação anual, característica típica de ativos de alto risco  

---

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo

2. Instale as dependências:
   ```bash
   pip install pandas
   pip install matplotlib

3. Execute o script principal:
   ```bash
   python PROJETO_02_crypto.py


## 📌 Autor
Projeto desenvolvido por **Matheus Alexandre** 💻  
📎 [LinkedIn](https://www.linkedin.com/in/matheus-alexandre-788848294/) | [GitHub](https://github.com/matheusangelucci)


