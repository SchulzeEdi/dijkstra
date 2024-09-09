import heapq

def dijkstra(grafo, inicio, fim):
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0, inicio))
    distancias = {no: float('inf') for no in grafo}
    distancias[inicio] = 0
    caminho = {no: None for no in grafo}

    while fila_prioridade:
        distancia_atual, no_atual = heapq.heappop(fila_prioridade)

        if distancia_atual > distancias[no_atual]:
            continue
        
        for vizinho, peso in grafo[no_atual]:
            distancia = distancia_atual + peso

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                caminho[vizinho] = no_atual
                heapq.heappush(fila_prioridade, (distancia, vizinho))

    caminho_final = []
    no = fim
    while no is not None:
        caminho_final.append(no)
        no = caminho[no]
    caminho_final.reverse()

    return caminho_final, distancias[fim]
