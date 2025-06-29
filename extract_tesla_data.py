import pandas as pd
from bs4 import BeautifulSoup

# HTML fornecido (você pode colar o HTML completo aqui)
html_content = """<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
<head>
<meta charset="utf-8"/>
<meta content="IE=edge,chrome=1" http-equiv="X-UA-Compatible"/>
<link href="https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue" rel="canonical"/>
<title>Tesla Revenue 2010-2022 | TSLA | MacroTrends</title>
<!-- ... resto do HTML ... -->
</head>
<body class="fuelux">
<!-- ... conteúdo da página ... -->
<div id="style-1" style="background-color:#fff; height:510px; overflow:auto; margin: 30px 0px 30px 0px; padding:0px 30px 20px 0px; border:1px solid #dfdfdf;">
<div class="col-xs-6">
<table class="historical_data_table table">
<thead>
<tr>
<th colspan="2" style="text-align:center">Tesla Annual Revenue<br/><span style="font-size:14px;">(Millions of US $)</span></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">2021</td>
<td style="text-align:center">$53,823</td>
</tr>
<tr>
<td style="text-align:center">2020</td>
<td style="text-align:center">$31,536</td>
</tr>
<tr>
<td style="text-align:center">2019</td>
<td style="text-align:center">$24,578</td>
</tr>
<tr>
<td style="text-align:center">2018</td>
<td style="text-align:center">$21,461</td>
</tr>
<tr>
<td style="text-align:center">2017</td>
<td style="text-align:center">$11,759</td>
</tr>
<tr>
<td style="text-align:center">2016</td>
<td style="text-align:center">$7,000</td>
</tr>
<tr>
<td style="text-align:center">2015</td>
<td style="text-align:center">$4,046</td>
</tr>
<tr>
<td style="text-align:center">2014</td>
<td style="text-align:center">$3,198</td>
</tr>
<tr>
<td style="text-align:center">2013</td>
<td style="text-align:center">$2,013</td>
</tr>
<tr>
<td style="text-align:center">2012</td>
<td style="text-align:center">$413</td>
</tr>
<tr>
<td style="text-align:center">2011</td>
<td style="text-align:center">$204</td>
</tr>
<tr>
<td style="text-align:center">2010</td>
<td style="text-align:center">$117</td>
</tr>
<tr>
<td style="text-align:center">2009</td>
<td style="text-align:center">$112</td>
</tr>
</tbody>
</table>
</div>
<div class="col-xs-6">
<table class="historical_data_table table">
<thead>
<tr>
<th colspan="2" style="text-align:center">Tesla Quarterly Revenue<br/><span style="font-size:14px;">(Millions of US $)</span></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">2022-09-30</td>
<td style="text-align:center">$21,454</td>
</tr>
<tr>
<td style="text-align:center">2022-06-30</td>
<td style="text-align:center">$16,934</td>
</tr>
<tr>
<td style="text-align:center">2022-03-31</td>
<td style="text-align:center">$18,756</td>
</tr>
<tr>
<td style="text-align:center">2021-12-31</td>
<td style="text-align:center">$17,719</td>
</tr>
<tr>
<td style="text-align:center">2021-09-30</td>
<td style="text-align:center">$13,757</td>
</tr>
<tr>
<td style="text-align:center">2021-06-30</td>
<td style="text-align:center">$11,958</td>
</tr>
<tr>
<td style="text-align:center">2021-03-31</td>
<td style="text-align:center">$10,389</td>
</tr>
<tr>
<td style="text-align:center">2020-12-31</td>
<td style="text-align:center">$10,744</td>
</tr>
<tr>
<td style="text-align:center">2020-09-30</td>
<td style="text-align:center">$8,771</td>
</tr>
<tr>
<td style="text-align:center">2020-06-30</td>
<td style="text-align:center">$6,036</td>
</tr>
<tr>
<td style="text-align:center">2020-03-31</td>
<td style="text-align:center">$5,985</td>
</tr>
<tr>
<td style="text-align:center">2019-12-31</td>
<td style="text-align:center">$7,384</td>
</tr>
<tr>
<td style="text-align:center">2019-09-30</td>
<td style="text-align:center">$6,303</td>
</tr>
<tr>
<td style="text-align:center">2019-06-30</td>
<td style="text-align:center">$6,350</td>
</tr>
<tr>
<td style="text-align:center">2019-03-31</td>
<td style="text-align:center">$4,541</td>
</tr>
<tr>
<td style="text-align:center">2018-12-31</td>
<td style="text-align:center">$7,226</td>
</tr>
<tr>
<td style="text-align:center">2018-09-30</td>
<td style="text-align:center">$6,824</td>
</tr>
<tr>
<td style="text-align:center">2018-06-30</td>
<td style="text-align:center">$4,002</td>
</tr>
<tr>
<td style="text-align:center">2018-03-31</td>
<td style="text-align:center">$3,409</td>
</tr>
<tr>
<td style="text-align:center">2017-12-31</td>
<td style="text-align:center">$3,288</td>
</tr>
<tr>
<td style="text-align:center">2017-09-30</td>
<td style="text-align:center">$2,985</td>
</tr>
<tr>
<td style="text-align:center">2017-06-30</td>
<td style="text-align:center">$2,790</td>
</tr>
<tr>
<td style="text-align:center">2017-03-31</td>
<td style="text-align:center">$2,696</td>
</tr>
<tr>
<td style="text-align:center">2016-12-31</td>
<td style="text-align:center">$2,285</td>
</tr>
<tr>
<td style="text-align:center">2016-09-30</td>
<td style="text-align:center">$2,298</td>
</tr>
<tr>
<td style="text-align:center">2016-06-30</td>
<td style="text-align:center">$1,270</td>
</tr>
<tr>
<td style="text-align:center">2016-03-31</td>
<td style="text-align:center">$1,147</td>
</tr>
<tr>
<td style="text-align:center">2015-12-31</td>
<td style="text-align:center">$1,214</td>
</tr>
<tr>
<td style="text-align:center">2015-09-30</td>
<td style="text-align:center">$937</td>
</tr>
<tr>
<td style="text-align:center">2015-06-30</td>
<td style="text-align:center">$955</td>
</tr>
<tr>
<td style="text-align:center">2015-03-31</td>
<td style="text-align:center">$940</td>
</tr>
<tr>
<td style="text-align:center">2014-12-31</td>
<td style="text-align:center">$957</td>
</tr>
<tr>
<td style="text-align:center">2014-09-30</td>
<td style="text-align:center">$852</td>
</tr>
<tr>
<td style="text-align:center">2014-06-30</td>
<td style="text-align:center">$769</td>
</tr>
<tr>
<td style="text-align:center">2014-03-31</td>
<td style="text-align:center">$621</td>
</tr>
<tr>
<td style="text-align:center">2013-12-31</td>
<td style="text-align:center">$615</td>
</tr>
<tr>
<td style="text-align:center">2013-09-30</td>
<td style="text-align:center">$431</td>
</tr>
<tr>
<td style="text-align:center">2013-06-30</td>
<td style="text-align:center">$405</td>
</tr>
<tr>
<td style="text-align:center">2013-03-31</td>
<td style="text-align:center">$562</td>
</tr>
<tr>
<td style="text-align:center">2012-12-31</td>
<td style="text-align:center">$306</td>
</tr>
<tr>
<td style="text-align:center">2012-09-30</td>
<td style="text-align:center">$50</td>
</tr>
<tr>
<td style="text-align:center">2012-06-30</td>
<td style="text-align:center">$27</td>
</tr>
<tr>
<td style="text-align:center">2012-03-31</td>
<td style="text-align:center">$30</td>
</tr>
<tr>
<td style="text-align:center">2011-12-31</td>
<td style="text-align:center">$39</td>
</tr>
<tr>
<td style="text-align:center">2011-09-30</td>
<td style="text-align:center">$58</td>
</tr>
<tr>
<td style="text-align:center">2011-06-30</td>
<td style="text-align:center">$58</td>
</tr>
<tr>
<td style="text-align:center">2011-03-31</td>
<td style="text-align:center">$49</td>
</tr>
<tr>
<td style="text-align:center">2010-12-31</td>
<td style="text-align:center">$36</td>
</tr>
<tr>
<td style="text-align:center">2010-09-30</td>
<td style="text-align:center">$31</td>
</tr>
<tr>
<td style="text-align:center">2010-06-30</td>
<td style="text-align:center">$28</td>
</tr>
<tr>
<td style="text-align:center">2010-03-31</td>
<td style="text-align:center">$21</td>
</tr>
<tr>
<td style="text-align:center">2009-12-31</td>
<td style="text-align:center"></td>
</tr>
<tr>
<td style="text-align:center">2009-09-30</td>
<td style="text-align:center">$46</td>
</tr>
<tr>
<td style="text-align:center">2009-06-30</td>
<td style="text-align:center">$27</td>
</tr>
</tbody>
</table>
</div>
</div>
<!-- ... resto do HTML ... -->
</body>
</html>"""

