from .cidades import distancias

def construir_grafo():
    grafo = {
        'rio_do_sul': [
            ('lontras', distancias['rds_lon']),
            ('presidente_getulio', distancias['rds_pg']),
            ('trombudo_central', distancias['rds_tc']),
            ('agrolandia', distancias['rds_agr']),
            ('ituporanga', distancias['rds_itu']),
            ('ibirama', distancias['rds_ibi']),
        ],
        'lontras': [
            ('rio_do_sul', distancias['rds_lon']),
            ('ibirama', distancias['lon_ibi']),
            ('pouso_redondo', distancias['lon_pr']),
        ],
        'ibirama': [
            ('presidente_getulio', distancias['ibi_pg']),
            ('taio', distancias['ibi_ta']),
            ('pouso_redondo', distancias['pr_ibi']),
            ('lontras', distancias['lon_ibi']),
            ('rio_do_sul', distancias['rds_ibi']),
        ],
        'presidente_getulio': [
            ('ibirama', distancias['ibi_pg']),
            ('rio_do_sul', distancias['rds_pg']),
            ('ituporanga', distancias['itu_pg']),
        ],
        'trombudo_central' : [
            ('rio_do_sul', distancias['rds_tc']),
            ('braco_trombudo', distancias['tc_bt']),
            ('aurora', distancias['tc_aur']),
            ('agrolandia', distancias['tc_agr']),
        ],
        'agrolandia' : [
            ('trombudo_central', distancias['tc_agr']),
            ('ituporanga', distancias['agr_itu']),
            ('rio_do_sul', distancias['rds_agr']),
        ],
        'ituporanga' : [
            ('agrolandia', distancias['agr_itu']),
            ('presidente_getulio', distancias['itu_pg']),
            ('rio_do_sul', distancias['rds_itu']),
        ],
        'aurora' : [
            ('trombudo_central', distancias['tc_aur']),
        ],
        'braco_trombudo' : [
            ('trombudo_central', distancias['tc_bt'])
        ],
        'pouso_redondo' : [
            ('lontras', distancias['lon_pr']),
            ('vidal_ramos', distancias['pr_vr']),
            ('taio', distancias['pr_ta']),
            ('ibirama', distancias['pr_ibi']),
        ],
        'vidal_ramos' : [
            ('pouso_redondo', distancias['pr_vr'])
        ],
        'taio' : [
            ('pouso_redondo', distancias['pr_ta']),
            ('ibirama', distancias['ibi_ta']),
            ('salete', distancias['ta_sal']),
            ('rio_do_campo', distancias['ta_rdc']),
            ('laurentino', distancias['ta_lau']),
        ],
        'salete' : [
            ('taio', distancias['ta_sal']),
        ],
        'rio_do_campo' : [
            ('taio', distancias['ta_rdc'])
        ],
        'laurentino' : [
            ('taio', distancias['ta_lau'])
        ]
    }  
    return grafo
