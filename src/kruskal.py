class UnionFind:
    def __init__(self, numero_vertices):
        self.pai = list(range(numero_vertices))
        self.rank = [0] * numero_vertices

    def find(self, vertice):
        if self.pai[vertice] != vertice:
            self.pai[vertice] = self.find(self.pai[vertice])
        return self.pai[vertice]

    def union(self, vertice_a, vertice_b):
        raiz_a = self.find(vertice_a)
        raiz_b = self.find(vertice_b)

        if raiz_a == raiz_b:
            return False

        if self.rank[raiz_a] < self.rank[raiz_b]:
            self.pai[raiz_a] = raiz_b
        elif self.rank[raiz_a] > self.rank[raiz_b]:
            self.pai[raiz_b] = raiz_a
        else:
            self.pai[raiz_b] = raiz_a
            self.rank[raiz_a] += 1

        return True


def kruskal(grafo):
    arestas_ordenadas = sorted(
        grafo.obter_arestas(),
        key=lambda aresta: (aresta[2], aresta[0], aresta[1]),
    )
    union_find = UnionFind(grafo.numero_vertices)
    arestas_selecionadas = []
    arestas_descartadas = []
    custo_total = 0

    for origem, destino, peso in arestas_ordenadas:
        if union_find.union(origem, destino):
            arestas_selecionadas.append((origem, destino, peso))
            custo_total += peso
        else:
            arestas_descartadas.append((origem, destino, peso))

    if len(arestas_selecionadas) != grafo.numero_vertices - 1:
        raise ValueError("O grafo nao e conectado; nao existe arvore geradora minima.")

    return arestas_ordenadas, arestas_selecionadas, arestas_descartadas, custo_total
