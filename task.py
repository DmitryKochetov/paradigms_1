numbers = [1, 2, 3, 4, 5, 3]


def sort_list_declarative(numbers):
    numbers.sort(reverse=True)


print(f'список до сортировки {numbers}')
sort_list_declarative(numbers)
print(f'сортированный список {numbers}')

numbers2 = [1, 2, 3, 4, 5, 3, 7, 0]


def sort_list_imperative(numbers2):
     print(len(numbers2))
     for i in range(len(numbers2)-1):
        for j in range(len(numbers2)-i-1):
            if numbers2[j] < numbers2[j+1]:
                numbers2[j], numbers2[j + 1] = numbers2[j + 1], numbers2[j]



print(f'список до сортировки {numbers2}')
sort_list_imperative(numbers2)
print(f'сортированный список {numbers2}')
