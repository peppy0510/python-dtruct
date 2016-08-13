# encoding: utf-8


'''
author: Taehong Kim
email: peppy0510@hotmail.com
'''


import json
import zlib
import base64


try:
    basestring = eval('basestring')
except:
    basestring = str


def compress_dict(data, level=9):
    if data is None:
        return None
    return base64.b64encode(zlib.compress(json.dumps(data), level))


def decompress_dict(data):
    if data is None:
        return None
    return json.loads(zlib.decompress(base64.b64decode(data)))


class dtruct(object):

    def __init__(self, *args, **kwargs):
        for arg in args:
            # self.__dict__.update(arg)
            self.set_dict(arg)
        # self.__dict__.update(kwargs)
        self.set_dict(kwargs)

    def items(self):
        return self.__dict__.items()

    def values(self):
        return self.__dict__.values()

    def keys(self):
        return self.__dict__.keys()

    def get_dict(self, sort_keys=True, recursive=True):
        '''
        dtruct to dict.
        ex) x.get_dict()
        '''
        def struct_to_dict(data, recursive=True):
            if not isinstance(data, dtruct):
                return data
            result = dict()
            for key in data.keys():
                result[key] = eval('data.%s' % (key))
                if recursive and isinstance(result[key], dtruct):
                    result[key] = struct_to_dict(result[key], recursive=recursive)
                elif recursive and isinstance(result[key], list):
                    result[key] = [struct_to_dict(v, recursive=recursive)
                                   for v in result[key]]
                elif recursive and isinstance(result[key], tuple):
                    result[key] = tuple([struct_to_dict(v, recursive=recursive)
                                         for v in result[key]])
            return result

        return struct_to_dict(self, recursive)

    def set_dict(self, data, recursive=True):
        '''
        dict to dtruct.
        ex) x.set_dict({'a': 1, 'b': {'c': 2}})
        '''
        def dict_to_struct(data, recursive=True):

            if isinstance(data, int):
                return data

            if isinstance(data, float):
                return data

            if isinstance(data, basestring):
                return data

            if isinstance(data, list):
                return [dict_to_struct(v, recursive=recursive) for v in data]

            if isinstance(data, tuple):
                return tuple([dict_to_struct(v, recursive=recursive) for v in data])

            if isinstance(data, dtruct):
                return data

            # assume data is dict
            result = dtruct()
            for key in data.keys():
                if recursive and isinstance(data[key], dict):
                    data[key] = dict_to_struct(data[key],
                                               recursive=recursive)
                elif recursive and isinstance(data[key], list):
                    data[key] = [dict_to_struct(v, recursive=recursive)
                                 for v in data[key]]
                elif recursive and isinstance(data[key], tuple):
                    data[key] = tuple([dict_to_struct(v, recursive=recursive)
                                       for v in data[key]])
                setattr(result, key, data[key])
            return result

        for key in data.keys():
            if recursive and isinstance(data[key], dict):
                data[key] = dict_to_struct(data[key], recursive=recursive)
            setattr(self, key, data[key])

    def get_json(self, sort_keys=True, indent=4):
        return json.dumps(self.get_dict(), sort_keys=sort_keys, indent=indent)

    def set_json(self, data):
        self.set_dict(json.loads(data))

    def get_compressed(self, sort_keys=True, level=9):
        data = base64.b64encode(
            zlib.compress(
                json.dumps(
                    self.get_dict(),
                    sort_keys=sort_keys
                ).encode('utf-8'), level
            )
        )
        return data

    def set_compressed(self, data):
        data = json.loads(
            zlib.decompress(
                base64.b64decode(data)
            ).decode('utf-8')
        )
        self.set_dict(data)


def __test__():
    pad = 50

    data = dtruct(a=(1, 2, 3), b='2')
    print('data.get_dict()'.ljust(pad), data.get_dict())
    data = dtruct({'a': (1, 2, 3), 'b': '2'})
    print('data.get_dict()'.ljust(pad), data.get_dict())
    data.set_dict({
        'b': 3,
        'c': {
            'd': '4',
            'e': ({'f': {'g': 5}},)
        },
        'h': (1, 2, 3)
    })

    print('data.get_dict()'.ljust(pad),
          data.get_dict())

    print('data.c.e[0].get_dict()'.ljust(pad),
          data.c.e[0].get_dict())

    print('data.c.e[0].f.g'.ljust(pad),
          data.c.e[0].f.g)

    data.c.e[0].set_json('{"j": 5}')

    print('data.c.e[0].get_json(sort_keys=True, indent=4)'.ljust(pad),
          data.c.e[0].get_json(sort_keys=True, indent=4))

    c = data.get_compressed()
    print('data.get_compressed()'.ljust(pad), c)
    print('data.set_compressed(%s)' % (c))
    data.set_compressed(c)

    print('data.get_dict()'.ljust(pad), data.get_dict())


if __name__ == '__main__':
    __test__()
