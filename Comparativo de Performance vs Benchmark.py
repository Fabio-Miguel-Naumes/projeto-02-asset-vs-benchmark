import yfinance as yf
import pandas as pd
import plotly.express as px

# 1) Baixa os preços ajustados
data = yf.download('^N225', period='20y', interval='1d', end='2025-07-01', rounding=True, auto_adjust=False)
data_ativo = yf.download('MUFG', period='20y', interval='1d', end='2025-07-01', rounding=True, auto_adjust=False)

data = pd.DataFrame(data)

data_ativo = pd.DataFrame(data_ativo)

retorno = data['Close'] / data['Close'].shift(1) - 1

retorno_ativo = data_ativo['Close'] / data_ativo['Close'].shift(1) - 1

data['retorno_acumulado'] = (retorno + 1).cumprod() - 1

data_ativo['retorno_acumulado'] = (retorno_ativo + 1).cumprod() - 1

data = data.dropna()

fig = px.line(
    data,
    x=data.index,
    y=data['retorno_acumulado'],
    title = 'Comparação ativo e benchmark (Nikkei 225 e Mitsubishi UFJ Financial Group)',
)

fig.add_scatter(
    x=data_ativo.index,
    y=data_ativo['retorno_acumulado'],
    name = 'Mitsubishi UFJ Financial Group'
)

fig.update_layout(legend_title_text='Ativos')
fig.update_yaxes(tickformat='.2%')
fig.show()
