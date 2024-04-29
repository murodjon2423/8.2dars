class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, position, data):
        if position < 0:
            print("Invalid position!")
            return
        if position == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        prev = None
        current_position = 0
        while current_position < position and current:
            prev = current
            current = current.next
            current_position += 1
        if current_position < position:
            print("Invalid position!")
            return
        new_node = Node(data)
        prev.next = new_node
        new_node.next = current


    def sum_last(self):
        if not self.head:
            return 0
        total = 0
        current = self.head
        while current:
            total += current.data
            current = current.next
        return total

    def average(self):
        if not self.head:
            return None
        total = 0
        count = 0
        current = self.head
        while current:
            total += current.data
            count += 1
            current = current.next
        return total / count


    def delete_node(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def insert_after(self, prev_node_data, new_data):
        current = self.head
        while current:
            if current.data == prev_node_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"{prev_node_data} not found in the list.")

    def remove_duplicates(self):
        current = self.head
        prev = None
        seen = set()
        while current:
            if current.data in seen:
                prev.next = current.next
                current = None
            else:
                seen.add(current.data)
                prev = current
            current = prev.next

    def convert_to_linked_list(lst):
        linked_list = LinkedList()
        for item in lst:
             linked_list.append(item)
        return linked_list


# Test qismi
# LinkedList obyektini yaratish
linked_list = LinkedList()

# Ma'lumotlarni qo'shish
linked_list.insert_at_position(0, 5)  # 5 ni boshiga qo'shish
linked_list.insert_at_position(1, 3)  # 3 ni keyingisiga qo'shish
linked_list.insert_at_position(2, 7)  # 7 ni keyingisiga qo'shish
linked_list.insert_at_position(1, 4)  # 4 ni 2-o'riniga qo'shish

# Linked list ma'lumotlarini chiqarish
print("Linked list ma'lumotlari:")
current = linked_list.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# Elementlarni o'chirishni sinab ko'rish
linked_list.delete_node(3)  # 3 ni o'chirish
linked_list.delete_node(7)  # 7 ni o'chirish

# Linked list ma'lumotlarini chiqarish
print("Linked list ma'lumotlari o'chirildi:")
current = linked_list.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# Duplikatlar o'chirishni sinab ko'rish
linked_list.insert_at_position(2, 5)  # 5 ni qo'shish
linked_list.insert_at_position(4, 5)  # 5 ni qo'shish
linked_list.insert_at_position(2, 7)  # 7 ni qo'shish

print("Duplikatlarni o'chirishdan oldin:")
current = linked_list.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

linked_list.remove_duplicates()  # Duplikatlarni o'chirish

print("Duplikatlardan keyin:")
current = linked_list.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# O'rtacha hisoblash
print("O'rtacha:", linked_list.average())

# Oxirgi elementlarni qo'shish
linked_list.insert_after(4, 6)  # 4 dan keyingisiga 6 ni qo'shish
linked_list.insert_after(7, 8)  # 7 dan keyingisiga 8 ni qo'shish

print("So'nggi qo'shilgan ma'lumotlar:")
current = linked_list.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# Oxirgi elementlarni qo'shish
linked_list.insert_after(10, 9)  # 10 topilmadi, xabar chiqaradi

# Linked list ma'lumotlarini chiqarish
print("So'nggi qo'shilgan ma'lumotlar:")
current = linked_list.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# Oxirgi elementlarni qo'shish
linked_list.insert_after(8, 9)  # 8 dan keyingisiga 9 ni qo'shish

# Linked list ma'lumotlarini chiqarish
print("So'nggi qo'shilgan ma'lumotlar:")
current = linked_list.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# Linked list summasini hisoblash
print("Linked list summasi:", linked_list.sum_last())
