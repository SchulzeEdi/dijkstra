from geopy.distance import geodesic

rio_do_sul = [-27.219619, -49.648187]
lontras = [-27.163455, -49.554623]
presidente_getulio = [-27.044183, -49.622974]
trombudo_central = [-27.305115, -49.794268]
agrolandia = [-27.409043, -49.829361]
ituporanga = [-27.424301, -49.598461]
ibirama = [-27.060623, -49.524269]
aurora = [-27.315374, -49.635623]
braco_trombudo = [-27.361527, -49.889323]
pouso_redondo = [-27.258321, -49.930338]
vidal_ramos = [-27.391415, -49.365111]
taio = [-27.115944, -49.997965]
salete = [-26.981344, -50.006329]
rio_do_campo = [-26.947577, -50.141180]
laurentino = [-27.222370, -49.736678]

distancias = {
    'rds_lon': geodesic(rio_do_sul, lontras).kilometers,
    'rds_pg': geodesic(rio_do_sul, presidente_getulio).kilometers,
    'rds_lon' : geodesic(rio_do_sul, lontras).kilometers,
    'rds_pg' : geodesic(rio_do_sul, presidente_getulio).kilometers,
    'rds_tc' : geodesic(rio_do_sul, trombudo_central).kilometers,
    'rds_agr' : geodesic(rio_do_sul, agrolandia).kilometers,
    'rds_itu' : geodesic(rio_do_sul, ituporanga).kilometers,
    'rds_ibi' : geodesic(rio_do_sul, ibirama).kilometers,
    'tc_aur' : geodesic(trombudo_central, aurora).kilometers,
    'tc_bt' : geodesic(trombudo_central, braco_trombudo).kilometers,
    'tc_agr' : geodesic(trombudo_central, agrolandia).kilometers,
    'agr_itu' : geodesic(ituporanga, agrolandia).kilometers,
    'itu_pg' : geodesic(ituporanga, presidente_getulio).kilometers,
    'lon_ibi' : geodesic(lontras, ibirama).kilometers,
    'lon_pr' : geodesic(lontras, pouso_redondo).kilometers,
    'pr_vr' : geodesic(pouso_redondo, vidal_ramos).kilometers,
    'pr_ta' : geodesic(pouso_redondo, taio).kilometers,
    'pr_ibi' : geodesic(pouso_redondo, ibirama).kilometers,
    'ibi_pg' : geodesic(ibirama, presidente_getulio).kilometers,
    'ibi_ta' : geodesic(ibirama, taio).kilometers,
    'ta_sal' : geodesic(taio, salete).kilometers,
    'ta_rdc' : geodesic(taio, rio_do_campo).kilometers,
    'ta_lau' : geodesic(taio, laurentino).kilometers
}

pavimentacao = [1, 1.5, 2.2]
trafego = [1, 2, 3]
