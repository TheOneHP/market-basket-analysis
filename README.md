
# Análise de Cesta de Compras em Múltiplos Datasets

## Sumário Executivo

Este projeto realiza uma Análise de Cesta de Compras (*Market Basket Analysis*) para identificar padrões de consumo e regras de associação em diferentes tipos de datasets de varejo. O objetivo é duplo:

1.  Extrair insights acionáveis sobre quais produtos são frequentemente comprados juntos.
2.  Demonstrar um fluxo de trabalho de engenharia e ciência de dados robusto, capaz de lidar com datasets em diferentes estados de qualidade: um "sujo" (que exige limpeza extensiva), um "limpo" (bem estruturado) e um "desorganizado" (mal formatado).
## Resultados e Recomendações

A análise revela padrões de compra que podem ser usados para otimizar estratégias de marketing e layout de loja. Abaixo, um exemplo das regras encontradas no primeiro dataset:

```
                                                            antecedents                                                         consequents  ...  zhangs_metric
158  (ROSES REGENCY TEACUP AND SAUCER, GREEN REGENCY TEACUP AND SAUCER)                                    (PINK REGENCY TEACUP AND SAUCER)  ...       0.983493
161                                    (PINK REGENCY TEACUP AND SAUCER)  (ROSES REGENCY TEACUP AND SAUCER, GREEN REGENCY TEACUP AND SAUCER)  ...       0.983752
157   (ROSES REGENCY TEACUP AND SAUCER, PINK REGENCY TEACUP AND SAUCER)                                   (GREEN REGENCY TEACUP AND SAUCER)  ...       0.973435
162                                   (GREEN REGENCY TEACUP AND SAUCER)   (ROSES REGENCY TEACUP AND SAUCER, PINK REGENCY TEACUP AND SAUCER)  ...       0.994450
26                                     (PINK REGENCY TEACUP AND SAUCER)                                   (GREEN REGENCY TEACUP AND SAUCER)  ...       0.976308
```
O projeto utiliza a biblioteca `mlxtend` para aplicar o algoritmo Apriori e gerar as regras de associação.

## Tecnologias Utilizadas

*   **Linguagem de Programação:** Python 3.10
*   **Bibliotecas Python:**
    *   `pandas`: Para manipulação, limpeza e estruturação dos dados.
    *   `mlxtend`: Para a implementação do algoritmo Apriori e geração das regras de associação.
    *   `kagglehub`: Para download programático dos datasets via API do Kaggle.

## Estrutura do Projeto

O projeto é modularizado para garantir clareza e manutenibilidade:

*   `main.py`: Script orquestrador ## Resultados e Recomendações

A análise revela padrões de compra que podem ser usados para otimizar estratégias de marketing e layout de loja. Abaixo, um exemplo das regras encontradas no primeiro dataset:

```
                                                            antecedents                                                         consequents  ...  zhangs_metric
158  (ROSES REGENCY TEACUP AND SAUCER, GREEN REGENCY TEACUP AND SAUCER)                                    (PINK REGENCY TEACUP AND SAUCER)  ...       0.983493
161                                    (PINK REGENCY TEACUP AND SAUCER)  (ROSES REGENCY TEACUP AND SAUCER, GREEN REGENCY TEACUP AND SAUCER)  ...       0.983752
157   (ROSES REGENCY TEACUP AND SAUCER, PINK REGENCY TEACUP AND SAUCER)                                   (GREEN REGENCY TEACUP AND SAUCER)  ...       0.973435
162                                   (GREEN REGENCY TEACUP AND SAUCER)   (ROSES REGENCY TEACUP AND SAUCER, PINK REGENCY TEACUP AND SAUCER)  ...       0.994450
26                                     (PINK REGENCY TEACUP AND SAUCER)                                   (GREEN REGENCY TEACUP AND SAUCER)  ...       0.976308
```que executa toda a pipeline de análise em um único comando.
*   `download_datasets.py`: Módulo responsável por baixar os dados brutos do Kaggle.
*   `data_preparation.py`: Prepara e limpa o dataset "sujo" de varejo online.
*   `market_basket_analysis.py`: Executa a análise no dataset de varejo online.
*   `data_preparation_groceries.py`: Prepara o dataset "limpo" (`Groceries data.csv`).
*   `market_basket_analysis_groceries.py`: Executa a análise no dataset `Groceries`.
*   `data_preparation_basket.py`: Processa e estrutura o dataset "desorganizado" (`basket.csv`).
*   `market_basket_analysis_basket.py`: Executa a análise no dataset `basket`.
*   `*.pkl`: Arquivos binários contendo as listas de transações processadas, prontos para a análise.

