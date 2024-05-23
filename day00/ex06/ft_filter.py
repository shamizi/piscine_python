def est_pair(x):
    return x% 2 == 0

def start_p(x):
    newlist = [item for item in x if "p" in item]
    return newlist

def ft_filter(function, iterable):
    """
filter(function or None, iterable) --> filter object\n
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    #print(ft_filter.__doc__)
    if function:
        return (x for x in iterable if function(x))
    return(x for x in iterable)

def main():
    #print(filter.__doc__)
    #print("____________________________________")
    liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    string = ["pomme", "poire", "peche", "kiwi", "banane"]
    mix = [1, "pomme", 2, "poire", 3]

    print(list(ft_filter(est_pair,liste)))
    print(list(filter(est_pair, liste)))
    
    print(list(ft_filter(start_p,string)))
    print(list(filter(start_p, string)))
    
    print(list(filter(None, string)))
    print(list(filter(None, string)))

main()
    