# Análise de Desempenho de Turbina Eólica

Este projeto consiste em um conjunto de algoritmos Python para análise e visualização de dados de desempenho de turbinas eólicas. O código utiliza bibliotecas como Pandas, Seaborn e Matplotlib para carregar dados, gerar gráficos e calcular conformidades com limites de potência.

## Funcionalidades Principais

1. **Carregamento de Dados**
   - O método `load_data(file_path)` carrega os dados de um arquivo CSV especificado e converte a coluna 'Date/Time' para o formato de data.

2. **Visualizações Gráficas**
   - `plot_power_wind_relationship(df)`: Plota a relação entre a velocidade do vento e a potência ativa gerada.
   - `plot_power_comparison(df)`: Plota a comparação entre a potência ativa real e a potência teórica esperada.
   - `plot_power_compliance(df, compliance_labels)`: Plota os dados coloridos de acordo com a conformidade com os limites de potência.

3. **Cálculo de Limites de Potência**
   - `calculate_power_limits(df)`: Calcula os limites aceitáveis para a potência real em relação à potência teórica, classificando cada ponto como 'dentro', 'fora' ou 'zero' dos limites.

## Requisitos

- Python
- Pandas
- Seaborn
- Matplotlib

## Utilização

1. Certifique-se de ter Python e as bibliotecas necessárias instaladas.
2. Baixe o arquivo `T1.csv` ou substitua-o pelo seu conjunto de dados.
3. Execute o arquivo `main.py` para carregar os dados, gerar visualizações e calcular os limites de potência.

```bash
python main.py
