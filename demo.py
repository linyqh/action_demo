#  写一个冒泡排序
def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    arr1 = [3, 5, 1, 7, 2, 9, 4, 6, 8]
    print(bubble_sort(arr1))
