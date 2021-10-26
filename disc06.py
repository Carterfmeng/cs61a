class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i-1]
    def __len__(self):
        return 1 + len(self.rest)
    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(self.first)
        else:
            return 'Link({}, {})'.format(self.first, repr(self.rest))

def flip_two(lnk):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    # if lnk.rest is Link.empty:
    #     return
    # else:
    #     lnk.first, lnk.rest.first = lnk.rest.first, lnk.first
    #     flip_two(lnk.rest.rest)
    pos = lnk
    while not (pos.rest is Link.empty):
        pos.first, pos.rest.first = pos.rest.first, pos.first
        pos = pos.rest.rest

# def return_f(lnk):
#     flip_two(lnk)
#     return lnk

def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> unique = remove_duplicates(lnk)
    >>> len(unique)
    2
    >>> len(lnk)
    2
    """
    def helper(lnk):
        if lnk.rest is Link.empty:
            return
        else:
            if lnk.first == lnk.rest.first:
                lnk.rest = lnk.rest.rest
                remove_duplicates(lnk)
            else:
                remove_duplicates(lnk.rest)
    helper(lnk)
    return lnk

def reverse(lnk):
    """
    >>> a = Link(1, Link(2, Link(3)))
    >>> r = reverse(a)
    >>> r.first
    3
    >>> r.rest.first
    2
    """
    if lnk.rest is Link.empty:
        return lnk
    else:
        rest_rev  = reverse(lnk.rest)
        lnk.rest.rest = lnk
        lnk.rest = Link.empty
        return rest_rev
    
def max_product(lst):
    """Return the maximum product that can be formed using lst
    without using any consecutive numbers
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if lst == []:
        return 1
    else:
        use_first = lst[0] * max_product(lst[2:])
        not_use_fist = max_product(lst[1:])
        return max(use_first, not_use_fist)


# We choose one element of the list to be the pivot
# element and partition the remaining elements into two lists: one of elements less
# than the pivot and one of elements greater than the pivot. We recursively sort the
# two lists,
def quicksort_list(lst):
    """
    >>> quicksort_list([3, 1, 4])
    [1, 3, 4]
    """
    if lst == []:
        return lst
    pivot = lst[0]
    less = [elem for elem in lst[1:] if elem <= pivot]
    greater = [elem for elem in lst[1:] if elem > pivot]
    return quicksort_list(less) + [pivot] + quicksort_list(greater)

# 比较相邻的元素。如果第一个比第二个大，就交换他们两个;
# 对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数;
# 针对所有的元素重复以上的步骤，除了最后一个;
# 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较;
def BubbleSort(matrix):  
    for i in range(len(matrix) - 1):
        flag = True
        for j in range(len(matrix)-i-1): #要用到j+1，防止溢出，减掉1
            if matrix[j] > matrix[j + 1]:
                matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]
                flag = False
        if (flag): break
    return matrix

#第一次循环找出最大值（最小值），记录其下标，把他与最末尾（首）的元素交换，第二次找到第二大的，与倒数第二末尾的元素进行交换。第一次循环的范围是（0，数组长度-1），第二次是（0，数组长度-2）
def SelectionSort(matrix): 
    n = len(matrix)
    for i in range(n):
        index = 0
        for j in range(n - i): #每次拿出最大值放在末尾,然后继续比较剩余的n-i个数
            if matrix[j] > matrix[index]:
                index = j
        matrix[n - i - 1], matrix[index] = matrix[index], matrix[n - i - 1] #把最大值放在末尾
    return matrix

#相当于打牌时候摸牌，如数组[25, 5, 3, 9, 23, 44, 29]，第一张摸到的牌是25，第二张摸到了5，与25比较大小，放在25前面，依次摸完所有的牌，也就排序结束了。
# def InsertSort(matrix):
#     n = len(matrix)
#     for i in range(1, n):
#         cur = i
#         pre = cur - 1
#         while pre >= 0 and matrix[cur] < matrix[pre]:
#             if matrix[cur] < matrix[pre]:
#                 matrix[pre], matrix[cur] = matrix[cur], matrix[pre]
#                 cur = pre
#                 pre = cur - 1
#     return matrix

def InsertSort(matrix):
    for i in range(1, len(matrix)):
        tmp = i
        while tmp > 0:
            if matrix[tmp] < matrix[tmp - 1]:
                matrix[tmp], matrix[tmp - 1] = matrix[tmp - 1], matrix[tmp]
                tmp -= 1
            else:
                break

    return matrix

def ShellSort(matrix):
    n = len(matrix)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            for tmp in range(i, gap - 1, -gap):
                if matrix[tmp] < matrix[tmp - gap]:
                    matrix[tmp], matrix[tmp - gap] = matrix[tmp - gap], matrix[tmp]

        if gap == 2:
            gap = 1
        else:
            gap //= 2
    return matrix

#拿最后一层不断跟上一层比，返回更长的值？
def widest_level(t):
    """
    >>> sum([[1], [2]], [])
    [1, 2]
    >>> t = Tree(3, [Tree(1, [Tree(1), Tree(5)]),
    ... Tree(4, [Tree(9, [Tree(2)])])])
    >>> widest_level(t)
    [1, 5, 9]
    """
    levels = []
    x = [t]
    while [x]:
        x = [b for b in t.branches]
        levels = sum(t.label, [])
        # [[t.label] for ]
    return max(levels, key=lambda temp: len(temp))

















class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()