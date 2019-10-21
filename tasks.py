class Task(object):
    def __init__(self):
        self.lines = []

    def add(self, line):
        self.lines.append(line)


class TaskList(object):
    def __init__(self):
        self.list = []

    def add(self, task):
        self.list.append(task)
