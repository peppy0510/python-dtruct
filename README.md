
## Installation

```bash
pip install git+http://muteklab.com:9000/root/python-dtruct.git
```

```bash
pip uninstall dtruct
```

## Example

```python
from dtruct import dtruct
```

```python
data = dtruct(a=(1, 2, 3), b=2)
data.get_dict()
>>> {'b': 2, 'a': (1, 2, 3)}
```

```python
data.set_dict({'b': 3, 'c': {'d': 4, 'e': ({'f': {'g': 5}},)}, 'h': (1, 2, 3)})
data.get_dict()
>>> {'a': (1, 2, 3), 'h': (1, 2, 3), 'c': {'d': 4, 'e': ({'f': {'g': 5}},)}, 'b': 3}
```

```python
data.c.e[0].get_dict()
>>> {'f': {'g': 5}}
```

```python
data.c.e[0].f.g
>>> 5
```

## Repository

```bash
git clone http://muteklab.com:9000/root/python-dtruct.git
```
