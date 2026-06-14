import heapq
import math


def dijkstra(grafo, origem):
    distancias = [math.inf] * grafo.numero_vertices
    pais = [None] * grafo.numero_vertices
    distancias[origem] = 0

    fila_prioridade = [(0, origem)]

    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

        if distancia_atual > distancias[vertice_atual]:
            continue

        for vizinho, peso in grafo.vizinhos(vertice_atual):
            nova_distancia = distancia_atual + peso

            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                pais[vizinho] = vertice_atual
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

    return distancias, pais


def reconstruir_caminho(pais, origem, destino):
    caminho = []
    atual = destino

    while atual is not None:
        caminho.append(atual)

        if atual == origem:
            caminho.reverse()
            return caminho

        atual = pais[atual]

    return []
