import pandas as pd
from bs4 import BeautifulSoup
import re

def extract_tesla_revenue_tables(html_content):
    """
    Extrai as tabelas de receita da Tesla do HTML fornecido
    
    Args:
        html_content (str): Conteúdo HTML da página
        
    Returns:
        tuple: (annual_revenue_df, quarterly_revenue_df)
    """
    
    # Parse o HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Encontrar todas as tabelas
    tables = soup.find_all('table', class_='historical_data_table')
    
    annual_revenue_data = []
    quarterly_revenue_data = []
    
    for table in tables:
        # Verificar se é a tabela de receita anual
        header = table.find('thead')
        if header and 'Tesla Annual Revenue' in header.get_text():
            rows = table.find('tbody').find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                if len(cells) == 2:
                    year = cells[0].get_text(strip=True)
                    revenue = cells[1].get_text(strip=True)
                    # Remover o símbolo $ e converter para número
                    revenue_clean = revenue.replace('$', '').replace(',', '')
                    if revenue_clean and revenue_clean != '':
                        annual_revenue_data.append({
                            'Date': year,
                            'Revenue': int(revenue_clean)
                        })
        
        # Verificar se é a tabela de receita trimestral
        elif header and 'Tesla Quarterly Revenue' in header.get_text():
            rows = table.find('tbody').find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                if len(cells) == 2:
                    date = cells[0].get_text(strip=True)
                    revenue = cells[1].get_text(strip=True)
                    # Remover o símbolo $ e converter para número
                    revenue_clean = revenue.replace('$', '').replace(',', '')
                    if revenue_clean and revenue_clean != '':
                        quarterly_revenue_data.append({
                            'Date': date,
                            'Revenue': int(revenue_clean)
                        })
    
    # Criar DataFrames
    annual_df = pd.DataFrame(annual_revenue_data)
    quarterly_df = pd.DataFrame(quarterly_revenue_data)
    
    return annual_df, quarterly_df

def extract_tesla_revenue_from_html_file(html_content):
    """
    Função principal para extrair dados de receita da Tesla
    """
    print("Extraindo dados de receita da Tesla...")
    
    annual_revenue, quarterly_revenue = extract_tesla_revenue_tables(html_content)
    
    print("\n=== RECEITA ANUAL DA TESLA ===")
    print(annual_revenue)
    print(f"\nTotal de registros anuais: {len(annual_revenue)}")
    
    print("\n=== RECEITA TRIMESTRAL DA TESLA ===")
    print(quarterly_revenue)
    print(f"\nTotal de registros trimestrais: {len(quarterly_revenue)}")
    
    # Salvar em arquivos CSV
    annual_revenue.to_csv('tesla_annual_revenue.csv', index=False)
    quarterly_revenue.to_csv('tesla_quarterly_revenue.csv', index=False)
    
    print("\nArquivos salvos:")
    print("- tesla_annual_revenue.csv")
    print("- tesla_quarterly_revenue.csv")
    
    return annual_revenue, quarterly_revenue

# Exemplo de uso
if __name__ == "__main__":
    # Aqui você pode colar o HTML que você forneceu
    # Por enquanto, vou criar um exemplo com dados fictícios para demonstrar
    
    print("Para usar este script:")
    print("1. Cole o HTML da página da Tesla no arquivo")
    print("2. Execute o script para extrair as tabelas")
    print("3. Os dados serão salvos em arquivos CSV") 