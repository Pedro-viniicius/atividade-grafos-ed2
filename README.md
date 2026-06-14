# Atividade Grafos

Projeto acadêmico de Estruturas de Dados II sobre grafos ponderados, caminhos mínimos e árvores geradoras mínimas.

## Descrição

O projeto implementa, em Python, um grafo ponderado não direcionado usando lista de adjacência. Sobre esse grafo são executados:

- Dijkstra para caminhos mínimos.
- Prim para árvore geradora mínima.
- Kruskal para árvore geradora mínima com Union-Find.

Não são usadas bibliotecas prontas de grafos, como NetworkX. O projeto usa apenas recursos da biblioteca padrão do Python.

## Estrutura de Pastas

```text
atividade_grafos/
├── src/
│   ├── grafo_ponderado.py
│   ├── dijkstra.py
│   ├── prim.py
│   ├── kruskal.py
│   └── main.py
├── outputs/
│   └── saida_execucao.txt
├── README.md
└── RELATORIO.md
```

## Linguagem Utilizada

Python 3.

## Como Executar

A partir da pasta `atividade_grafos`, execute:

```bash
python src/main.py
```

Caso o comando `python` não esteja disponível no ambiente, use:

```bash
python3 src/main.py
```

## Arquivo de Saída

A execução imprime os resultados no terminal e também salva toda a saída em:

```text
outputs/saida_execucao.txt
```
