
import pandas as pd
import pickle

# --- Constantes ---
INPUT_CSV_PATH = '/home/hp/market_basket_analysis/groceries_dataset/Groceries data.csv'
OUTPUT_PICKLE_PATH = '/home/hp/market_basket_analysis/prepared_transactions_groceries.pkl'

def main():
    """Carrega os dados do 'Groceries data.csv', agrupa em transações e salva o resultado."""
    print(f"Iniciando a leitura de: {INPUT_CSV_PATH}")
    
    try:
        # O arquivo parece bem formatado, então uma leitura simples deve funcionar.
        df = pd.read_csv(INPUT_CSV_PATH)
        print("Arquivo carregado com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return

    # Limpeza de dados (se necessário) - para este dataset, parece não ser preciso.
    # Remover espaços em branco extras no nome dos itens para garantir consistência.
    df['itemDescription'] = df['itemDescription'].str.strip()

    print("Agrupando itens por transação (cliente + data) para formar as cestas...")
    
    # Agrupa por 'Member_number' e 'Date' para definir uma transação única.
    # Em seguida, coleta todos os 'itemDescription' para cada transação em uma lista.
    basket = df.groupby(['Member_number', 'Date'])['itemDescription'].apply(list)
    
    # Converte o resultado para uma lista de listas
    transactions_list = basket.tolist()
    print(f"Foram encontradas {len(transactions_list)} transações únicas.")

    # Salvar o Resultado
    print(f"Salvando a lista de transações em: {OUTPUT_PICKLE_PATH}")
    with open(OUTPUT_PICKLE_PATH, 'wb') as f:
        pickle.dump(transactions_list, f)
    
    print("\nProcesso de preparação de dados para 'Groceries' concluído com sucesso!")

if __name__ == "__main__":
    main()
