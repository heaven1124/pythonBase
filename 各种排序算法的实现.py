# 冒泡排序
def bubble_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        # 如果一次循环后没有进行交换，说明后面已经有序了，后续循环无需在做
        swapped = False
        for j in  range(length - i - 1):
            if arr[j] > arr[j + 1]:
                # 交换位置
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped: break
    return arr


# 选择排序
def select_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        least = i
        for j in range(i+1, length):
            if arr[j] < arr[least]:
                # 更新least
                least = j
        # 交换位置
        arr[least], arr[i] = arr[i], arr[least]
    return arr


# 插入排序
def insertion_sort(arr):
    for loop_index in range(1, len(arr)):
        insertion_index = loop_index
        # 前一个大于后一个就交换位置
        while insertion_index > 0 and arr[insertion_index - 1] > arr[insertion_index]:
            # 交换位置
            arr[insertion_index - 1], arr[insertion_index] = arr[insertion_index], arr[insertion_index - 1]
            insertion_index -= 1
    return arr


# 快速排序
def quick_sort(arr):
    # 退出递归的条件
    length = len(arr)
    if length <= 1:
        return arr
    else:
        # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值，作为基准值。
        pivot = arr.pop()
        # 创建二个空列表
        greater, lesser = [], []
        for element in arr:
            if element > pivot:
                greater.append(element)
            else:
                lesser.append(element)
        # 递归调用
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    arr = input('请输入要排序的数字，以逗号分割').strip()
    arr = [int(item) for item in arr.split(',')]
    print(*quick_sort(arr), sep=',')