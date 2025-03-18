# Este arquivo contém funções para leitura e limpeza de dados de vendas.

import pandas as pd


def ler_dados(caminho_arquivo):
    """Lê o arquivo CSV e retorna um DataFrame do pandas."""
    return pd.read_csv(caminho_arquivo)


def limpar_dados(df):
    """Realiza a limpeza dos dados, removendo valores nulos e duplicados."""
    df = df.dropna()
    df = df.drop_duplicates()
    return df 


def processar_dados(caminho_arquivo):
    # Ler o arquivo CSV
    df = ler_dados(caminho_arquivo)
    
    # Remover valores nulos e duplicados
    df = limpar_dados(df)
    
    # Criar coluna 'Receita Total'
    df['Receita Total'] = df['Quantidade'] * df['Preço']
    
    # Criar coluna 'Mês/Ano'
    df['Mês/Ano'] = pd.to_datetime(df['Data']).dt.to_period('M')
    
    # Exibir resumo dos dados
    print("Resumo dos Dados:")
    print(df.describe())
    print("\nDados após limpeza:")
    print(df.head())

# Exemplo de uso
if __name__ == "__main__":
    processar_dados('data/vendas.csv') 