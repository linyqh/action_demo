#  写一个冒泡排序
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [5, 3, 8, 1, 9, 2]
print(bubble_sort(arr))

if __name__ == '__main__':
    print(bubble_sort([5, 3, 8, 1, 9, 2]))
