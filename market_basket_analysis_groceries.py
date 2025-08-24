
import pandas as pd
import pickle
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# --- Constantes ---
INPUT_PICKLE_PATH = '/home/hp/market_basket_analysis/prepared_transactions_groceries.pkl'

def main():
    """Carrega as transações do dataset Groceries, executa a análise e exibe os resultados."""
    
    # Passo 1: Carregar os Dados Preparados
    print(f"Carregando transações de: {INPUT_PICKLE_PATH}")
    try:
        with open(INPUT_PICKLE_PATH, 'rb') as f:
            transactions = pickle.load(f)
        print(f"{len(transactions)} transações carregadas com sucesso.")
    except FileNotFoundError:
        print(f"Erro: Arquivo de transações não encontrado em '{INPUT_PICKLE_PATH}'.")
        print("Por favor, execute o script 'data_preparation_groceries.py' primeiro.")
        return
    except Exception as e:
        print(f"Um erro ocorreu ao carregar o arquivo: {e}")
        return

    # Passo 2: Codificar os Dados para o Formato One-Hot
    print("Codificando transações para o formato binário...")
    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    df_encoded = pd.DataFrame(te_ary, columns=te.columns_)
    print("Codificação concluída.")

    # Passo 3: Aplicar o Algoritmo Apriori
    # Usamos um min_support de 0.01 (1%) como ponto de partida.
    print("Aplicando o algoritmo Apriori para encontrar itemsets frequentes (min_support=0.01)...")
    frequent_itemsets = apriori(df_encoded, min_support=0.01, use_colnames=True)
    print(f"Encontrados {len(frequent_itemsets)} itemsets frequentes.")

    # Passo 4: Gerar Regras de Associação
    # Usamos uma confiança mínima de 0.2 (20%) como ponto de partida.
    print("Gerando regras de associação a partir dos itemsets (min_confidence=0.2)...")
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.1)
    print(f"Encontradas {len(rules)} regras de associação.")

    # Passo 5: Ordenar e Exibir os Melhores Resultados
    if not rules.empty:
        rules_sorted = rules.sort_values(by=['lift', 'confidence'], ascending=False)
        
        print("\n--- Top 20 Regras de Associação Mais Fortes (Dataset Groceries) ---")
        print(rules_sorted.head(20).to_string())
    else:
        print("\nNenhuma regra de associação encontrada com os parâmetros definidos.")

if __name__ == "__main__":
    main()
