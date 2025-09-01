import pandas as pd
import matplotlib.pyplot as plt

BTC_df = pd.read_csv('../TRAININGS/PROJETO_02_crypto/file/coin_Bitcoin.csv')
ETH_df = pd.read_csv('../TRAININGS/PROJETO_02_crypto/file/coin_Ethereum.csv')
analise_caminho = '../TRAININGS/PROJETO_02_crypto/file/analise_cripto.txt'

def metricas(dataframe, exportar=True):

    criptomoeda = dataframe.loc[0, 'Symbol']

    # Cálculo do Retorno diário
    retorno_dia = dataframe[['Symbol', 'Date', 'Open', 'Close']].copy()
    retorno_dia['Retorno dia'] = round(((retorno_dia['Close'] - retorno_dia['Open']) / retorno_dia['Open']) * 100, 2)
    if exportar:
        retorno_dia.to_csv(f'../TRAININGS/PROJETO_02_crypto/file/ready/{criptomoeda}_retorno_dia.csv', index=False)
    
    # Cálculo do Retorno mensal
    retorno_mes = retorno_dia[['Symbol', 'Date', 'Retorno dia']].copy()
    retorno_mes.rename(columns={'Retorno dia': 'Retorno mes'}, inplace=True)
    retorno_mes['Date'] = pd.to_datetime(retorno_mes['Date']).dt.strftime('%Y-%m')
    retorno_mes_agrupado = retorno_mes.groupby('Date')['Retorno mes'].sum().round(2)
    if exportar:
        retorno_mes_agrupado.to_csv(f'../TRAININGS/PROJETO_02_crypto/file/ready/{criptomoeda}_retorno_mes.csv')

    # Cálculo do Retorno anual
    retorno_ano = retorno_dia[['Symbol', 'Date', 'Retorno dia']].copy()
    retorno_ano.rename(columns={'Retorno dia': 'Retorno ano'}, inplace=True)
    retorno_ano['Date'] = pd.to_datetime(retorno_ano['Date']).dt.strftime('%Y')
    retorno_ano_agrupado = retorno_ano.groupby('Date')['Retorno ano'].sum().round(2)
    if exportar:
        retorno_ano_agrupado.to_csv(f'../TRAININGS/PROJETO_02_crypto/file/ready/{criptomoeda}_retorno_ano.csv')

    # Cálculo do Retorno acumulado
    retorno_acumulado = retorno_ano[['Symbol', 'Retorno ano']].copy()
    retorno_acumulado.rename(columns={'Retorno ano': 'Retorno acumulado'}, inplace=True)
    retorno_acumulado = retorno_acumulado.groupby('Symbol')['Retorno acumulado'].sum().round(2)
    if exportar:
        retorno_acumulado.to_csv(f'../TRAININGS/PROJETO_02_crypto/file/ready/{criptomoeda}_retorno_acumulado.csv', index=False)

    # Cálculo do preço médio
    preco_medio = dataframe[['Symbol', 'Open', 'Close', 'High', 'Low']].copy()
    preco_medio['preco_medio'] = preco_medio[['Open', 'Close', 'High', 'Low']].mean(axis=1).round(2)
    preco_medio = preco_medio.groupby('Symbol')['preco_medio'].mean().round(2)
    if exportar:
        preco_medio.to_csv(f'../TRAININGS/PROJETO_02_crypto/file/ready/{criptomoeda}_preco_medio.csv', index=False)

    # Cálculo da volatilidade: desvio padrão por ano
    volatilidade_ano = dataframe[['Symbol', 'Date', 'Close']].copy()
    volatilidade_ano['Date'] = pd.to_datetime(volatilidade_ano['Date']).dt.strftime('%Y')
    volatilidade_ano = volatilidade_ano.groupby('Date')['Close'].std(ddof=1).round(2)
    if exportar:
        volatilidade_ano.to_csv(f'../TRAININGS/PROJETO_02_crypto/file/ready/{criptomoeda}_volatilidade_ano.csv')

