import pytest

from jobsNqueues import Queue, Job


def test_queue_push():
    q = Queue()
    q.push(1)
    assert q.size() == 1
    q.push(2)
    assert q.size() == 2

def test_queue_pop():
    q = Queue()
    q.push(1)
    q.push(2)
    assert q.pop() == 1
    assert q.pop() == 2
    assert q.empty()

def test_queue_empty():
    q = Queue()
    assert q.empty()
    q.push(1)
    assert not q.empty()
    q.pop()
    assert q.empty()

def test_queue_size():
    q = Queue()
    assert q.size() == 0
    q.push(1)
    assert q.size() == 1
    q.push(2)
    assert q.size() == 2
    q.pop()
    assert q.size() == 1


def test_job_init():
    job = Job('test', 1)
    assert job._function == 'test'
    assert job._args == (1,)
    assert job._kwargs == {}

def test_job_run():
    result = []
    def sample_function(x, y):
        result.append(x + y)
    job = Job(sample_function, 1, 2)
    job.run()
    assert result == [3]



if __name__ == "__main__":
    pytest.main()
