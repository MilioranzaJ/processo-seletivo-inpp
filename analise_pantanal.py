import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    file_path = 'dados_pantanal.csv'
    
    if not os.path.exists(file_path):
        print(f"Erro: O arquivo {file_path} não foi encontrado no diretório atual.")
        return

    df = pd.read_csv(file_path, parse_dates=['data'])
    df.set_index('data', inplace=True)

    print("--- Dados Originais (com valores nulos) ---")
    print(df)
    print("\n")

    df_tratado = df.interpolate(method='time')

    print("--- Dados Tratados (após interpolação linear) ---")
    print(df_tratado)
    print("\n")

    medias = df_tratado.mean()
    print("--- Médias Calculadas ---")
    print(f"Temperatura Média (°C): {medias['temperatura_c']:.2f}")
    print(f"Nível do Rio Médio (m): {medias['nivel_rio_m']:.2f}")
    print(f"NDVI Médio: {medias['ndvi']:.4f}")
    print("\n")

    plt.style.use('seaborn-v0_8-darkgrid')
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    ax1.plot(df_tratado.index, df_tratado['temperatura_c'], marker='o', color='tab:red', linestyle='-', linewidth=2)
    ax1.set_title('Evolução da Temperatura no Pantanal (Jan/2025)', fontsize=14)
    ax1.set_ylabel('Temperatura (°C)', fontsize=12)
    ax1.grid(True, linestyle='--', alpha=0.7)

    ax2.plot(df_tratado.index, df_tratado['nivel_rio_m'], marker='s', color='tab:blue', linestyle='-', linewidth=2, label='Nível do Rio (m)')
    ax2.set_ylabel('Nível do Rio (m)', color='tab:blue', fontsize=12)
    ax2.tick_params(axis='y', labelcolor='tab:blue')
    
    ax3 = ax2.twinx()
    ax3.plot(df_tratado.index, df_tratado['ndvi'], marker='^', color='tab:green', linestyle='--', linewidth=2, label='NDVI')
    ax3.set_ylabel('NDVI', color='tab:green', fontsize=12)
    ax3.tick_params(axis='y', labelcolor='tab:green')

    ax2.set_title('Dinâmica Hidrológica e Vegetação (Nível do Rio vs NDVI)', fontsize=14)
    ax2.set_xlabel('Data', fontsize=12)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    output_filename = 'visualizacao_pantanal.png'
    plt.savefig(output_filename, dpi=300)
    print(f"Gráficos gerados e salvos como '{output_filename}'.")
    
    plt.show()

if __name__ == "__main__":
    main()