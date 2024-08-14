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

    for i in defaults.keys():
        if i not in field_names:
            raise SyntaxError(f"Invalid field name value: {i}")

   # print("타입네임", type_name, "필드네임", field_names, "defaults는:", defaults)

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

    code = f'''
class {type_name}:

    _mutable = {mutable}  
    _fields = {field_names}
                    
    def __init__(self, *args, **kwargs):
        
        self.args = args
        self.kwargs = kwargs  
        
        if len(self.kwargs) == 0:
            for i in range(len(self._fields)):
                field_name = self._fields[i]
                self.__dict__[field_name]= self.args[i]

        if len(self.args) == 0:
            for i in range(len(self._fields)):
                field_name = self._fields[i]
                self.__dict__[field_name]= self.kwargs[field_name]
                
    def __repr__(self):
        return '{type_name}('+','.join(f"{{self._fields[i]}}={{self.__dict__[self._fields[i]]}}" for i in range(len(self._fields)))+')'
    
    def __eq__(self, other):
        print("EQ myname 들어옴")
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
        z
    def __getitem__(self, index):
        if index >= len(self._fields):
            raise IndexError("Index out of range")
        if type(index) is int:
            return self.__dict__[self._fields[index]]
        else:
            raise TypeError("the index is not int")
   
    def __contains__(self, item):
        for v in self.return_dict.values():
            if v == item:
                return True
        return False
    
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
        if not self._mutable:
            raise AttributeError("Attribute cannot be set")
        self.__dict__[name] = value

        
      
'''

    for i in field_names:
        code += f'''
    def get_{i}(self):
        return self.__dict__['{i}']
        '''

    namespace = {}
    exec(code, namespace)

    return namespace[type_name]

#coordinate = mynamedtuple('coordinate', ['x', 'y'])
#print("coordinate리턴은: ", coordinate)
#p = coordinate(0, 0)
#print("setattr:", p.__setattr__('x', 1))
#print("p는:", p)

#Triple1 = mynamedtuple("Triple1", ['a', 'b', 'c'])
#Triple2 = mynamedtuple("Triple3", ['a', 'b', 'c'])
#print(Triple1.a)
#print(Triple1.__eq__(Triple1, Triple2))


#coordinate = mynamedtuple('coordinate', ['x', 'y'])
#Triple1 = mynamedtuple("Triple1", ['a', 'b', 'c'])
#t1 = Triple1(a=2, b=2, c=2)
#print(t1)
#print("replace: ,", t1._replace(a=2, b=2, c=0))
#p = coordinate(0, 0)
#print("p는:", p)

#coordinate = mynamedtuple('coordinate', ['x', 'y'], mutable=True)
#print("coordinate리턴은: ", coordinate)
#p = coordinate(0, 0)
#print("setattr:", p.__setattr__('x', 1))
#print("p는:", p)

#print("replace: ", p._replace(y=5))
#print("get함수:", p.get_x())
#print("p[0]:", p[1])
#print("asdict:", p._asdict())
#print("_make: ", coordinate._make((0,1)))
#origin = coordinate(0, 0)
#dif = repr(origin)
#yes = eval(dif)
#print("yes", yes.x)
#print("repr(origin)", repr(origin))
#print("여기", yes == origin)
#print("되나", origin.get_x())

#origin = coordinate(0,0)
#new_origin = origin._replace(y=5)
#print(origin, new_origin)
