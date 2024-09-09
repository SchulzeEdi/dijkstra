import folium
from .cidades import rio_do_sul, lontras, presidente_getulio, trombudo_central, agrolandia, \
 ituporanga, ibirama, aurora, braco_trombudo, pouso_redondo, vidal_ramos, taio, salete, rio_do_campo, laurentino
from .dijkstra import dijkstra
from .grafo import construir_grafo

def gerar_mapa(cidade_inicio, cidade_final):
    mapa = folium.Map(location=rio_do_sul, zoom_start=10)
    folium.PolyLine([rio_do_sul, lontras], color="blue", weight=2.5, opacity=1).add_to(mapa)
    folium.PolyLine([rio_do_sul, presidente_getulio], color="blue", weight=2.5, opacity=1).add_to(mapa)
    folium.PolyLine([rio_do_sul, trombudo_central], color="blue", weight=2.5, opacity=1).add_to(mapa)
    folium.PolyLine([rio_do_sul, agrolandia], color="blue", weight=2.5, opacity=1).add_to(mapa)
    folium.PolyLine([rio_do_sul, ituporanga], color="blue", weight=2.5, opacity=1).add_to(mapa)
    folium.PolyLine([rio_do_sul, ibirama], color="blue", weight=2.5, opacity=1).add_to(mapa)
    folium.PolyLine([trombudo_central, aurora], color="blue", weight=2.5, opacity=1).add_to(mapa)
    folium.PolyLine([trombudo_central, braco_trombudo], color="blue", weight=2.5, opacity=1).add_to(mapa)
    folium.PolyLine([trombudo_central, agrolandia], color="blue", weight=2.5, opacity=1).add_to(mapa)
    folium.PolyLine([ituporanga, agrolandia], color="blue", weight=2.5, opacity=1).add_to(mapa)
    folium.PolyLine([ituporanga, presidente_getulio], color="blue", weight=2.5, opacity=1).add_to(mapa)
    folium.PolyLine([lontras, ibirama], color="blue", weight=2.5, opacity=1).add_to(mapa)
    folium.PolyLine([lontras, pouso_redondo], color="blue", weight=2.5, opacity=1).add_to(mapa)
    folium.PolyLine([pouso_redondo, vidal_ramos], color="blue", weight=2.5, opacity=1).add_to(mapa)
    folium.PolyLine([pouso_redondo, taio], color="blue", weight=2.5, opacity=1).add_to(mapa)
    folium.PolyLine([pouso_redondo, ibirama], color="blue", weight=2.5, opacity=1).add_to(mapa)
    folium.PolyLine([ibirama, presidente_getulio], color="blue", weight=2.5, opacity=1).add_to(mapa)
    folium.PolyLine([ibirama, taio], color="blue", weight=2.5, opacity=1).add_to(mapa)
    folium.PolyLine([taio, salete], color="blue", weight=2.5, opacity=1).add_to(mapa)
    folium.PolyLine([taio, rio_do_campo], color="blue", weight=2.5, opacity=1).add_to(mapa)
    folium.PolyLine([taio, laurentino], color="blue", weight=2.5, opacity=1).add_to(mapa)

    cidades = {
        'rio_do_sul': rio_do_sul,
        'lontras': lontras,
        'presidente_getulio': presidente_getulio,
        'trombudo_central' : trombudo_central, 
        'agrolandia' : agrolandia,
        'ituporanga' : ituporanga, 
        'ibirama': ibirama, 
        'aurora': aurora, 
        'braco_trombudo': braco_trombudo, 
        'pouso_redondo': pouso_redondo, 
        'vidal_ramos': vidal_ramos, 
        'taio': taio, 
        'salete': salete, 
        'rio_do_campo': rio_do_campo, 
        'laurentino' : laurentino        
    }

    for cidade, coordenadas in cidades.items():
        folium.Marker(coordenadas, popup=cidade.capitalize()).add_to(mapa)

    grafo = construir_grafo()
    caminho, custo_total = dijkstra(grafo, cidade_inicio, cidade_final)

    for i in range(len(caminho) - 1):
        cidade_atual = caminho[i]
        proxima_cidade = caminho[i + 1]
        folium.Marker(cidades[caminho[0]], popup='Inicio').add_to(mapa)
        folium.Marker(cidades[caminho[len(caminho)-1]], popup='Fim').add_to(mapa)
        folium.PolyLine([cidades[cidade_atual], cidades[proxima_cidade]], color="red", weight=5, opacity=0.8).add_to(mapa)

    mapa.save("maps/mapa.html")
    print(f"Custo total da viagem é: {custo_total}")
    return mapa._repr_html_()