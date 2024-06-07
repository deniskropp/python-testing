jobsNqueues
===========


## About

`jobsNqueues` is a python package that provides a simple way to manage and
execute jobs. It includes a basic job queue and a job scheduler.

## Development

```bash
  pip install -e .
```

## Usage

```python
  from jobsNqueues import Queue, Job

  queue = Queue()
  queue.add(Job(func=print, args=('hello',), kwargs={'end': '\n'}))
  queue.add(Job(func=print, args=('world',), kwargs={'end': '\n'}))

  while (not queue.empty()):
    job = queue.get()
    job.run()

```


## License

MIT License


## Author

[Denis Kropp](https://github.com/deniskropp)
