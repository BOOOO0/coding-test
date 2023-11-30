array = [11, 13, -40, 7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return
    # 첫 pivot은 start
    # 이후 재귀에서 들어오는 부분은 각 파티션의 첫 원소가 pivot이 될 것
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # pivot보다 작은 값을 left부터 찾기 위해 index에 변화를 주는 부분
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # pivot보다 큰 값을 right부터 찾기 위해 index에 변화를 주는 부분
        while right > start and array[right] >= array[pivot]:
            right -= 1
        
        # 교차가 될 때라면(엇갈리는 때)
        # 엇갈리는 때의 교체를 while 종료 후에 하면 안되는 이유?
        # if left > right:
        #     array[right], array[pivot] = array[pivot], array[right]
        # else:
        #     array[left], array[right] = array[right], array[left]
        
        # 그 외 각각 작은 값과 큰 값을 찾은 때라면
        if left <= right:
            array[left], array[right] = array[right], array[left]
        
    
    # 일단 빼서 확인해 봤는데 되긴 됨 
    array[right], array[pivot] = array[pivot], array[right]
    
    # 이 때 right의 인덱스가 pivot의 인덱스이므로
    # pivot 기준 왼쪽 파티션에 다시 퀵 정렬 명령
    quick_sort(array, start, right - 1)
    # pivot 기준 오른쪽 파티션에 다시 퀵 정렬 명령
    quick_sort(array, right + 1, end)
    

quick_sort(array, 0, len(array) - 1)

print(array)