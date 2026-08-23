def binary_search_vis(arr, val):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        print(f"Checking index: {mid} (Value: {arr[mid]}) within range [{low}, {high}]")
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    binary_search_vis(arr, 23)
