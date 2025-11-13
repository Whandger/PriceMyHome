from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import numpy as np

def machine(X, Y, Z):
    # Normaliza as features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    Y = np.array(Y)

    # Cria e treina o modelo
    modelo = LinearRegression()
    modelo.fit(X, Y)

    # Nova casa (exemplo fixo por enquanto)
    nova_casa = np.array(Z)
    nova_casa = scaler.transform(nova_casa)  # aplica a mesma escala

    # Faz a previsão e garante que não seja negativa
    previsao = modelo.predict(nova_casa)[0]
    previsao = max(previsao, 0)

    return f"Preço estimado: R$ {previsao:.2f} mil"
