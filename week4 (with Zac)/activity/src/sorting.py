def my_mutating_sort(items: list):
    items.sort()
    return items

def my_immutable_sort(items: list):
    new_sorted_list = list(items)
    new_sorted_list.sort()
    return new_sorted_list

def galaxy_sorting_method(galaxies: list):
    return my_mutating_sort(galaxies)