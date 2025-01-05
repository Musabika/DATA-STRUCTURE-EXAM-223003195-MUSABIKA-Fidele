def height(node):
    if not node:
        return 0
    return node['height']

def balance_factor(node):
    if not node:
        return 0
    return height(node['left']) - height(node['right'])

def rotate_right(y):
    x = y['left']
    T2 = x['right']
    x['right'] = y
    y['left'] = T2
    y['height'] = max(height(y['left']), height(y['right'])) + 1
    x['height'] = max(height(x['left']), height(x['right'])) + 1
    return x

def rotate_left(x):
    y = x['right']
    T2 = y['left']
    y['left'] = x
    x['right'] = T2
    x['height'] = max(height(x['left']), height(x['right'])) + 1
    y['height'] = max(height(y['left']), height(y['right'])) + 1
    return y

def insert(root, parcel_id):
    if not root:
        return {'parcel_id': parcel_id, 'left': None, 'right': None, 'height': 1}

    if parcel_id < root['parcel_id']:
        root['left'] = insert(root['left'], parcel_id)
    else:
        root['right'] = insert(root['right'], parcel_id)

    root['height'] = max(height(root['left']), height(root['right'])) + 1
    balance = balance_factor(root)

    if balance > 1 and parcel_id < root['left']['parcel_id']:
        return rotate_right(root)

    if balance < -1 and parcel_id > root['right']['parcel_id']:
        return rotate_left(root)

    if balance > 1 and parcel_id > root['left']['parcel_id']:
        root['left'] = rotate_left(root['left'])
        return rotate_right(root)

    if balance < -1 and parcel_id < root['right']['parcel_id']:
        root['right'] = rotate_right(root['right'])
        return rotate_left(root)

    return root

def min_value_node(node):
    current = node
    while current['left']:
        current = current['left']
    return current

def delete(root, parcel_id):
    if not root:
        return root

    if parcel_id < root['parcel_id']:
        root['left'] = delete(root['left'], parcel_id)
    elif parcel_id > root['parcel_id']:
        root['right'] = delete(root['right'], parcel_id)
    else:
        if not root['left']:
            return root['right']
        elif not root['right']:
            return root['left']
        temp = min_value_node(root['right'])
        root['parcel_id'] = temp['parcel_id']
        root['right'] = delete(root['right'], temp['parcel_id'])

    if not root:
        return root

    root['height'] = max(height(root['left']), height(root['right'])) + 1
    balance = balance_factor(root)

    if balance > 1 and balance_factor(root['left']) >= 0:
        return rotate_right(root)

    if balance < -1 and balance_factor(root['right']) <= 0:
        return rotate_left(root)

    if balance > 1 and balance_factor(root['left']) < 0:
        root['left'] = rotate_left(root['left'])
        return rotate_right(root)

    if balance < -1 and balance_factor(root['right']) > 0:
        root['right'] = rotate_right(root['right'])
        return rotate_left(root)

    return root

def in_order_traversal(root):
    if root:
        in_order_traversal(root['left'])
        print(root['parcel_id'], end=' ')
        in_order_traversal(root['right'])

root = None
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 10)
root = insert(root, 5)

print("Parcels in AVL Tree:")
in_order_traversal(root)

root = delete(root, 10)
print("\nAfter removing parcel 10:")
in_order_traversal(root)
