def findClosestValueinBst(tree, target):
    return findClosestValueinBstHelper(tree, target, float("inf"))

def findClosestValueinBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueinBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueinBstHelper(tree.right, target, closest)
    else:
        return closest

def findClosestValueinBstHelper2(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            currentNode = tree.value
        if target < currentNode.value:
            return findClosestValueinBstHelper(currentNode.left, target, closest)
        elif target > currentNode.value:
            return findClosestValueinBstHelper(currentNode.right, target, closest)
        else:
            break
    return closest