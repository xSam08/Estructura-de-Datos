from sll import singleLinkedList

inst_sll = singleLinkedList()

inst_sll.add_node_end('1')
inst_sll.add_node_end('2')
inst_sll.add_node_end('3')
inst_sll.add_node_end('4')

inst_sll.add_initial_node('0')
inst_sll.add_initial_node('-1')
inst_sll.add_initial_node('-2')
inst_sll.add_initial_node('-3')


inst_sll.remove_last_node()


inst_sll.show_list()

