
## Installation

```bash
pip install git+http://east-control.com:9000/pockestra/python-dtruct.git
```

```bash
pip uninstall dtruct
```

## Example

```python
from dtruct import dtruct
```

```python
data = dtruct(a=(1, 2, 3), b='2')
data.get_dict()
>>> {'b': '2', 'a': (1, 2, 3)}
```

```python
data = dtruct({'a': (1, 2, 3), 'b': '2'})
data.get_dict()
>>> {'b': '2', 'a': (1, 2, 3)}
```

```python
data.set_dict({'b': 3, 'c': {'d': '4', 'e': ({'f': {'g': 5}},)}, 'h': (1, 2, 3)})
data.get_dict()
>>> {'h': (1, 2, 3), 'b': 3, 'a': (1, 2, 3), 'c': {'d': '4', 'e': ({'f': {'g': 5}},)}}
```

```python
data.c.e[0].get_dict()
>>> {'f': {'g': 5}}
```

```python
data.c.e[0].f.g
>>> 5
```

```python
data.c.e[0].set_json('{"j": 5}')
data.c.e[0].get_json(sort_keys=True, indent=4, ensure_ascii=True)
>>> {
        "f": {
            "g": 5
        },
        "j": 5
    }
```

```python
data.get_compressed()
>>> b'eNqrVkpUslKINtRRMNJRMI7VUVBKAvKNgXQykK5WSgGSSiZKQH4qSF21UhpYOB1ImtbWxtYCJTKQDagFANurEok='
data.set_compressed(b'eNqrVkpUslKINtRRMNJRMI7VUVBKAvKNgXQykK5WSgGSSiZKQH4qSF21UhpYOB1ImtbWxtYCJTKQDagFANurEok=')
data.get_dict()
>>> {'h': (1, 2, 3), 'b': 3, 'a': (1, 2, 3), 'c': {'d': '4', 'e': ({'f': {'g': 5}},)}}
```

```python
data.set_dict({'a': 1}, recursive=False, deepcopy=True)
```

## Repository

```bash
git clone http://east-control.com:9000/pockestra/python-dtruct.git
```
