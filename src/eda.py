# Este arquivo contém funções para análise exploratória de dados e geração de gráficos.

import matplotlib.pyplot as plt
import pandas as pd


def gerar_grafico_vendas_mensais(df):
    """Gera um gráfico de vendas mensais."""
    vendas_mensais = df.groupby(df['data'].dt.to_period('M')).sum()
    vendas_mensais.plot(kind='bar')
    plt.title('Vendas Mensais')
    plt.xlabel('Mês')
    plt.ylabel('Total de Vendas')
    plt.show()


def gerar_grafico_produtos_mais_vendidos(df):
    """Gera um gráfico dos produtos mais vendidos."""
    produtos_mais_vendidos = df['produto'].value_counts().head(10)
    produtos_mais_vendidos.plot(kind='bar')
    plt.title('Produtos Mais Vendidos')
    plt.xlabel('Produto')
    plt.ylabel('Quantidade Vendida')
    plt.show()


def gerar_grafico_receita_por_mes(df):
    """Gera um gráfico de receita total por mês."""
    receita_por_mes = df.groupby('Mês/Ano')['Receita Total'].sum()
    receita_por_mes.plot(kind='bar', figsize=(10, 6))
    plt.title('Receita Total por Mês')
    plt.xlabel('Mês/Ano')
    plt.ylabel('Receita Total')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def gerar_grafico_produto_mais_vendido(df):
    """Gera um gráfico do produto mais vendido."""
    produto_mais_vendido = df['Produto'].value_counts()
    produto_mais_vendido.plot(kind='bar', figsize=(10, 6))
    plt.title('Produto Mais Vendido')
    plt.xlabel('Produto')
    plt.ylabel('Quantidade Vendida')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def gerar_grafico_receita_por_produto(df):
    """Gera um gráfico de receita total por produto."""
    receita_por_produto = df.groupby('Produto')['Receita Total'].sum()
    receita_por_produto.plot(kind='bar', figsize=(10, 6))
    plt.title('Receita Total por Produto')
    plt.xlabel('Produto')
    plt.ylabel('Receita Total')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def gerar_grafico_evolucao_vendas(df):
    """Gera um gráfico da evolução das vendas ao longo do tempo."""
    vendas_ao_longo_do_tempo = df.groupby('Data')['Quantidade'].sum()
    vendas_ao_longo_do_tempo.plot(kind='line', figsize=(10, 6))
    plt.title('Evolução das Vendas ao Longo do Tempo')
    plt.xlabel('Data')
    plt.ylabel('Quantidade Vendida')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Exemplo de uso
if __name__ == "__main__":
    df = pd.read_csv('data/vendas.csv')
    df['Mês/Ano'] = pd.to_datetime(df['Data']).dt.to_period('M')
    df['Receita Total'] = df['Quantidade'] * df['Preço']
    gerar_grafico_receita_por_mes(df)
    gerar_grafico_produto_mais_vendido(df)
    gerar_grafico_receita_por_produto(df)
    gerar_grafico_evolucao_vendas(df) 