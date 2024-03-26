import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def load_data(file_path):
    """
    Carrega os dados do arquivo CSV especificado.

    Args:
    file_path (str): Caminho do arquivo CSV.

    Returns:
    DataFrame: Dataframe contendo os dados carregados.
    """
    df = pd.read_csv(file_path)
    df['Date/Time'] = pd.to_datetime(df['Date/Time'], format='%d %m %Y %H:%M')
    return df


def plot_power_wind_relationship(df):
    """
    Plota a relação entre a velocidade do vento e a potência ativa gerada.

    Args:
    df (DataFrame): Dataframe contendo os dados.
    """
    sns.scatterplot(data=df, x='Wind Speed (m/s)', y='LV ActivePower (kW)')
    plt.xlabel('Velocidade do Vento (m/s)')
    plt.ylabel('Potência Ativa (kW)')
    plt.title('Relação entre Velocidade do Vento e Potência Ativa Gerada')
    plt.show()


def plot_power_comparison(df):
    """
    Plota a comparação entre a potência ativa real e a potência teórica esperada.

    Args:
    df (DataFrame): Dataframe contendo os dados.
    """
    sns.scatterplot(data=df, x='Wind Speed (m/s)', y='Theoretical_Power_Curve (KWh)')
    plt.xlabel('Velocidade do Vento (m/s)')
    plt.ylabel('Potência Teórica (KWh)')
    plt.title('Comparação entre Potência Ativa Real e Potência Teórica Esperada')
    plt.show()


def calculate_power_limits(df):
    """
    Calcula os limites aceitáveis para a potência real em relação à potência teórica.

    Args:
    df (DataFrame): Dataframe contendo os dados.

    Returns:
    list: Lista contendo os rótulos de conformidade ('dentro', 'fora', 'zero').
    """
    pot_real = df['LV ActivePower (kW)']
    pot_teorica = df['Theoretical_Power_Curve (KWh)']
    pot_max = pot_teorica * 1.05
    pot_min = pot_teorica * 0.95
    dentro_limite = ['dentro' if pot_min[i] <= pot_real[i] <= pot_max[i] else 'fora' if pot_real[i] != 0 else 'zero' for
                     i in range(len(pot_real))]
    return dentro_limite


def plot_power_compliance(df, compliance_labels):
    """
    Plota os dados coloridos de acordo com a conformidade com os limites de potência.

    Args:
    df (DataFrame): Dataframe contendo os dados.
    compliance_labels (list): Lista contendo os rótulos de conformidade ('dentro', 'fora', 'zero').
    """
    cores = {'dentro': 'blue', 'fora': 'red', 'zero': 'orange'}
    sns.scatterplot(data=df, x='Wind Speed (m/s)', y='LV ActivePower (kW)', hue=compliance_labels, s=1, palette=cores)
    plt.xlabel('Velocidade do Vento (m/s)')
    plt.ylabel('Potência Ativa (kW)')
    plt.title('Conformidade da Potência Ativa com os Limites Teóricos')
    plt.show()


if __name__ == "__main__":
    file_path = 'T1.csv'
    df = load_data(file_path)
    plot_power_wind_relationship(df)
    plot_power_comparison(df)
    compliance_labels = calculate_power_limits(df)
    plot_power_compliance(df, compliance_labels)
