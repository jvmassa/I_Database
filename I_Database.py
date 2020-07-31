# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 18:46:26 2020

@author: massa
"""

import pandas as pd
import yfinance as yf


def importa_ticker(ticker, s_date, e_date):
    """
    Inputs:
    tickers: code of a certain asset. Must be a string.
    s_date: first trading date.
    e_date: last trading date.
    ------------------------------------------------------------    
    """
    df = yf.download(ticker, start = s_date, end = e_date, 
                     auto_adjust = True)    
    df = df.dropna()        
    return df

def importa_tickers(tickers, s_date, e_date):
    lista = []
    data = pd.DataFrame()
    for i in range(len(tickers)):
        lista.append(tickers[i])

    for i in range(len(lista)):
        data[i] = yf.download(lista[i], start = s_date, end = e_date, 
            auto_adjust = True)['Close']
    
    dic = { i : lista[i] for i in range(0, len(lista) ) }
    data = data.rename(columns = dic)
    data = data.dropna() #remove valores em branco do df

    return data

def importa_bc(codigo):
    url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(codigo)
    df = pd.read_json(url)
    df['data'] = pd.to_datetime(df['data'], dayfirst = True)
    df.set_index('data', inplace = True)
    return df

def importa_cdi(s_date, e_date,codigo = 4389):
    df = importa_bc(codigo)
    df['valor'] = df['valor']/100
    return df[s_date:e_date]
    