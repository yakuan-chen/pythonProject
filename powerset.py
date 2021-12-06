def powerset(array):
    subsets = [[]]
    for ele in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [ele])
    return subsets

def powerset2(array, idx = None):
    if idx is None:
        idx = len(array) - 1
    elif idx < 0 :
        return [[]]
    ele = array[idx]
    subsets = powerset2(array, idx - 1)
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [ele])
    return subsets