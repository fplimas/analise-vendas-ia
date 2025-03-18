# Este arquivo contém funções para geração de relatórios PDF com gráficos e análises.

from fpdf import FPDF
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Relatório de Análise de Vendas', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')


def gerar_relatorio(titulo, conteudo, caminho_arquivo):
    """Gera um relatório PDF com o título e conteúdo fornecidos."""
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, titulo, 0, 1, 'C')
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, conteudo)
    pdf.output(caminho_arquivo)


def gerar_relatorio_completo(df, caminho_arquivo):
    """Gera um relatório PDF completo com resumo, gráficos e previsões."""
    pdf = PDF()
    pdf.add_page()

    # Resumo das vendas
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Resumo das Vendas', 0, 1, 'C')
    resumo = df.describe().to_string()
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, resumo)

    # Gráficos
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Gráficos de Vendas', 0, 1, 'C')

    # Receita Total por Mês
    plt.figure()
    receita_por_mes = df.groupby('Mês/Ano')['Receita Total'].sum()
    receita_por_mes.plot(kind='bar')
    plt.title('Receita Total por Mês')
    plt.xlabel('Mês/Ano')
    plt.ylabel('Receita Total')
    plt.xticks(rotation=45)
    plt.tight_layout()
    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    pdf.image(img_buf, x=10, y=None, w=180)
    plt.close()

    # Previsões do Modelo de IA
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Previsões do Modelo de IA', 0, 1, 'C')
    previsoes = prever_receita(df, modelo='linear_regression')
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, f"R²: {previsoes['r2']:.2f}\nMAE: {previsoes['mae']:.2f}")

    pdf.output(caminho_arquivo)

# Exemplo de uso
if __name__ == "__main__":
    df = pd.read_csv('data/vendas.csv')
    df['Mês/Ano'] = pd.to_datetime(df['Data']).dt.to_period('M')
    df['Receita Total'] = df['Quantidade'] * df['Preço']
    gerar_relatorio_completo(df, 'reports/relatorio_vendas.pdf') 