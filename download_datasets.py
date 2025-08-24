import kagglehub
import os
import shutil

# --- Datasets provided by the user ---
DATASETS = {
    "groceries": {
        "slug": "rashikrahmanpritom/groceries-dataset-for-market-basket-analysismba",
        "target_dir": "/home/hp/market_basket_analysis/groceries_dataset"
    },
    "raw_retail": {
        "slug": "aslanahmedov/market-basket-analysis",
        "target_dir": "/home/hp/market_basket_analysis/raw_retail_dataset"
    }
}

def download_and_copy(slug, target_path):
    """Baixa um dataset do Kaggle e copia os arquivos para um diretório de destino."""
    print(f"--- Processando: {slug} ---")
    try:
        print("Baixando e verificando o caminho...")
        # kagglehub agora retorna o caminho para a PASTA com os arquivos descompactados
        source_dir = kagglehub.dataset_download(slug)
        print(f"Download concluído. Arquivos de origem em: {source_dir}")

        # Cria o diretório de destino
        os.makedirs(target_path, exist_ok=True)
        
        print(f"Copiando arquivos de '{source_dir}' para '{target_path}'...")
        
        # Copia o conteúdo da pasta de origem para a de destino
        # dirs_exist_ok=True permite que a pasta de destino já exista
        shutil.copytree(source_dir, target_path, dirs_exist_ok=True)
        
        print("Cópia concluída.")
        
    except Exception as e:
        print(f"Ocorreu um erro ao processar {slug}: {e}")

def main():
    """Função principal para orquestrar os downloads."""
    print("Iniciando o processo de download dos datasets...")
    for key, info in DATASETS.items():
        download_and_copy(info["slug"], info["target_dir"])
    print("\nProcesso finalizado.")

if __name__ == "__main__":
    main()