import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Obtendo os dados históricos das ações da Petrobras
petrobras = yf.Ticker("PETR4.SA")
start_date = datetime.now() - timedelta(days=365*3) # últimos 3 anos
end_date = datetime.now()
historical_data = petrobras.history(start=start_date, end=end_date)

# Calculando a média móvel dos últimos 50 dias
historical_data['MA50'] = historical_data['Close'].rolling(window=50).mean()

# Calculando a média móvel dos últimos 1095 dias
historical_data['MA1095'] = historical_data['Close'].rolling(window=1095).mean()


# Calculando a volatilidade
historical_data['Log_Ret'] = np.log(historical_data['Close'] / historical_data['Close'].shift(1))
historical_data['Volatility'] = historical_data['Log_Ret'].rolling(window=252).std() * np.sqrt(252)

# Plotando o gráfico
plt.figure(figsize=(10, 5))
plt.plot(historical_data.index, historical_data['Close'], label='Preço de Fechamento')
plt.plot(historical_data.index, historical_data['MA50'], label='Média Móvel de 50 dias')
plt.title('Histórico de Preços e Média Móvel de 50 dias da Petrobras')
plt.xlabel('Data')
plt.ylabel('Preço (R$)')
plt.legend()
plt.show()

# Plotando o gráfico
plt.figure(figsize=(10, 5))
plt.plot(historical_data.index, historical_data['Close'], label='Preço de Fechamento')
plt.plot(historical_data.index, historical_data['MA1095'], label='Média Móvel de 1095 dias')
plt.title('Histórico de Preços e Média Móvel de 1095 dias da Petrobras')
plt.xlabel('Data')
plt.ylabel('Preço (R$)')
plt.legend()
plt.show()
