from mynamedtuple import mynamedtuple

class DictTuple:
    def __init__(self, *kwargs):

        self.dt = [dictionaries for dictionaries in kwargs]
        print("받은값: ", self.dt)

        if len(self.dt) == 0:
            raise AssertionError("Dictionary is empty")

        if type(self.dt[0]) == dict:
            if len(self.dt[0]) == 0:
                raise AssertionError("Dictionary is empty")
        else:
           raise AssertionError(f"DictTuple.__init__:{self.dt[0]} is not a dictionary")

        for i in range(len(self.dt)):
            if len(self.dt[i]) == 0:
                raise AssertionError("Dictionary is empty")


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
        print("eq 안에 들어옴")

        left_keys = {}
        right_keys = {}

        if not isinstance(other, DictTuple):
            return False

        for left_dict in self.dt:
            for left_key, left_value in left_dict.items():
                left_keys[left_key] = left_value

        for right_dict in other.dt:
            for right_key, right_value in right_dict.items():
                right_keys[right_key] = right_value

        if left_keys != right_keys:
            return False

        return True




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
        print("get item 안에 들어옴")

        if type(self.dt) is tuple:
            self.dt = list(self.dt)
        dict_keys = []
        for dictionary in reversed(self.dt):
            for key in dictionary.keys():
                dict_keys.append(key)
        if k not in dict_keys:
            raise KeyError("The key does not exists")

        if type(k) == str:
            for dictionaries in reversed(self.dt):
                return_list = []
                for key, value in dictionaries.items():
                    if k == key:
                        if type(value) is int:
                            return value
                        else:
                            for i in value:
                                return_list.append(i)

                        return tuple(return_list)
        else:
            raise TypeError("the key is not in string")

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
        print("add 안에 들어옴")
        print("self.dt는: ", self.dt, type(self.dt))
        print("right은: ", right, type(right))
        result_list = []
        if type(right) is DictTuple:
            if self.dt is tuple:
                self.dt = list(self.dt)
            self.dt.extend(right.dt)
            for dictionary in self.dt:

                if dictionary not in result_list:
                    result_list.append(dictionary)
                    print(result_list)
            return DictTuple(*result_list)

        elif type(right) is dict:
            if self.dt is tuple:
                self.dt = list(self.dt)
            self.dt.extend(right)

            for dictionary in self.dt:
                if dictionary not in result_list:
                    result_list.append(dictionary)
            return DictTuple(*result_list)

        else:
            raise TypeError("The key is not DictTuple or Dict")

    def __radd__(self, left):
        print("__radd__ 들어옴")

        result_list = []

        if type(left) is dict:
            self.dt.insert(0, left)
            print("여기는", self.dt)
            for dictionary in self.dt:
                if dictionary not in result_list:
                    result_list.append(dictionary)
            return DictTuple(*result_list)

        elif type(left) is DictTuple:
            self.dt.insert(0, left)
            for dictionary in self.dt:
                if dictionary not in result_list:
                    result_list.append(dictionary)
            return DictTuple(*result_list)

        elif type(left) is tuple:
            left = list(left)
            self.dt = list(self.dt)
            for i in range(len(left), 0, -1):
                self.dt.insert(0, left[i-1])
            for dictionary in self.dt:
                if dictionary not in result_list:
                    result_list.append(dictionary)
            return DictTuple(*result_list)

        else:
            raise TypeError("The key is not DictTuple or Dict")

    def __call__(self, argument):
        print("__call__ 들어옴")
        my_list = []
        for dictionaries in self.dt:
            for key, values in dictionaries.items():
                if key == argument:
                    inner_list = []
                    if type(values) is int:
                        inner_list.append(values)
                        my_list.append(inner_list)
                    else:
                        for value in values:
                            inner_list.append(value)
                        my_list.append(inner_list)
        return my_list

    def __iter__(self):
        total_list = []
        for dictionary in reversed(self.dt):
            for key in dictionary.keys():
                if key not in total_list:
                    yield key
                total_list.append(key)

        return self

    def __setitem__(self, index, value):
        print("set items 들어옴")
        key_lists = []
        for dictionaries in self.dt:
            for key in dictionaries.keys():
                key_lists.append(key)

        if index not in key_lists:
            self.dt.append({index:value})

        for dictionaries in reversed(self.dt):
            if index in dictionaries.keys():
                dictionaries[index] = value
                break


