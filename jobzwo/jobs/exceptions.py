class Error(Exception):
    pass


class JobStatusError(Error):
    """Exception raised when the current state is illegal."""
    def __init__(self, message, job, current):
        self.message = message
        self.job = job
        self.current = current

    def __repr__(self):
        return self.message


class JobTransitionError(Error):
    """Exception raised when an application tries attempts to change
    status into illegal for current one.

    Current and rejected status can be read from `current` and `target`
    attributes
    """

    def __init__(self, message, job, current, target):
        self.message = message
        self.job = job
        self.current = current
        self.target = target

    def __repr__(self):
        return self.message