def extract_tesla_revenue_data():
    """
    Extrai os dados de receita da Tesla do HTML fornecido
    """
    # Parse o HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Encontrar as tabelas
    tables = soup.find_all('table', class_='historical_data_table')
    
    annual_data = []
    quarterly_data = []
    
    for table in tables:
        # Verificar o cabeçalho da tabela
        header = table.find('thead')
        if header:
            header_text = header.get_text()
            
            # Tabela de receita anual
            if 'Tesla Annual Revenue' in header_text:
                rows = table.find('tbody').find_all('tr')
                for row in rows:
                    cells = row.find_all('td')
                    if len(cells) == 2:
                        year = cells[0].get_text(strip=True)
                        revenue = cells[1].get_text(strip=True)
                        
                        # Limpar o valor da receita
                        if revenue and revenue != '':
                            revenue_clean = revenue.replace('$', '').replace(',', '')
                            annual_data.append({
                                'Date': year,
                                'Revenue': int(revenue_clean)
                            })
            
            # Tabela de receita trimestral
            elif 'Tesla Quarterly Revenue' in header_text:
                rows = table.find('tbody').find_all('tr')
                for row in rows:
                    cells = row.find_all('td')
                    if len(cells) == 2:
                        date = cells[0].get_text(strip=True)
                        revenue = cells[1].get_text(strip=True)
                        
                        # Limpar o valor da receita
                        if revenue and revenue != '':
                            revenue_clean = revenue.replace('$', '').replace(',', '')
                            quarterly_data.append({
                                'Date': date,
                                'Revenue': int(revenue_clean)
                            })
    
    # Criar DataFrames
    annual_df = pd.DataFrame(annual_data)
    quarterly_df = pd.DataFrame(quarterly_data)
    
    return annual_df, quarterly_df

# Executar a extração
if __name__ == "__main__":
    print("Extraindo dados de receita da Tesla...")
    
    annual_revenue, quarterly_revenue = extract_tesla_revenue_data()
    
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
    
    # Mostrar estatísticas básicas
    print("\n=== ESTATÍSTICAS ===")
    print(f"Receita anual mais recente (2021): ${annual_revenue.iloc[0]['Revenue']:,} milhões")
    print(f"Receita trimestral mais recente (2022-09-30): ${quarterly_revenue.iloc[0]['Revenue']:,} milhões")
    print(f"Período coberto: {annual_revenue['Date'].min()} a {annual_revenue['Date'].max()}") 