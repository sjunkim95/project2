from mynamedtuple import mynamedtuple

class DictTuple:
    def __init__(self, *kwargs):

        self.dt = [dictionaries for dictionaries in kwargs]

        if type(self.dt[0]) == dict:
            if len(self.dt[0]) == 0:
                raise AssertionError("Dictionary is empty")
        else:
            raise AssertionError(f"DictTuple.__init__:{self.dt[0]} is not a dictionary")

    def __len__(self):
        len_set = set()
        for dictionary in self.dt:
            for key in dictionary:
                len_set.add(key)

        print(type(len(len_set)))
        return len(len_set)

    def __bool__(self):
        if len(self.dt) > 1:
            return True
        else:
            return False

    def __repr__(self):
        self.dt = tuple(self.dt)
        return f'DictTuple{self.dt}'

    def __eq__(self, other):
        if not isinstance(other, DictTuple):
            raise TypeError('not a DictTuple')
        return self.dt == other.dt

    def __contains__(self, args):
        key_list = []
        for dictionaries in self.dt:
            for i in dictionaries.keys():
                key_list.append(i)
        if args not in key_list:
            return False
        else:
            return True

    def __getitem__(self, k):
        if type(self.dt) is tuple:
            self.dt = list(self.dt)
        self.dt.reverse()
        dict_keys = []
        for dictionary in self.dt:
            for key in dictionary.keys():
                dict_keys.append(key)
        if k not in dict_keys:
            raise KeyError("The key does not exists")
        
        if type(k) == str:
            for dictionaries in self.dt:
                for key, value in dictionaries.items():
                    print("밸류는", key, value)
                    if key == k:
                        return_list = []
                        for i in value:
                            return_list.append(i)
                        return tuple(return_list)

        else:
            raise TypeError("the key is not in string")
        print("출력", self.dt)

    def __delitem__(self, k):
        if type(self.dt) == tuple:
            self.dt = list(self.dt)
        dict_keys = []
        for dictionary in self.dt:
            for key in dictionary.keys():
                dict_keys.append(key)
        if k not in dict_keys:
            raise KeyError("The key does not exists")
        if type(k) == str:
            for dictionaries in self.dt:
                if k in dictionaries.keys():
                    del dictionaries[k]

        else:
            raise TypeError("the key is not in string")

        length = len(self.dt)
        while length > 0:
            count = 0
            if len(self.dt[count]) == 0:
                self.dt.pop(count)
            length -= 1

    def __add__(self, right):
        print("add")
        if type(right) is dict:
            self.dt.append(right)
            return self.dt
        if type(right) is DictTuple:
            return self.dt + right.dt
        else:
            return NotImplemented


    def __radd__(self, left):
        print(type(left))
        print("여긴가")
        print("여기", self.dt, left)
        if type(left) is dict or DictTuple:
            self.dt.insert(0, left)
        else:
            raise TypeError("The key is not DictTuple or Dict")
        return self.dt




coordinate = mynamedtuple('coordinate', 'x y')
d = DictTuple({'c1': coordinate(1, 2)}, {'c1': coordinate(3, 4)})
d1 = DictTuple({'c1': coordinate(1, 2)}, {'c1': coordinate(3, 4)})
d2 = DictTuple({'c2': coordinate(1, 2)}, {'c3': coordinate(3, 4)})
d4 = DictTuple({'c1': coordinate(1, 2)}, {'c1': coordinate(3, 4)}, {'c2': coordinate(1, 2)}, {'c3': coordinate(3, 4)})


#print("d4 :", d4)
# Eq 함수
#print("eq: ", d.__eq__(d1))
# Len 함수
#print("d.__len__():", d.__len__())
# Bool 함수
#print("d.__bool__():", d.__bool__())
# Repr 함수
# print("repr(d):, ", repr(d))
# Contains
#print("contains: ", d4.__contains__('c2'))
# GetItems
#print("getitems: ", d4.__getitem__('c1'))
#print("getitems 이후: ", d4)
#print("여기는" , d['c1'])
# DelItems
#print("delitems :", d.__delitem__('c1'), "그 후 d:", d)
#print("delitems전 : ", d4)
#print("delitems : ", d4.__delitem__('c1'), "그 후 d4: ", d4)
#print("d.__getattr__(): ", d.__getattr__('c1'))

# __add__
# 1.
#print("d1+d2 는: ", d2+d1)

# 2.
#adt = DictTuple({'c1': coordinate(1, 2)}, {'c1': coordinate(3, 4)})
#adict = {'c3': coordinate(3, 4)}
#print("adict + adt: ", adt + adict)

# 3.
#adt = DictTuple({'c1': coordinate(1, 2)}, {'c1': coordinate(3, 4)})
#adict = {'c3': coordinate(3, 4)}

#print("adt + adict는 : ", adict + adt)



