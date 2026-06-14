# Relatório — Atividade 01: Grafos, Rotas e Redes de Menor Custo

## 1. Introdução

Este trabalho implementa e analisa algoritmos clássicos sobre grafos ponderados não direcionados. O objetivo é representar um grafo por lista de adjacência, calcular caminhos mínimos com Dijkstra e encontrar árvores geradoras mínimas com Prim e Kruskal.

Os algoritmos foram implementados manualmente em Python, sem uso de bibliotecas prontas de grafos. A execução foi feita sobre o mesmo grafo obrigatório, com vértices de 0 a 8 e 15 arestas ponderadas.

## 2. Representação do Grafo

O grafo foi representado por uma lista de adjacência. Cada posição da lista corresponde a um vértice e armazena pares no formato `(vizinho, peso)`.

Exemplo:

```text
0: [(1, 4), (2, 2)]
1: [(0, 4), (2, 1), (3, 5)]
```

Como o grafo é não direcionado, cada aresta `(u, v, peso)` é adicionada duas vezes: uma em `u`, apontando para `v`, e outra em `v`, apontando para `u`.

A lista de adjacência é adequada porque o grafo não é completo. Com 9 vértices, uma matriz de adjacência teria 81 posições, muitas delas vazias. A lista armazena apenas as conexões existentes, economizando espaço e facilitando a iteração pelos vizinhos reais de cada vértice, o que é útil em Dijkstra e Prim.

## 3. Algoritmo de Dijkstra

Dijkstra calcula o menor custo entre uma origem e todos os outros vértices, desde que os pesos das arestas não sejam negativos.

O algoritmo mantém:

- Uma lista de distâncias mínimas conhecidas.
- Uma lista de pais, usada para reconstruir caminhos.
- Uma fila de prioridade, implementada com `heapq`, para sempre processar o vértice com menor distância parcial.

Durante a execução, o algoritmo relaxa as arestas dos vértices processados. Relaxar uma aresta significa verificar se passar por uma aresta melhora a distância conhecida até um vértice vizinho. Se melhorar, a distância e o pai desse vizinho são atualizados.

## 4. Resultados de Dijkstra

### Origem 0

Distâncias mínimas:

```text
[0, 3, 2, 8, 10, 13, 14, 18, 20]
```

Vetor de pais:

```text
[None, 2, 0, 1, 3, 4, 5, 6, 6]
```

Caminho mínimo de 0 até 5:

```text
0 -> 2 -> 1 -> 3 -> 4 -> 5
```

Custo total: `13`.

Caminho mínimo de 0 até 8:

```text
0 -> 2 -> 1 -> 3 -> 4 -> 5 -> 6 -> 8
```

Custo total: `20`.

### Origem 3

Distâncias mínimas:

```text
[8, 5, 6, 0, 2, 5, 6, 10, 12]
```

Vetor de pais:

```text
[2, 3, 1, None, 3, 4, 5, 6, 6]
```

## 5. Respostas da análise sobre Dijkstra

**1. Por que BFS não seria suficiente para resolver esse problema?**

BFS encontra caminhos com o menor número de arestas em grafos não ponderados, ou em grafos onde todas as arestas têm o mesmo custo. Neste problema, as arestas têm pesos diferentes. Portanto, um caminho com menos arestas pode ter custo maior que outro caminho com mais arestas.

**2. O que significa relaxar uma aresta?**

Relaxar uma aresta significa testar se a distância até um vizinho pode ser reduzida passando pelo vértice atual. Se `distancia[atual] + peso` for menor que `distancia[vizinho]`, a distância do vizinho é atualizada e o vértice atual passa a ser seu pai.

**3. Qual a diferença entre encontrar o caminho com menos arestas e o caminho de menor custo?**

O caminho com menos arestas minimiza a quantidade de conexões percorridas. O caminho de menor custo minimiza a soma dos pesos das arestas. Em grafos ponderados, esses dois caminhos podem ser diferentes.

