# Module API


class Queue:
    def __init__(self):
        """
        Initialize a new Queue object.
        """
        self._data = []

    def push(self, item):
        """
        Add an item to the queue.
        """
        self._data.append(item)

    def pop(self):
        """
        Remove and return the item at the front of the queue.
        """
        return self._data.pop(0)

    def empty(self):
        """
        Return True if the queue is empty, False otherwise.
        """
        return len(self._data) == 0


class Job:
    def __init__(self, function, *args, **kwargs):
        """
        Initialize a new Job object.

        Args:
            function (callable): The function to execute as the task.
            *args: Positional arguments to pass to the function.
            **kwargs: Keyword arguments to pass to the function.
        """
        self._function = function
        self._args = args
        self._kwargs = kwargs

    def run(self):
        """
        Execute the task.
        """
        self._function(*self._args, **self._kwargs)


