from memento import Conserje, Documento


documento = Documento("Borrador 1", "Texto introductorio del documento.")
historial = Conserje(documento)

historial.respaldar()
documento.editar("Borrador 2", "Se expande la sección de metodología.")

historial.respaldar()
documento.editar("Borrador Final", "Conclusiones definitivas listas para entrega.")

historial.mostrar_historial()

print("\n--- Deshaciendo cambios ---")
historial.deshacer()

print("\n--- Deshaciendo cambios otra vez ---")
historial.deshacer()