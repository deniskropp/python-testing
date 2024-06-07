# jobsNqueues


## About

`jobsNqueues` is a python package that provides a simple way to manage and
execute jobs. It includes a basic queue and job object.


## Installation

To install the `jobsNqueues` package, you can use pip:

```bash
  pip install jobsNqueues
```

## Usage

```python
  from jobsNqueues import Queue, Job

  queue = Queue()
  queue.push(Job(print, 'hello', end='\n'))
  queue.push(Job(print, 'world', end='\n'))

  while (not queue.empty()):
    job = queue.pop()
    job.run()
```


## Development

```bash
  pip install -e .
```


## License

MIT License


## Author

[Denis Kropp](https://github.com/deniskropp)
