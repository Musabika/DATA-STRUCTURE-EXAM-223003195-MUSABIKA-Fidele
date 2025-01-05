class Parcel:
    def __init__(self, parcel_id, priority):
        self.parcel_id = parcel_id
        self.priority = priority

    def __repr__(self):
        return f"Parcel({self.parcel_id}, {self.priority})"

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and key.priority < bucket[j].priority:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
    return bucket

def bucket_sort(parcels):
    max_priority = max(parcels, key=lambda p: p.priority).priority
    min_priority = min(parcels, key=lambda p: p.priority).priority

    bucket_count = max_priority - min_priority + 1
    buckets = [[] for _ in range(bucket_count)]

    for parcel in parcels:
        index = parcel.priority - min_priority
        buckets[index].append(parcel)

    sorted_parcels = []
    for bucket in buckets:
        sorted_parcels.extend(insertion_sort(bucket))

    return sorted_parcels

def main():
    parcels = [
        Parcel("P001", 5),
        Parcel("P002", 1),
        Parcel("P003", 3),
        Parcel("P004", 4),
        Parcel("P005", 2)
    ]
    
    print("Before Sorting:")
    print(parcels)
    
    sorted_parcels = bucket_sort(parcels)
   
    print("\nAfter Sorting:")
    print(sorted_parcels)
main()
