class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, "-->", end=" ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Private method to sort the linked list using merge sort
    def _merge_sort(self, head):
        if head is None or head.next is None:
            return head

        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)

        sorted_list = self._sorted_merge(left, right)
        return sorted_list

    def _get_middle(self, head):
        if head is None:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _sorted_merge(self, a, b):
        if not a:
            return b
        if not b:
            return a

        if a.data <= b.data:
            result = a
            result.next = self._sorted_merge(a.next, b)
        else:
            result = b
            result.next = self._sorted_merge(a, b.next)
        return result

    def sort(self):
        # Start merge sort from the head of the linked list
        self.head = self._merge_sort(self.head)

    def merge_sorted_lists(self, list2):
        # Merges the current linked list with another sorted linked list
        self.head = self._sorted_merge(self.head, list2.head)

if __name__ == "__main__":
    # Create first linked list
    list1 = LinkedList()
    list1.insert_at_end(5)
    list1.insert_at_end(10)
    list1.insert_at_end(15)

    # Create second linked list
    list2 = LinkedList()
    list2.insert_at_end(2)
    list2.insert_at_end(3)
    list2.insert_at_end(20)

    # Print both lists
    print("List 1:")
    list1.print_list()
    print("List 2:")
    list2.print_list()

    list1.reverse()
    print("Reversed list:")
    list1.print_list()

    # Sort the reversed list
    list1.sort()
    print("Sorted merged list:")
    list1.print_list()


    # Merge the two lists and sort
    list1.merge_sorted_lists(list2)
    print("Merged sorted list:")
    list1.print_list()
