def deep_merge_sum(*args, **kwargs):
    

    def merge_dictionary(a, b):
        for key, value in b.items():
            if key not in a:
                a[key] = value
            else:
                x = a[key]
                if type(x) in (int, float) and type(value) in (int, float):
                    a[key] = x + value
                elif type(x) in (list, tuple) and type(value) in (list, tuple):
                    a[key] = list(x) + list(value)
                elif type(x) is dict and type(value) is dict:
                    merge_dictionary(x, value)
                else:
                    a[key] = value
        return a
    
    result={}

    for arg in args:
        if type(arg) is dict:
            src = arg
        elif type(arg) in (list, tuple):
            src = dict(arg)
        else:
            continue

        merge_dictionary(result, src)

        if kwargs:
            merge_dictionary(result, kwargs)

    return result

def main():

    data1 = {"a": 1, "b": [1, 2], "c": {"x": 5}}
    data2 = [("a", 3), ("b", [3, 4]), ("c", {"y": 9})]
    data3 = {"b": [5], "c": {"x": 2, "z": 7}}

    print(deep_merge_sum(data1, data2, data3, d=100, e=[9]))

if __name__ == "__main__":
    main()