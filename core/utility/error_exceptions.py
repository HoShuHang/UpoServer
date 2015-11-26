from rest_framework import status


class Error(Exception):
    def __init__(self, message="unknown error!", status_code=status.HTTP_400_BAD_REQUEST):
        self._message = str(message)
        self._status_code = status_code

    @property
    def message(self):
        return self._message

    @property
    def status_code(self):
        return self._status_code


class FbTokenExistedError(Error):
    def __init__(self):
        super(FbTokenExistedError, self).__init__("fb token has registered!", status.HTTP_409_CONFLICT)


class ParameterError(Error):
    def __init__(self):
        super(ParameterError, self).__init__("parameter missing!", status.HTTP_403_FORBIDDEN)
