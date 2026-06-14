from pathlib import Path

from dijkstra import dijkstra, reconstruir_caminho
from grafo_ponderado import GrafoPonderado
from kruskal import kruskal
from prim import prim


ARESTAS_OBRIGATORIAS = [
    (0, 1, 4),
    (0, 2, 2),
    (1, 2, 1),
    (1, 3, 5),
    (2, 3, 8),
    (2, 4, 10),
    (3, 4, 2),
    (3, 5, 6),
    (4, 5, 3),
    (4, 6, 7),
    (5, 6, 1),
    (5, 7, 9),
    (6, 7, 4),
    (6, 8, 6),
    (7, 8, 2),
]


def criar_grafo_obrigatorio():
    grafo = GrafoPonderado(9)

    for origem, destino, peso in ARESTAS_OBRIGATORIAS:
        grafo.adicionar_aresta(origem, destino, peso)

    return grafo


def formatar_caminho(caminho):
    if not caminho:
        return "nao existe caminho"
    return " -> ".join(str(vertice) for vertice in caminho)


def formatar_lista_arestas(arestas):
    return "\n".join(f"({origem}, {destino}, {peso})" for origem, destino, peso in arestas)


def normalizar_arestas(arestas):
    return {
        (min(origem, destino), max(origem, destino), peso)
        for origem, destino, peso in arestas
    }


def gerar_saida():
    grafo = criar_grafo_obrigatorio()
    linhas = []

    linhas.append("=== GRAFO ===")
    linhas.append(grafo.exibir_grafo())

    distancias_0, pais_0 = dijkstra(grafo, 0)
    caminho_0_5 = reconstruir_caminho(pais_0, 0, 5)
    caminho_0_8 = reconstruir_caminho(pais_0, 0, 8)

    linhas.append("")
    linhas.append("=== DIJKSTRA origem 0 ===")
    linhas.append(f"Distâncias: {distancias_0}")
    linhas.append(f"Pais: {pais_0}")
    linhas.append(f"Caminho 0 -> 5: {formatar_caminho(caminho_0_5)}")
    linhas.append(f"Custo: {distancias_0[5]}")
    linhas.append(f"Caminho 0 -> 8: {formatar_caminho(caminho_0_8)}")
    linhas.append(f"Custo: {distancias_0[8]}")

    distancias_3, pais_3 = dijkstra(grafo, 3)

    linhas.append("")
    linhas.append("=== DIJKSTRA origem 3 ===")
    linhas.append(f"Distâncias: {distancias_3}")
    linhas.append(f"Pais: {pais_3}")

    prim_0_arestas, prim_0_custo, prim_0_ordem = prim(grafo, 0)

    linhas.append("")
    linhas.append("=== PRIM origem 0 ===")
    linhas.append("Arestas selecionadas:")
    linhas.append(formatar_lista_arestas(prim_0_arestas))
    linhas.append(f"Ordem dos vértices: {prim_0_ordem}")
    linhas.append(f"Custo total: {prim_0_custo}")

    prim_3_arestas, prim_3_custo, prim_3_ordem = prim(grafo, 3)

    linhas.append("")
    linhas.append("=== PRIM origem 3 ===")
    linhas.append("Arestas selecionadas:")
    linhas.append(formatar_lista_arestas(prim_3_arestas))
    linhas.append(f"Ordem dos vértices: {prim_3_ordem}")
    linhas.append(f"Custo total: {prim_3_custo}")

    (
        kruskal_ordenadas,
        kruskal_selecionadas,
        kruskal_descartadas,
        kruskal_custo,
    ) = kruskal(grafo)

    linhas.append("")
    linhas.append("=== KRUSKAL ===")
    linhas.append("Arestas ordenadas por peso:")
    linhas.append(formatar_lista_arestas(kruskal_ordenadas))
    linhas.append("Arestas selecionadas:")
    linhas.append(formatar_lista_arestas(kruskal_selecionadas))
    linhas.append("Arestas descartadas por ciclo:")
    linhas.append(formatar_lista_arestas(kruskal_descartadas))
    linhas.append(f"Custo total: {kruskal_custo}")

    prim_0_igual_kruskal = normalizar_arestas(prim_0_arestas) == normalizar_arestas(
        kruskal_selecionadas
    )
    prim_3_igual_kruskal = normalizar_arestas(prim_3_arestas) == normalizar_arestas(
        kruskal_selecionadas
    )
    custos_iguais = prim_0_custo == prim_3_custo == kruskal_custo

    linhas.append("")
    linhas.append("=== COMPARAÇÃO ===")
    linhas.append(f"Custo Prim origem 0: {prim_0_custo}")
    linhas.append(f"Custo Prim origem 3: {prim_3_custo}")
    linhas.append(f"Custo Kruskal: {kruskal_custo}")
    linhas.append(
        "As arestas de Prim origem 0 e Kruskal são iguais? "
        f"{'Sim' if prim_0_igual_kruskal else 'Não'}"
    )
    linhas.append(
        "As arestas de Prim origem 3 e Kruskal são iguais? "
        f"{'Sim' if prim_3_igual_kruskal else 'Não'}"
    )
    linhas.append(f"Os custos são iguais? {'Sim' if custos_iguais else 'Não'}")

    return "\n".join(linhas) + "\n"


def salvar_saida(conteudo):
    raiz_projeto = Path(__file__).resolve().parents[1]
    caminho_saida = raiz_projeto / "outputs" / "saida_execucao.txt"
    caminho_saida.parent.mkdir(parents=True, exist_ok=True)
    caminho_saida.write_text(conteudo, encoding="utf-8")
    return caminho_saida


def main():
    conteudo = gerar_saida()
    caminho_saida = salvar_saida(conteudo)
    print(conteudo)
    print(f"Saída salva em: {caminho_saida}")


if __name__ == "__main__":
    main()
