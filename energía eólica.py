import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# arquivo CSV
df = pd.read_csv('T1.csv')


# convertendo data
df['Date/Time'] = pd.to_datetime(df['Date/Time'], format='%d %m %Y %H:%M')


# plotando dados
sns.scatterplot(data=df, x='Wind Speed (m/s)', y='LV ActivePower (kW)')
plt.xlabel('Velocidade do Vento (m/s)')
plt.ylabel('Potência Ativa (kW)')
plt.show()


# plotando os dados em um grafico
sns.scatterplot(data=df, x='Wind Speed (m/s)', y='Theoretical_Power_Curve (KWh)')
plt.show()


# criando limitis aceitaveis
pot_real = df['LV ActivePower (kW)'].tolist()
pot_teorica = df['Theoretical_Power_Curve (KWh)'].tolist()
pot_max = []
pot_min = []
dentro_limite = []


for potencia in pot_teorica:
    pot_max.append(potencia*1.05)   # limite de 5% acima
    pot_min.append(potencia*0.95)   # limite de 5% a baixo


for i, potencia in enumerate(pot_real):
    if potencia >= pot_min[i] and potencia <= pot_max[i]:
        dentro_limite.append('dentro')
    elif potencia == 0:
        dentro_limite.append('zero')
    else:
        dentro_limite.append('fora')


# criando coluna dentro limite
df['DentroLimite'] = dentro_limite


cores = {'dentro': 'blue', 'fora': 'red', 'zero': 'orange'}
sns.scatterplot(data=df, x='Wind Speed (m/s)', y='LV ActivePower (kW)', hue='DentroLimite', s=1, palette=cores)
plt.show()











