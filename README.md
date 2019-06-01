# Global problems overview

These tools are generating charts which show dependencies of global problems. They don't show severity of problems but rather how they linked together and form multiple positive feedback loops.

Note: keep in mind that work is in progress.

### Requirements

Scripts work under Linux but with some effort can be run in Windows and cygwin too.

1. Python3
2. Python3 libraries:
    1. Numpy
    2. Matplotlib
3. graphviz
4. Any image viewer you like

### Generating global chart
```bash
/bin/bash compile.sh global.dot
```

### Generating pie chart
```python
python3 pie.py
...or
python3 pie-big.py
```

## License
MIT
