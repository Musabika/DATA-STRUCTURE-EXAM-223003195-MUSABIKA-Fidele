from collections import deque

parcel_deque = deque()

def add_parcel_rear(parcel_id):
    parcel_deque.append(parcel_id)
    print(f"Parcel {parcel_id} added at the rear.")

def add_parcel_front(parcel_id):
    parcel_deque.appendleft(parcel_id)
    print(f"Parcel {parcel_id} added at the front.")

def remove_parcel_front():
    if parcel_deque:
        parcel_id = parcel_deque.popleft()
        print(f"Parcel {parcel_id} removed from the front.")
        return parcel_id
    print("No parcels to remove from the front.")
    return None

def remove_parcel_rear():
    if parcel_deque:
        parcel_id = parcel_deque.pop()
        print(f"Parcel {parcel_id} removed from the rear.")
        return parcel_id
    print("No parcels to remove from the rear.")
    return None

def view_parcels():
    if parcel_deque:
        print("Current parcels in the system:", list(parcel_deque))
    else:
        print("No parcels in the system.")

def is_empty():
    return len(parcel_deque) == 0

def parcel_count():
    return len(parcel_deque)

def create_node(parcel_id):
    return {"id": parcel_id, "next": None}

head = None

def add_parcel_linked_list(parcel_id):
    global head
    new_node = create_node(parcel_id)
    if not head:
        head = new_node
    else:
        current = head
        while current["next"]:
            current = current["next"]
        current["next"] = new_node
    print(f"Parcel {parcel_id} added to the linked list.")

def remove_parcel_linked_list():
    global head
    if not head:
        print("No parcels to remove from the linked list.")
        return None
    parcel_id = head["id"]
    head = head["next"]
    print(f"Parcel {parcel_id} removed from the linked list.")
    return parcel_id

def view_parcels_linked_list():
    if not head:
        print("No parcels in the linked list.")
        return
    current = head
    parcels = []
    while current:
        parcels.append(current["id"])
        current = current["next"]
    print("Current parcels in the linked list:", parcels)

def create_circular_queue(max_size):
    queue = [None] * max_size
    return {
        "queue": queue,
        "max_size": max_size,
        "front": -1,
        "rear": -1
    }

def is_full(circular_queue):
    return (circular_queue["rear"] + 1) % circular_queue["max_size"] == circular_queue["front"]

def is_empty_queue(circular_queue):
    return circular_queue["front"] == -1

def enqueue(circular_queue, order_id):
    if is_full(circular_queue):
        print("Queue is full. Cannot add more orders.")
        return
    if is_empty_queue(circular_queue):
        circular_queue["front"] = 0
    circular_queue["rear"] = (circular_queue["rear"] + 1) % circular_queue["max_size"]
    circular_queue["queue"][circular_queue["rear"]] = order_id
    print(f"Order {order_id} added to the circular queue.")

def dequeue(circular_queue):
    if is_empty_queue(circular_queue):
        print("Queue is empty. No orders to remove.")
        return None
    order_id = circular_queue["queue"][circular_queue["front"]]
    if circular_queue["front"] == circular_queue["rear"]:
        circular_queue["front"] = circular_queue["rear"] = -1  # Queue is now empty
    else:
        circular_queue["front"] = (circular_queue["front"] + 1) % circular_queue["max_size"]
    print(f"Order {order_id} removed from the circular queue.")
    return order_id

def view_queue(circular_queue):
    if is_empty_queue(circular_queue):
        print("No orders in the circular queue.")
        return
    orders = []
    i = circular_queue["front"]
    while True:
        orders.append(circular_queue["queue"][i])
        if i == circular_queue["rear"]:
            break
        i = (i + 1) % circular_queue["max_size"]
    print("Current orders in the circular queue:", orders)

cq = create_circular_queue(3)
enqueue(cq, "O001")
enqueue(cq, "O002")
enqueue(cq, "O003")
view_queue(cq)
dequeue(cq)
enqueue(cq, "O004")
view_queue(cq)

add_parcel_front("P456")
add_parcel_rear("P789")
add_parcel_front("P1011")
view_parcels()
remove_parcel_front()
view_parcels()
remove_parcel_rear()
view_parcels()

add_parcel_linked_list("L001")
add_parcel_linked_list("L002")
add_parcel_linked_list("L003")
view_parcels_linked_list()
remove_parcel_linked_list()
view_parcels_linked_list()
