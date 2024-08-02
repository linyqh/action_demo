#  写一个冒泡排序
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    arr1 = [5, 3, 8, 1, 9, 2]
    x = bubble_sort(arr1)
    print(x)
