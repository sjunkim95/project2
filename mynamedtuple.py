import keyword


def mynamedtuple(type_name, field_names, mutable=False, defaults={}):

    if type(field_names) == list:
        copy_field_names = []
        for i in field_names:
            i = i.strip()
            copy_field_names.append(i)
        field_names = copy_field_names
        field_names = sorted(list(set(field_names)))

    if type(field_names) == str:

        if ',' in field_names:
            field_names = field_names.split(',')
            copy_field_names = []
            for i in field_names:
                i = i.strip()
                copy_field_names.append(i)
            field_names = copy_field_names
        else:
            field_names = field_names.split(' ')
            copy_field_names = []
            for i in field_names:
                i = i.strip()
                copy_field_names.append(i)
            field_names = copy_field_names

        temp_list = []
        for names in field_names:
            if names not in temp_list:
                temp_list.append(names)
            field_names = temp_list

    for i in defaults.keys():
        if i not in field_names:
            raise SyntaxError(f"Invalid field name value: {i}")

    if type(type_name) == int:
        raise SyntaxError(f"int should not be the type_name")
    if not type_name.isidentifier():
        raise SyntaxError(f"Invalid type name: {type_name}")
    if keyword.iskeyword(type_name):
        raise SyntaxError(f"Invalid keyword name: {type_name}")

    if type(field_names) == list or type(field_names) == str:
        if type(field_names) == str:
            if keyword.iskeyword(field_names):
                raise SyntaxError(f"Invalid keyword names: {field_names}")
        if type(field_names) == list:
            for i in field_names:
                if keyword.iskeyword(i):
                    raise SyntaxError(f"Invalid keyword names: {i}")
    else:
        raise SyntaxError(f"Invalid field names: {field_names}")

    my_init = ""
    init_keyword = ','.join(field_names)
    for i in field_names:
        my_init += f"self.{i} = {i}\n        "

    code = f'''
class {type_name}:

    _mutable = {mutable}  
    _fields = {field_names}
                    
    def __init__(self, {init_keyword}): 
        {my_init}
                
    def __repr__(self):
        return '{type_name}('+','.join(f"{{self._fields[i]}}={{self.__dict__[self._fields[i]]}}" for i in range(len(self._fields)))+')'
    
    def __eq__(self, other):
        if not isinstance(other, {type_name}):
            return False
        for i in range(len(self._fields)):
            field_name = self._fields[i]
            if (self.__dict__[field_name] != other.__dict__[field_name]):
                return False
        return True
       
    def _replace(self, **kwargs):
        temp = dict()
        for i in range(len(self._fields)):
            field_name = self._fields[i]
            temp[field_name] = self.__dict__[field_name]
            for key in kwargs.keys():
                if key not in self._fields:
                    raise TypeError("Key is wrong")
                if self._mutable:
                    self.__dict__[key] = kwargs[key]
                else:
                    temp[key] = kwargs[key]
        if self._mutable:
            return None
        else:
            return eval(f'{type_name}('+','.join(f"{{k}}={{v}}" for k, v in temp.items())+')')
            
    def __getitem__(self, index):
        if index >= len(self._fields):
            raise IndexError("Index out of range")
        if type(index) is int:
            return self.__dict__[self._fields[index]]
        else:
            raise TypeError("the index is not int")
    
    def _asdict(self):
        store = ','.join(f"{{self._fields[i]}}:{{self.__dict__[self._fields[i]]}}" for i in range(len(self._fields)))
        
        dictionary = dict(i.split(":") for i in store.split(","))
        for k, v in dictionary.items():
            if type(v) == str:
                dictionary[k] = int(v)
        return dictionary
        
    def _make(iterable):
        return {type_name}(*iterable)
        
    def __setattr__(self, name, value):
        if {type_name}._mutable:
            self.__dict__[name] = value
        elif not {type_name}._mutable and name not in self.__dict__ and name in {type_name}._fields:
            self.__dict__[name] = value
        else:
            raise AttributeError("Attribute cannot be set")
      
'''

    for i in field_names:
        code += f'''
    def get_{i}(self):
        return self.__dict__['{i}']
        '''

    namespace = {}
    exec(code, namespace)

    return namespace[type_name]
