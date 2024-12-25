class Queue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x: int) -> None:
        # Push item onto in_stack
        self.in_stack.append(x)

    def dequeue(self) -> int:
        # If out_stack is empty, move all items from in_stack to out_stack
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        # Pop the top item from out_stack, which is the front of the queue
        return self.out_stack.pop()

# Example usage:
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
q.enqueue(3)
print(q.dequeue())  # Output: 2
