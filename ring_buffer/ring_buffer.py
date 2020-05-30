class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

class MockDLL:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1

        # handle if there is a tail
        if self.tail:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        # handle if there is no tail
        else:
            self.head = new_node

        self.tail = new_node


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = MockDLL()
        self.oldest = None

    def append(self, item):
        # If at max capacity
        if len(self.buffer) == self.capacity:
            # Check if oldest is the tail
            if self.oldest == self.buffer.tail:
            # Overwrite the value
                self.oldest.value = item
                # Set the oldest to the head
                self.oldest = self.buffer.head
            # Otherwise 
            else:
                # Overwrite the oldest value
                self.oldest.value = item
                # Set the oldest to the next node
                self.oldest = self.oldest.next
        else:
            # Add to tail if not at max capacity
            self.buffer.add_to_tail(item)
            # Set the oldest 
            if self.oldest == None:
                # First append case
                self.oldest = self.buffer.tail

    def get(self):
        buffer_list = []

        current = self.buffer.head
        
        while current is not None:
            buffer_list.append(current.value)
            current = current.next

        return buffer_list



