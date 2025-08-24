# -*- coding: utf-8 -*- 

"""
Script principal para orquestrar a execução completa do projeto de Análise de Cesta de Compras.

Este script executa as seguintes etapas em ordem:
1.  Download dos datasets do Kaggle.
2.  Preparação e Análise do dataset "sujo" (Online Retail).
3.  Preparação e Análise do dataset "limpo" (Groceries).
4.  Preparação e Análise do dataset "desorganizado" (Basket).
"""

# Importa as funções principais de cada módulo do projeto
import download_datasets
import data_preparation
import market_basket_analysis
import data_preparation_groceries
import market_basket_analysis_groceries
import data_preparation_basket
import market_basket_analysis_basket

def print_header(title):
    """Imprime um cabeçalho formatado para separar as seções da execução."""
    print("\n" + "="*60)
    print(f"	{title}")
    print("="*60 + "\n")

if __name__ == "__main__":
    # Etapa 1: Download dos dados
    print_header("ETAPA 1: BAIXANDO DATASETS DO KAGGLE")
    download_datasets.main()

    # Etapa 2: Análise do primeiro dataset (Varejo Online "Sujo")
    print_header("ETAPA 2: PROCESSANDO DATASET DE VAREJO ONLINE (SUJO)")
    data_preparation.main()
    market_basket_analysis.main()

    # Etapa 3: Análise do segundo dataset (Groceries "Limpo")
    print_header("ETAPA 3: PROCESSANDO DATASET GROCERIES (LIMPO)")
    data_preparation_groceries.main()
    market_basket_analysis_groceries.main()

    # Etapa 4: Análise do terceiro dataset (Basket "Desorganizado")
    print_header("ETAPA 4: PROCESSANDO DATASET BASKET (DESORGANIZADO)")
    data_preparation_basket.main()
    market_basket_analysis_basket.main()

    print_header("PROCESSO DE ANÁLISE COMPLETO CONCLUÍDO")
