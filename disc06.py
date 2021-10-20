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