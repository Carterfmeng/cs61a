# Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

# Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

# For convenience
def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

# Example tree construction
t = tree(1, [tree(3, [tree(4), tree(5), tree(6)]), tree(2)])

def tree_max(t):
    """Return the max of a tree."""
    if is_leaf(t):
        return label(t)
    else:
        return max([label(t)] + [tree_max(b) for b in branches(t)])

def height(t):
    """Return the height of a tree"""
    if is_leaf(t):
        return 0
    else:
        return max([height(b) + 1 for b in branches(t)])


def square_tree(t):
    """Return a tree with the square of every element in t"""
    if is_leaf(t):
        return tree(label(t) ** 2)
    else:
        return tree(label(t) ** 2, [square_tree(b) for b in branches(t)])

def find_path(tree, x):
    """
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    path_now = []
    def helper(tree, x, path_now):
        if label(tree) == x:
            return path_now + [label(tree)]
        else:
            for b in branches(tree):
                result_path = helper(b, x, path_now + [label(tree)])
                if result_path != None:
                    return result_path
    return helper(tree, x, path_now)

def prune(t, k):
    def helper(t, k, depth_now):
        if depth_now == k:
            return tree(label(t))
        else:
            return tree(label(t), [ helper(b, k, depth_now + 1) for b in branches(t)])
    return helper(t, k, 0)