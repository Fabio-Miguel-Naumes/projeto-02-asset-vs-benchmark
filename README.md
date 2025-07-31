## 📘 2. Projeto 2 – Performance vs Benchmark


# 📊 Projeto 2 – Performance vs Benchmark

[![Plotly](https://img.shields.io/badge/Plotly-Interactive-orange)]() [![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## 🎯 Objetivo
Comparar o retorno acumulado de um ativo selecionado contra o S&P500, quantificando desempenho, volatilidade e correlação.

## 🛠️ Ferramentas & Tecnologias
- **Python 3.9+**  
- **yfinance**: dados de ativos e benchmark (`^GSPC`)  
- **Pandas**: cálculos de retorno e estatísticas  
- **Plotly Express**: gráficos interativos  
- **NumPy**: operações numéricas

## 🚀 Funcionalidades
1. Cálculo de retornos diários e retornos acumulados  
2. Gráfico interativo de linha comparando ativo x benchmark  
3. Métricas: volatilidade anual, Sharpe Ratio e Beta

## 📈 Demonstração
![return_comparison](images/Comparação-ativo-e-benchmark-(Nikkei-225-e-Mitsubishi-UFJ-Financial-Group).png)

## 📝 Como Rodar
bash
git clone https://github.com/Fabio-Miguel-Naumes/projeto-02-asset-vs-benchmark.git
cd projeto-02-asset-vs-benchmark
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python src/compare.py
