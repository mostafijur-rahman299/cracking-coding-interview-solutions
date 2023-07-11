def intersect_linked_lists(head1, head2):
  # Initialize two pointers, one for each linked list.
  p1 = head1
  p2 = head2

  # While the two pointers are not equal, move them forward one node at a time.
  while p1 != p2:
    if p1 is None:
      return None
    p1 = p1.next
    if p2 is None:
      return None
    p2 = p2.next

  # The two pointers have now met, so they must be pointing to the intersection node.
  return p1
