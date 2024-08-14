from mynamedtuple import mynamedtuple

class DictTuple:
    def __init__(self, *kwargs):

        self.dt = [dictionaries for dictionaries in kwargs]

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

        result_list = []
        if type(right) is DictTuple:
            self.dt = list(self.dt)
            self.dt.extend(right.dt)

            for dictionary in self.dt:
                if dictionary not in result_list:
                    result_list.append(dictionary)

            return DictTuple(*result_list)

        elif type(right) is dict:

            self.dt = list(self.dt)
            right = list(right)
            self.dt.extend(right)

            for dictionary in self.dt:
                if dictionary not in result_list:
                    result_list.append(dictionary)
            return DictTuple(*result_list)

        else:
            raise TypeError("The key is not DictTuple or Dict")

    def __radd__(self, left):

        result_list = []

        if type(left) is dict:
            left = list(left)
            self.dt = list(self.dt)
            self.dt.insert(0, left)
            for dictionary in self.dt:
                if dictionary not in result_list:
                    result_list.append(dictionary)
            return DictTuple(*result_list)

        elif type(left) is DictTuple:
            self.dt = list(self.dt)
            self.dt.insert(0, left.dt)
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

    def __setattr__(self, name, value):
        if name != "dt":
            raise AssertionError("The variable name is wrong, should be dt")
        self.__dict__[name] = value

