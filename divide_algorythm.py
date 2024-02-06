def divide_conq(target, arr=[1,2,3,4,5,6,7,8,9])
    mid = len(arr)/2
    mid_index = index(arr[mid])
    mid_item = arr[mid_index]

    while mid_item != target:
        if target > mid_item:
            new_arr = arr[:mid_index + 1]
