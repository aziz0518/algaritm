def linear_search(arr: list, target: int) -> int:
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    else:
        return None


arr = [10, 20, 30, 40, 50, 60]

print(linear_search(arr, 30))