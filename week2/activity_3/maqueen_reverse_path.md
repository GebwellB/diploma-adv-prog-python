**MicroPython Doubly Linked List Activity Worksheet: Reverse Navigation with Maqueen**

---

**Objective:** Use a doubly linked list to program your Maqueen robot to follow a path, then automatically reverse the steps to return to the starting point.

---

**Scenario:** Your Maqueen robot starts at the classroom door. It must:

1. Drive forward across the classroom
2. Turn right into a corridor
3. Turn left into another hallway
4. Drive forward to the end of the corridor
5. Stop

Then it must reverse its path to return to where it started.

---

**Task 1: Write Forward Path** Use the doubly linked list to store the path commands in order.

```python
# path.append("your_command_here")
path.append("forward")   # move across classroom
path.append("right")     # turn into corridor
path.append("left")      # turn into hallway
path.append("forward")   # down the hallway
path.append("stop")      # final stop
```

---

**Task 2: Execute the Forward Path** Traverse from `head` to `tail`, running robot actions for each node.

```python
node = path.head
while node:
    cmd = node.value
    # TODO: translate cmd into Maqueen motor action
    node = node.next
```

---

**Task 3: Execute the Reverse Path** Traverse the linked list in reverse using `.prev`, performing the opposite action.

```python
node = path.tail
while node:
    cmd = node.value
    # TODO: translate cmd into opposite Maqueen action
    node = node.prev
```

---

**Challenge Tasks:**

- Modify the linked list to support durations (e.g., forward for 2 seconds)
- Add more path complexity (e.g., u-turns, reverse beeps, LED signals)
- Create a reusable function: `run_command(cmd, reverse=False)`

---

**Reflection Questions:**

1. What makes a doubly linked list more useful than a singly linked list in this project?
2. How could you store sensor data or environment information alongside each node?
3. What happens if your robot loses track of its path halfway through? How could you recover?

---

**Completed Code for Lecturer Testing:**

`robot_doubly_linked_list.py`

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def is_empty(self):
        return self.head is None
```

`main.py`

```python
from maqueen import Maqueen
from robot_doubly_linked_list import DoublyLinkedList
import utime

robot = Maqueen()
path = DoublyLinkedList()

# Forward path
path.append("forward")   # move across classroom
path.append("right")     # turn into corridor
path.append("left")      # turn into hallway
path.append("forward")   # down the hallway
path.append("stop")      # stop

# Execute forward
print("Executing forward path...")
node = path.head
while node:
    cmd = node.value
    if cmd == "forward":
        robot.set_motor(0, 100)
        robot.set_motor(1, 100)
    utime.sleep(1)

utime.sleep(2)
print("Reversing path...")

robot.motor_stop_all()
print("Back at starting point.")
```

