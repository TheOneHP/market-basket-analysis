
import pandas as pd
import pickle

# --- Constantes ---
INPUT_CSV_PATH = '/home/hp/market_basket_analysis/groceries_dataset/basket.csv'
OUTPUT_PICKLE_PATH = '/home/hp/market_basket_analysis/prepared_transactions_basket.pkl'

def main():
    """Carrega os dados do 'basket.csv', limpa e transforma em uma lista de transações."""
    print(f"Iniciando a leitura do arquivo problemático: {INPUT_CSV_PATH}")
    
    try:
        # Lemos o CSV. Como não há um cabeçalho real, usamos header=None.
        df = pd.read_csv(INPUT_CSV_PATH, header=None)
        print("Arquivo carregado com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return

    print("Iniciando a transformação dos dados...")
    
    transactions_list = []
    # Iteramos por cada linha do DataFrame.
    for index, row in df.iterrows():
        # Para cada linha, removemos os valores nulos/vazios (NaN) e criamos uma lista.
        transaction = [item for item in row if pd.notna(item)]
        transactions_list.append(transaction)
    
    print(f"Foram encontradas e processadas {len(transactions_list)} transações.")

    # Salvar o Resultado
    print(f"Salvando a lista de transações em: {OUTPUT_PICKLE_PATH}")
    with open(OUTPUT_PICKLE_PATH, 'wb') as f:
        pickle.dump(transactions_list, f)
    
    print("\nProcesso de preparação de dados para 'basket.csv' concluído com sucesso!")

if __name__ == "__main__":
    main()