**4. O algoritmo de Dijkstra funcionaria se houvesse pesos negativos? Justifique.**

Não. Dijkstra assume que, depois que um vértice é processado com a menor distância conhecida, essa distância não será reduzida depois. Arestas com peso negativo quebram essa propriedade, pois podem criar uma melhoria posterior em um vértice já processado.

## 6. Algoritmo de Prim

Prim constrói uma árvore geradora mínima começando por um vértice inicial. A cada passo, escolhe a menor aresta que conecta algum vértice já pertencente à árvore a um vértice ainda não visitado.

A implementação usa uma fila de prioridade com `heapq`. As arestas candidatas são armazenadas por peso, e a menor delas é escolhida primeiro. O algoritmo termina quando a árvore possui `V - 1` arestas. Como o grafo tem 9 vértices, a árvore geradora mínima deve possuir 8 arestas.

## 7. Resultados de Prim

### Origem 0

Arestas selecionadas:

```text
(0, 2, 2)
(2, 1, 1)
(1, 3, 5)
(3, 4, 2)
(4, 5, 3)
(5, 6, 1)
(6, 7, 4)
(7, 8, 2)
```

Ordem dos vértices:

```text
[0, 2, 1, 3, 4, 5, 6, 7, 8]
```

Custo total: `20`.

### Origem 3

Arestas selecionadas:

```text
(3, 4, 2)
(4, 5, 3)
(5, 6, 1)
(6, 7, 4)
(7, 8, 2)
(3, 1, 5)
(1, 2, 1)
(2, 0, 2)
```

Ordem dos vértices:

```text
[3, 4, 5, 6, 7, 8, 1, 2, 0]
```

Custo total: `20`.

## 8. Respostas da análise sobre Prim

**1. Qual é a diferença entre o objetivo de Prim e o objetivo de Dijkstra?**

Dijkstra busca caminhos mínimos a partir de uma origem até os demais vértices. Prim busca uma árvore geradora mínima que conecte todos os vértices com o menor custo total possível. Dijkstra resolve um problema de rotas; Prim resolve um problema de conexão global de menor custo.

**2. Por que a árvore geradora mínima não pode conter ciclos?**

Uma árvore, por definição, é conectada e acíclica. Se houvesse ciclo, seria possível remover uma aresta desse ciclo e manter os vértices conectados, reduzindo ou mantendo a quantidade de arestas. Assim, um ciclo indicaria que a estrutura não é uma árvore geradora mínima válida.

**3. O resultado de Prim depende do vértice inicial? Explique.**

A ordem de inclusão dos vértices pode depender do vértice inicial. O conjunto de arestas também pode variar quando existem múltiplas árvores geradoras mínimas com mesmo custo. Entretanto, o custo total da árvore geradora mínima deve ser o mesmo. Neste grafo, as execuções com origem 0 e origem 3 produziram o mesmo custo total, `20`, e o mesmo conjunto de arestas quando as direções são desconsideradas.

## 9. Algoritmo de Kruskal

Kruskal constrói uma árvore geradora mínima ordenando todas as arestas do grafo por peso crescente. Em seguida, percorre essa lista e seleciona uma aresta se ela conectar dois componentes diferentes.

Para detectar ciclos, foi usada a estrutura Union-Find, com compressão de caminho e união por rank. Se os dois vértices de uma aresta já pertencem ao mesmo conjunto, adicionar essa aresta formaria um ciclo, então ela é descartada.

## 10. Resultados de Kruskal

Arestas ordenadas por peso:

```text
(1, 2, 1)
(5, 6, 1)
(0, 2, 2)
(3, 4, 2)
(7, 8, 2)
(4, 5, 3)
(0, 1, 4)
(6, 7, 4)
(1, 3, 5)
(3, 5, 6)
(6, 8, 6)
(4, 6, 7)
(2, 3, 8)
(5, 7, 9)
(2, 4, 10)
```