## Processo de Análise

1.  **Obtenção de Dados:** Os datasets são baixados do Kaggle para garantir a reprodutibilidade.
2.  **Engenharia de Dados:** Cada um dos três datasets passa por um processo de ETL customizado para seu estado inicial, gerando uma lista de transações padronizada.
3.  **Modelagem:** O algoritmo Apriori é aplicado sobre cada lista de transações para identificar os conjuntos de itens mais frequentes (`frequent itemsets`).
4.  **Geração de Regras:** Com base nos itemsets frequentes, são geradas as regras de associação, que são então filtradas por métricas de confiança (`confidence`) e suporte (`lift`).

## Como Reproduzir a Análise

Para executar a pipeline completa, siga os passos abaixo:

1.  **Clone o repositório (exemplo):**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd market_basket_analysis
    ```
2.  **Instale as dependências:**
    ```bash
    pip install pandas mlxtend kagglehub
    ```
3.  **Configure a API do Kaggle:**
    Para que o download funcione, você precisa ter suas credenciais do Kaggle configuradas, o que geralmente envolve ter um arquivo `kaggle.json` no diretório `~/.kaggle/`.
4.  **Execute o script principal:**
    Rode o script `main.py` para executar todo o processo, desde o download até a análise final de todos os datasets.
    ```bash
    python main.py
    ```
    O progresso e os resultados de cada etapa serão exibidos no terminal.

## Resultados e Recomendações

A análise revela padrões de compra que podem ser usados para otimizar estratégias de marketing e layout de loja. Abaixo, um exemplo das regras encontradas no primeiro dataset:

```
                                                            antecedents                                                         consequents  ...  zhangs_metric
158  (ROSES REGENCY TEACUP AND SAUCER, GREEN REGENCY TEACUP AND SAUCER)                                    (PINK REGENCY TEACUP AND SAUCER)  ...       0.983493
161                                    (PINK REGENCY TEACUP AND SAUCER)  (ROSES REGENCY TEACUP AND SAUCER, GREEN REGENCY TEACUP AND SAUCER)  ...       0.983752
157   (ROSES REGENCY TEACUP AND SAUCER, PINK REGENCY TEACUP AND SAUCER)                                   (GREEN REGENCY TEACUP AND SAUCER)  ...       0.973435
162                                   (GREEN REGENCY TEACUP AND SAUCER)   (ROSES REGENCY TEACUP AND SAUCER, PINK REGENCY TEACUP AND SAUCER)  ...       0.994450
26                                     (PINK REGENCY TEACUP AND SAUCER)                                   (GREEN REGENCY TEACUP AND SAUCER)  ...       0.976308
```

### Recomendações de Negócio

*   **Cross-selling:** Itens com alto `lift` e `confidence` devem ser alvos de campanhas de cross-selling. Por exemplo, se a análise mostra que "pão" e "manteiga" são frequentemente comprados juntos, um desconto em um item pode ser oferecido na compra do outro.
*   **Layout da Loja:** Produtos que aparecem juntos nas regras de associação podem ser posicionados próximos nas gôndolas para incentivar a compra conjunta e melhorar a experiência do cliente.## Resultados e Recomendações

A análise revela padrões de compra que podem ser usados para otimizar estratégias de marketing e layout de loja. Abaixo, um exemplo das regras encontradas no primeiro dataset:

```
                                                            antecedents                                                         consequents  ...  zhangs_metric
158  (ROSES REGENCY TEACUP AND SAUCER, GREEN REGENCY TEACUP AND SAUCER)                                    (PINK REGENCY TEACUP AND SAUCER)  ...       0.983493
161                                    (PINK REGENCY TEACUP AND SAUCER)  (ROSES REGENCY TEACUP AND SAUCER, GREEN REGENCY TEACUP AND SAUCER)  ...       0.983752
157   (ROSES REGENCY TEACUP AND SAUCER, PINK REGENCY TEACUP AND SAUCER)                                   (GREEN REGENCY TEACUP AND SAUCER)  ...       0.973435
162                                   (GREEN REGENCY TEACUP AND SAUCER)   (ROSES REGENCY TEACUP AND SAUCER, PINK REGENCY TEACUP AND SAUCER)  ...       0.994450
26                                     (PINK REGENCY TEACUP AND SAUCER)                                   (GREEN REGENCY TEACUP AND SAUCER)  ...       0.976308
```
*   **Gestão de Estoque:** A popularidade de certos conjuntos de itens (itemsets) pode informar decisões de gestão de estoque, garantindo que produtos frequentemente comprados em conjunto estejam sempre disponíveis.
