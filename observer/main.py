from observer import CanalYouTube, Usuario


canal = CanalYouTube("Python Pro")

ana = Usuario("Ana")
carlos = Usuario("Carlos")

canal.suscribir(ana)
canal.suscribir(carlos)

canal.subir_video("Patrón Observer con Interfaces Formales")