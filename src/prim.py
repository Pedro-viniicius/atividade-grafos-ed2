import heapq


def prim(grafo, origem):
    visitados = [False] * grafo.numero_vertices
    arestas_escolhidas = []
    ordem_vertices = [origem]
    custo_total = 0
    fila_prioridade = []

    visitados[origem] = True

    for destino, peso in grafo.vizinhos(origem):
        heapq.heappush(fila_prioridade, (peso, origem, destino))

    while fila_prioridade and len(arestas_escolhidas) < grafo.numero_vertices - 1:
        peso, origem_aresta, destino_aresta = heapq.heappop(fila_prioridade)

        if visitados[destino_aresta]:
            continue

        visitados[destino_aresta] = True
        arestas_escolhidas.append((origem_aresta, destino_aresta, peso))
        ordem_vertices.append(destino_aresta)
        custo_total += peso

        for proximo_destino, proximo_peso in grafo.vizinhos(destino_aresta):
            if not visitados[proximo_destino]:
                heapq.heappush(
                    fila_prioridade,
                    (proximo_peso, destino_aresta, proximo_destino),
                )

    if len(arestas_escolhidas) != grafo.numero_vertices - 1:
        raise ValueError("O grafo nao e conectado; nao existe arvore geradora minima.")

    return arestas_escolhidas, custo_total, ordem_vertices