def analise_cripto(dataframe):

    criptomoeda = dataframe.loc[0, 'Symbol']
    dataframe['Date'] = pd.to_datetime(dataframe['Date']).dt.strftime('%Y')
    ano_inicial = dataframe.loc[0, 'Date']
    ano_final = dataframe.iloc[-1]['Date']
    maior_preco = round(dataframe['Close'].max(), 2)
    menor_preco = round(dataframe['Close'].min(), 2)
    media_preco = dataframe['Close'].mean().round(2)
    valorizacao = round(((dataframe.iloc[-1]['Close'] - dataframe.loc[0, 'Close']) / dataframe.loc[0, 'Close']) * 100, 2)

    with open(analise_caminho, 'a', encoding='utf-8') as w:
        w.write(f'ANÁLISE DA CRIPTOMOEDA: {criptomoeda}\n\n- Maior preço de {criptomoeda}: ${maior_preco}\n- Menor preço de {criptomoeda}: ${menor_preco}\n- Média de preço de {criptomoeda}: ${media_preco}\n- Valorização de {criptomoeda} entre {ano_inicial} e {ano_final}: {valorizacao}%\n\n\n')

def serie_temporal_precos_BTCxETH(dataframe1, dataframe2):

    BTC_base_series = dataframe1[['Date', 'Close']]
    BTC_base_series['Date'] = pd.to_datetime(BTC_base_series['Date']).dt.strftime('%Y-%m')
    BTC_base_series = BTC_base_series[BTC_base_series['Date'].str.startswith('2020')]
    BTC_series_precos = BTC_base_series.set_index('Date')['Close']

    ETH_base_series = dataframe2[['Date', 'Close']]
    ETH_base_series['Date'] = pd.to_datetime(ETH_base_series['Date']).dt.strftime('%Y-%m')
    ETH_base_series = ETH_base_series[ETH_base_series['Date'].str.startswith('2020')]
    ETH_series_precos = ETH_base_series.set_index('Date')['Close']

    figura, grafico = plt.subplots(figsize=(20,10))

    grafico.plot(BTC_series_precos, "-y", label='BTC')
    grafico.plot(ETH_series_precos, "-p", label='ETH')
    grafico.legend(loc='upper left')
    grafico.set_xlabel('DATA')
    grafico.set_ylabel('PREÇO')
    grafico.set_title('GRÁFICO DE COMPARAÇÃO em 2020: BTC x ETH')
    figura.savefig('../TRAININGS/PROJETO_02_crypto/img/serie_temporal_precos_BTCxETH.png')

def histograma_retornos(dataframe, crypto=''):
    if crypto not in ('BTC', 'ETH'):
        print('\nVocê forneceu um código errado de criptomoeda, favor forneça "BTC" ou "ETH".\n')
        exit
    elif crypto == 'BTC':
        titulo_hist = 'HISTOGRAMA DO RETORNO: BTC'
        caminho_hist = '../TRAININGS/PROJETO_02_crypto/img/BTC_histograma_retornos.png'
    elif crypto == 'ETH':
        titulo_hist = 'HISTOGRAMA DO RETORNO: ETH'
        caminho_hist = '../TRAININGS/PROJETO_02_crypto/img/ETH_histograma_retornos.png'

    base_hist = dataframe.iloc[:, -1]

    figura, grafico = plt.subplots(figsize=(20,10))

    grafico.hist(base_hist, color='red', edgecolor='black')
    grafico.set_xlabel('RETORNOS')
    grafico.set_ylabel('QUANTIDADE DE RETORNOS')
    grafico.set_title(titulo_hist)
    figura.savefig(caminho_hist)

def volatilidade_ano(dataframe, crypto=''):
    if crypto not in ('BTC', 'ETH'):
        print('\nVocê forneceu um código errado de criptomoeda, favor forneça "BTC" ou "ETH".\n')
        exit
    elif crypto == 'BTC':
        titulo_hist = 'GRÁFICO DA VOLATILIDADE/DESVIO PADRÃO: BTC'
        caminho_hist = '../TRAININGS/PROJETO_02_crypto/img/BTC_volatilidade_ano.png'
    elif crypto == 'ETH':
        titulo_hist = 'GRÁFICO DA VOLATILIDADE/DESVIO PADRÃO: ETH'
        caminho_hist = '../TRAININGS/PROJETO_02_crypto/img/ETH_volatilidade_ano.png'
    

    figura, grafico = plt.subplots(figsize=(20,10))

    grafico.barh(dataframe['Date'], dataframe['Close'], color="green")
    grafico.set_xlabel('DATA')
    grafico.set_ylabel('VOLATILIDADE')
    grafico.set_title(titulo_hist, fontsize=16, fontweight='bold')
    figura.savefig(caminho_hist)

