from collections import deque

# Deque-based parcel tracking system
parcel_deque = deque()

# Functions to add parcels
def add_parcel_rear(parcel_id):
    parcel_deque.append(parcel_id)
    print(f"Parcel {parcel_id} added at the rear.")

def add_parcel_front(parcel_id):
    parcel_deque.appendleft(parcel_id)
    print(f"Parcel {parcel_id} added at the front.")

# Functions to remove parcels
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

# View, check, and count parcels
def view_parcels():
    if parcel_deque:
        print("Current parcels in the system:", list(parcel_deque))
    else:
        print("No parcels in the system.")

def is_empty():
    return len(parcel_deque) == 0

def parcel_count():
    return len(parcel_deque)

# Linked list node class
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

add_parcel_rear("P123")
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
