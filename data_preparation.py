import pandas as pd
import pickle

# --- Constantes ---
INPUT_CSV_PATH = '/home/hp/market_basket_analysis/raw_retail_dataset/Assignment-1_Data.csv'
OUTPUT_PICKLE_PATH = '/home/hp/market_basket_analysis/prepared_transactions.pkl'

def main():
    """Orquestra a limpeza e preparação dos dados brutos."""
    print(f"Iniciando a leitura de: {INPUT_CSV_PATH}")
    
    # Passo 1: Carregar os Dados Corretamente
    # Usamos encoding 'utf-8-sig' para lidar com o caractere BOM no início do arquivo.
    try:
        df = pd.read_csv(INPUT_CSV_PATH, sep=';', decimal=',', encoding='utf-8-sig')
        print("Arquivo carregado com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return

    # Passo 2: Limpeza Inicial
    print("Iniciando processo de limpeza...")
    
    # Remove linhas com BillNo ou Itemname faltando
    df.dropna(subset=['BillNo', 'Itemname'], inplace=True)
    
    # Garante que BillNo seja tratado como texto
    df['BillNo'] = df['BillNo'].astype(str)
    
    # Remove transações de cancelamento (que contém 'C' no BillNo)
    df = df[~df['BillNo'].str.contains('C', na=False)]
    
    # Remove itens com quantidade negativa ou zero (devoluções, etc.)
    df = df[df['Quantity'] > 0]
    
    # Limpa espaços em branco extras no nome dos itens
    df['Itemname'] = df['Itemname'].str.strip()
    print("Limpeza inicial concluída.")

    # Passo 3: Transformar para o Formato de Cesta
    print("Agrupando itens por transação para formar as cestas...")
    
    # Agrupa por BillNo e cria uma lista de itens para cada um
    basket = df.groupby('BillNo')['Itemname'].apply(list)
    
    # Converte o resultado para uma lista de listas
    transactions_list = basket.tolist()
    print(f"Foram encontradas {len(transactions_list)} transações únicas.")

    # Passo 4: Salvar o Resultado
    print(f"Salvando a lista de transações em: {OUTPUT_PICKLE_PATH}")
    with open(OUTPUT_PICKLE_PATH, 'wb') as f:
        pickle.dump(transactions_list, f)
    
    print("\nProcesso de preparação de dados concluído com sucesso!")

if __name__ == "__main__":
    main()