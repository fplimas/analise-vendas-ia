# Este arquivo contém a implementação do modelo de machine learning para previsão de vendas.

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import pandas as pd


def treinar_modelo(df, modelo='linear_regression'):
    """Treina um modelo de machine learning para previsão de vendas."""
    X = df.drop('vendas', axis=1)
    y = df['vendas']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    if modelo == 'linear_regression':
        model = LinearRegression()
    elif modelo == 'random_forest':
        model = RandomForestRegressor()
    else:
        raise ValueError("Modelo não suportado: escolha 'linear_regression' ou 'random_forest'")
    
    model.fit(X_train, y_train)
    previsoes = model.predict(X_test)
    mse = mean_squared_error(y_test, previsoes)
    
    return model, mse 


def prever_receita(df, modelo='linear_regression'):
    # Preparar os dados
    X = df[['Quantidade', 'Preço']]
    y = df['Receita Total']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Treinar o modelo
    if modelo == 'linear_regression':
        model = LinearRegression()
    elif modelo == 'random_forest':
        model = RandomForestRegressor()
    else:
        raise ValueError("Modelo não suportado: escolha 'linear_regression' ou 'random_forest'")

    model.fit(X_train, y_train)

    # Avaliar o modelo
    previsoes = model.predict(X_test)
    r2 = model.score(X_test, y_test)
    mae = mean_squared_error(y_test, previsoes, squared=False)
    print(f"R²: {r2:.2f}")
    print(f"MAE: {mae:.2f}")

    # Plotar gráfico de valores reais vs. previstos
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, previsoes, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
    plt.xlabel('Valores Reais')
    plt.ylabel('Valores Previstos')
    plt.title('Comparação de Valores Reais vs. Previstos')
    plt.show()

# Exemplo de uso
if __name__ == "__main__":
    df = pd.read_csv('data/vendas.csv')
    df['Receita Total'] = df['Quantidade'] * df['Preço']
    prever_receita(df, modelo='linear_regression') 