#coordinate = mynamedtuple('coordinate', 'x y')
#d = DictTuple({'c1': coordinate(1, 2)}, {'c1': coordinate(3, 4)})
#d1 = DictTuple({'c1': coordinate(1, 2)}, {'c1': coordinate(3, 4)})
#d2 = DictTuple({'c2': coordinate(1, 2)}, {'c3': coordinate(3, 4)})
#d4 = DictTuple({'c1': coordinate(1, 2)}, {'c1': coordinate(3, 4)}, {'c2': coordinate(1, 2)}, {'c3': coordinate(3, 4)})

#print("더하기", d2+d1)

# set items
#print("set items 없을때: ")
#d4['c4'] = 1
#p = DictTuple({'a': 1, 'b': 2}, {'b': 12, 'c': 13})
#print("set items 있을때: ")
#p['b'] = 13
#print("iter: ", d4.__iter__())
#print("d4['c1']", d4['c1'])
#print("d4 :", d4)
#print("d4 __call__ :", d4.__call__(argument='c1'))

#test1 = DictTuple({'a': 1, 'b': 2}, {'b': 12, 'c': 13})
#test2 = DictTuple({'a': 1, 'b': 12}, {'c': 13})
#print("EQ는: ", test1 == test2)

# Eq 함수
# mynamed도 불려오네
#print("eq: True?", d == d1)
#print("eq: False?", d == d2)
# Len 함수
#print("d.__len__():", d.__len__())
# Bool 함수
#print("d.__bool__():", d.__bool__())
# Repr 함수
# print("repr(d):, ", repr(d))
# Contains
#print("contains: ", d4.__contains__('c2'))
#GetItems
#print("getitems: ", d4.__getitem__('c1'))
#print("getitems : ", d4['c1'])
# newGet
#p4 = DictTuple({'a': 1, 'b': 2, 'c': 3}, {'c': 13, 'd': 14, 'e': 15}, {'e': 25, 'f': 26, 'g': 27})
#print("getItems: ", p4.__getitem__('e'))

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


# 3.
#adt = {'a': 1, 'b': 2}, {'b': 12, 'c': 13}
#adict = DictTuple({'a': 'one', 'b': 'two'}, {'b': 'twelve', 'c': 'thirteen'}, {'a': 1, 'b': 2}, {'b': 12, 'c': 13})
#print("adt + adict는 : ", adt + adict)


# new EQ
#p = DictTuple({'a': 'one', 'b': 'two'}, {'b': 'twelve', 'c': 'thirteen'}, {'a': 1, 'b': 2}, {'b': 12, 'c': 13}, {'a': 'one', 'b': 'two'}, {'b': 'twelve', 'c': 'thirteen'})
#p1 = DictTuple({'a': 'one', 'b': 'two'}, {'b': 'twelve', 'c': 'thirteen'}, {'a': 1, 'b': 2}, {'b': 12, 'c': 13})
#p2 = DictTuple({'a': 1, 'b': 12}, {'c': 13})
#print("더하기", p+p1)

#print("eq: False", p1.__eq__(p2))
#print("eq: True", p.__eq__(p1))
#print("add: ", p2+p1)




#p3 = DictTuple({'a': 1, 'b': 2, 'c': 3}, {'c': 13, 'd': 14, 'e': 15}, {'e': 25, 'f': 26, 'g': 27})
#print("ITER 보자:", p3.__iter__())
#print("ITER 이어서:", iter(p3))

#for i in p3:
 #   print(str(i) + ', ', end = '')
  #  print('finished')
