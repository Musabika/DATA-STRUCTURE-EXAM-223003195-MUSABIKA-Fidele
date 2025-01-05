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
    else:
        print("No parcels to remove from the front.")
        return None
def remove_parcel_rear():
    if parcel_deque:
        parcel_id = parcel_deque.pop()
        print(f"Parcel {parcel_id} removed from the rear.")
        return parcel_id
    else:
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
add_parcel_rear("P123")
add_parcel_front("P456")
add_parcel_rear("P789")
add_parcel_front("P1011")
view_parcels()
remove_parcel_front()
view_parcels()
remove_parcel_rear()
view_parcels()