def boxplot_retornos_mes_BTCxETH(dataframe1, dataframe2):

    BTC = dataframe1['Retorno mes']
    ETH = dataframe2['Retorno mes']
    

    figura, grafico = plt.subplots(figsize=(20,10))

    grafico.boxplot([BTC, ETH], labels=['BTC', 'ETH'])
    grafico.set_xlabel('MENSAL')
    grafico.set_ylabel('RETORNOS')
    grafico.set_title('BOXPLOT COMPARATIVO DE RETORNOS MENSAIS: BTC x ETH', fontsize=16, fontweight='bold')
    figura.savefig('../TRAININGS/PROJETO_02_crypto/img/boxplot_retornos_mes_BTCxETH.png')

def calcular_lucro(qtd_compra, cambio_compra, valor_investido, crypto=''):

    if crypto not in ('BTC', 'ETH'):
        print('\nVocê forneceu um código errado de criptomoeda, favor forneça "BTC" ou "ETH".\n')
        exit
    elif crypto == 'BTC':
        BTC_atual = BTC_df['Close'].iloc[-1]

        BTC_venda_atual = BTC_atual * qtd_compra
        BTC_venda_fornecida = (cambio_compra * qtd_compra) - valor_investido

        BTC_valorizacao_cripto = round(((BTC_atual - cambio_compra) / cambio_compra) * 100, 2)
        BTC_percentual_retorno_financeiro = round(((BTC_venda_fornecida - BTC_venda_atual) / BTC_venda_fornecida) * 100, 2)
        BTC_valor_retorno_financeiro = round(BTC_venda_atual - BTC_venda_fornecida, 2)

        print(f'\nValor de retorno: ${BTC_valor_retorno_financeiro}\nPercentual de retorno: {BTC_percentual_retorno_financeiro}%\nValorização da criptomoeda: {BTC_valorizacao_cripto}%')
    elif crypto == 'ETH':
    
        ETH_atual = ETH_df['Close'].iloc[-1]

        ETH_venda_atual = ETH_atual * qtd_compra
        ETH_venda_fornecida = (cambio_compra * qtd_compra) - valor_investido

        ETH_valorizacao_cripto = round(((ETH_atual - cambio_compra) / cambio_compra) * 100, 2)
        ETH_percentual_retorno_financeiro = round(((ETH_venda_fornecida - ETH_venda_atual) / ETH_venda_fornecida) * 100, 2)
        ETH_valor_retorno_financeiro = round(ETH_venda_atual - ETH_venda_fornecida, 2)

        print(f'\nValor de retorno: ${ETH_valor_retorno_financeiro}\nPercentual de retorno: {ETH_percentual_retorno_financeiro}%\nValorização da criptomoeda: {ETH_valorizacao_cripto}%')

calcular_lucro(5, 134.74, 1600, crypto='ETH')

metricas(ETH_df, exportar=True)
serie_temporal_precos_BTCxETH(BTC_df, ETH_df)

retornos = pd.read_csv('../TRAININGS/PROJETO_02_crypto/file/ready/ETH_retorno_dia.csv')
histograma_retornos(retornos, crypto='ETH')

volatilidade = pd.read_csv('../TRAININGS/PROJETO_02_crypto/file/ready/BTC_volatilidade_ano.csv')
volatilidade_ano(volatilidade, crypto='BTC')

BTC_retorno_mes = pd.read_csv('../TRAININGS/PROJETO_02_crypto/file/ready/BTC_retorno_mes.csv')
ETH_retorno_mes = pd.read_csv('../TRAININGS/PROJETO_02_crypto/file/ready/ETH_retorno_mes.csv')

boxplot_retornos_mes_BTCxETH(BTC_retorno_mes, ETH_retorno_mes)

analise_cripto(ETH_df)


