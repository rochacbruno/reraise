# reraise exceptions like a boss

```bash
$ pip install reraise
```

```python
import reraise

try:
    1 / 0
except ZeroDivisionError:
    reraise(ValueError("Can't divide by zero!"))


```

```python
import reraise

class MyCustomException(IOError):
    pass

try:
    open('file_not_exits')
except IOError:
    reraise(MyCustomException)
```