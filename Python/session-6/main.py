from sll import sll

inst_sll = sll()

inst_sll.create_nodo(5)

print(inst_sll.validar(-10))
print(inst_sll.validar(11))
print(inst_sll.validar(12))

inst_sll.punto_uno(12)
inst_sll.punto_uno(12)
inst_sll.punto_uno(12)
inst_sll.punto_uno(36)
inst_sll.punto_uno(36)
inst_sll.punto_uno(36)
inst_sll.punto_uno(-10)
inst_sll.punto_uno(-11)

inst_sll.punto_dos(-3)
inst_sll.punto_dos(-5)

print("Lista:")
inst_sll.imprimir_lista()

""" inst_sll.eliminar_nodos_repetidos()
print("Nueva lista:")
inst_sll.imprimir_lista() """

inst_sll.eliminar_nodos_pares()
print("Nueva lista:")
inst_sll.imprimir_lista()