def delete_node(n):
    if n is None or n.next is None:
        return False
    next_node = n.next
    n.data = next_node.data
    n.next = next_node.next
    return True

