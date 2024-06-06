from jobsNqueues import Queue, Job


def test_queue():
    q = Queue()
    assert q.empty()
    q.push(1)
    assert q.size() == 1
    assert not q.empty()
    assert q.pop() == 1
    assert q.empty()

def test_job():
    job = Job('test', 1)
    assert job.name == 'test'
    assert job.priority == 1

def test_job_queue():
    q = Queue()
    q.push(Job('a', 1))
    q.push(Job('b', 2))
    q.push(Job('c', 3))
    assert q.pop().name == 'b'

