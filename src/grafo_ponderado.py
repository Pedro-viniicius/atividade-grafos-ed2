class GrafoPonderado:
    """Grafo ponderado nao direcionado representado por lista de adjacencia."""

    def __init__(self, numero_vertices):
        if numero_vertices <= 0:
            raise ValueError("O numero de vertices deve ser positivo.")

        self.numero_vertices = numero_vertices
        self.lista_adjacencia = [[] for _ in range(numero_vertices)]

    def _validar_vertice(self, vertice):
        if vertice < 0 or vertice >= self.numero_vertices:
            raise ValueError(f"Vertice invalido: {vertice}")

    def adicionar_aresta(self, origem, destino, peso):
        self._validar_vertice(origem)
        self._validar_vertice(destino)

        if peso < 0:
            raise ValueError("Este grafo nao aceita pesos negativos.")

        self.lista_adjacencia[origem].append((destino, peso))
        self.lista_adjacencia[destino].append((origem, peso))

    def exibir_grafo(self):
        linhas = []
        for vertice, vizinhos in enumerate(self.lista_adjacencia):
            linhas.append(f"{vertice}: {vizinhos}")
        return "\n".join(linhas)

    def vizinhos(self, vertice):
        self._validar_vertice(vertice)
        return self.lista_adjacencia[vertice]

    def obter_arestas(self):
        arestas = []
        visitadas = set()

        for origem in range(self.numero_vertices):
            for destino, peso in self.lista_adjacencia[origem]:
                chave = tuple(sorted((origem, destino)))
                if chave not in visitadas:
                    visitadas.add(chave)
                    arestas.append((origem, destino, peso))

        return arestas
