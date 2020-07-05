def median_num (*args):
    """calculate the median of any given set of numbers"""
    length = len(args)
    if length % 2 ==0:
        mid1 = int(length/2)
        mid2 = int(mid1 -1)
        median = (args[mid1]+ args[mid2]) /2
        return median
    elif length % 2 > 0:
        mid = int((length-1)/2)
        median = args[mid]
        return median
