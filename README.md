# 🌀 Sorted Circular Linked List in Python

This project implements a Sorted Circular Linked List in Python.

### ✅ Features

- Each inserted node is automatically placed in its correct sorted position.
- The list maintains a circular structure, meaning the last node points back to the head.
- Includes methods to:
  - Insert elements in sorted order
  - Print the list in circular traversal from head to head

---

### 📌 Example

Inserting the integers: `7, 3, 9, 1, 4` one by one:

After inserting 7: [7]

After inserting 3: [3] -> [7]

After inserting 9: [3] -> [7] -> [9]

After inserting 1: [1] -> [3] -> [7] -> [9]

After inserting 4: [1] -> [3] -> [4] -> [7] -> [9]

### 💡 How it works

- If the list is empty:  
  → The inserted node becomes the head and points to itself.
  
- If the new value is less than the current head:  
  → Insert before head and update head.

- Otherwise:  
  → Traverse to find correct position and insert accordingly.
نسخ
تحر