Arestas selecionadas:

```text
(1, 2, 1)
(5, 6, 1)
(0, 2, 2)
(3, 4, 2)
(7, 8, 2)
(4, 5, 3)
(6, 7, 4)
(1, 3, 5)
```

Arestas descartadas por formarem ciclo:

```text
(0, 1, 4)
(3, 5, 6)
(6, 8, 6)
(4, 6, 7)
(2, 3, 8)
(5, 7, 9)
(2, 4, 10)
```

Custo total: `20`.

## 11. Respostas da análise sobre Kruskal

**1. Como Kruskal detecta se uma aresta formaria ciclo?**

Kruskal usa Union-Find. Antes de adicionar uma aresta `(u, v)`, verifica se `u` e `v` pertencem ao mesmo conjunto. Se pertencem, já existe um caminho entre eles, então a nova aresta formaria ciclo e deve ser descartada.

**2. Por que ordenar as arestas é uma etapa essencial?**

A ordenação garante que as arestas sejam avaliadas do menor para o maior peso. Isso permite que Kruskal escolha localmente as conexões mais baratas sem formar ciclos, construindo uma árvore geradora mínima.

**3. Prim e Kruskal devem produzir sempre o mesmo custo total? Justifique.**

Sim, quando aplicados ao mesmo grafo conectado e ponderado, ambos devem produzir uma árvore geradora mínima com o mesmo custo total. As arestas escolhidas podem diferir se houver mais de uma árvore geradora mínima possível, mas o custo mínimo total deve ser igual.

## 12. Comparação entre Dijkstra, Prim e Kruskal

Dijkstra calcula caminhos mínimos a partir de uma origem. Seu resultado principal é a menor distância de uma origem até cada vértice e os predecessores usados para reconstruir caminhos específicos.

Prim e Kruskal calculam árvores geradoras mínimas. Eles não buscam o menor caminho entre dois vértices, mas sim uma forma de conectar todos os vértices com custo total mínimo.

Neste trabalho:

- Dijkstra a partir de 0 encontrou custo `13` de 0 até 5 e custo `20` de 0 até 8.
- Prim a partir de 0 encontrou uma árvore geradora mínima de custo `20`.
- Prim a partir de 3 também encontrou uma árvore geradora mínima de custo `20`.
- Kruskal encontrou uma árvore geradora mínima de custo `20`.

## 13. Comparação entre Prim e Kruskal

Prim origem 0, Prim origem 3 e Kruskal encontraram custo total `20`.

As arestas de Prim e Kruskal foram iguais quando comparadas sem considerar a direção das arestas:

```text
(0, 2, 2)
(1, 2, 1)
(1, 3, 5)
(3, 4, 2)
(4, 5, 3)
(5, 6, 1)
(6, 7, 4)
(7, 8, 2)
```

Portanto, neste grafo específico, além do custo total ser igual, o conjunto de arestas da árvore geradora mínima também foi o mesmo. Em outros grafos, os algoritmos podem produzir conjuntos de arestas diferentes, desde que todos tenham o custo mínimo total.

## 14. Conclusão

O projeto implementou corretamente a representação do grafo ponderado não direcionado por lista de adjacência e executou os algoritmos Dijkstra, Prim e Kruskal.

Dijkstra foi usado para calcular caminhos mínimos a partir dos vértices 0 e 3. Prim foi executado a partir dos vértices 0 e 3, gerando árvores com 8 arestas e custo total `20`. Kruskal também gerou uma árvore com 8 arestas e custo total `20`, confirmando a consistência entre os algoritmos de árvore geradora mínima.

A principal diferença observada é que Dijkstra resolve problemas de menor caminho a partir de uma origem, enquanto Prim e Kruskal resolvem o problema de conectar todos os vértices com o menor custo total possível.
