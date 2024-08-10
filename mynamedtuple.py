import keyword


def mynamedtuple(type_name, field_names, mutable=False, defaults={}):

    if type(field_names) == list:
        field_names = sorted(list(set(field_names)))
    if type(field_names) == str:
        if ',' in field_names:
            field_names = field_names.split(',')
        else:
            field_names = field_names.split(' ')

    for i in range(len(field_names)):
        if field_names[i] not in defaults.keys():
            defaults[field_names[i]] = 0

  #  print("타입네임", type_name, "필드네임", field_names, "defaults는:", defaults)
    if not type_name.isidentifier():
        raise SyntaxError(f"Invalid type name: {type_name}")
    if keyword.iskeyword(type_name):
        raise SyntaxError(f"Invalid keyword name: {type_name}")

# check kwargs are in the fields
# if it is in the fields assign into the fields
# if there is no raise an error


    code = f'''
class {type_name}:

    _fields = {field_names}
    _mutable = False

    def __init__(self, *args):
        self.args = args
        self.key_list = list({defaults}.keys())
        self.return_dict = dict()
        for field in self._fields:
            if field not in {defaults}.keys():
                raise SyntaxError("the field name is invalid")
        for keys in {defaults}.keys():
            if keys not in self._fields:
                raise SyntaxError("the field name is invalid")

        for i in range(len(self.key_list)):
            self.return_dict[self.key_list[i]] = self.args[i]
   
    def __repr__(self):
       return '{type_name}('+','.join(f"{{k}}={{v}}" for k, v in self.return_dict.items())+')'
    
    def __eq__(self, other):
        if not isinstance(other, {type_name}):
            raise TypeError('not a {type_name}')
        return self.return_dict == other.return_dict
       
    def _replace(self, **kwargs):
        for i in range(len(self._fields)):
            for key in kwargs.keys():
                if key == self._fields[i]:
                    self.return_dict[key] = kwargs[key]
        return '{type_name}('+','.join(f"{{k}}={{v}}" for k, v in self.return_dict.items())+')'
        
    def __getitem__(self, index):
        if index >= len(self._fields):
            raise IndexError("Index out of range")
        if type(index) is int:
            return self.return_dict[self._fields[index]]
        else:
            raise TypeError("the index is not int")
   
    def __contains__(self, item):
        for v in self.return_dict.values():
            if v == item:
                return True
        return False
    
    def _asdict(self):
        return ','.join(f"'{{k}}':{{v}}" for k, v in self.return_dict.items())
        
    def _make(iterable):
        return {type_name}(*iterable)
            
      
'''

    for i in field_names:
        code += f'''
    def get_{i}(self):
        return self.return_dict['{i}']
        '''

    namespace = {}
    exec(code, namespace)

    return namespace[type_name]

"""
coordinate = mynamedtuple('coordinate', ['x', 'y'])
#coordinate = mynamedtuple('coordinate', 'x,y', defaults = {'y':2})
print("coordinate리턴은: ", coordinate)
p = coordinate(3, 2)
print("p는:", p)
print("replace: ", p._replace(y=5))
print("get함수:", p.get_x())
print("p[0]:", p[1])
print("asdict:", p._asdict())
print("_make: ", coordinate._make((0,1)))
#origin = coordinate(0, 0)
#dif = repr(origin)
#yes = eval(dif)
#print("yes", yes.x)
#print("repr(origin)", repr(origin))
#print("여기", yes == origin)
#print("되나", origin.get_x())

origin = coordinate(0,0)
new_origin = origin._replace(y=5)
print(origin, new_origin)
"""