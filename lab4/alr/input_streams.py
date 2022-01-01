import codecs


class InputStream:
    def __init__(self, data: str):
        self.strdata = data
        self._index = 0

    @property
    def source(self):
        return self.strdata

    @property
    def index(self):
        return self._index

    @property
    def is_consumed(self):
        return self._index == len(self.strdata)

    def consume(self, cnt: int):
        self._index += cnt

    def get(self):
        return self.strdata[self._index:]

    def __str__(self):
        return self.strdata


class FileStream(InputStream):
    def __init__(self, fileName: str, encoding: str = 'ascii', errors: str = 'strict'):
        super().__init__(self._readDataFrom(fileName, encoding, errors))

    def _readDataFrom(self, fileName: str, encoding: str, errors: str = 'strict'):
        # read binary to avoid line ending conversion
        with open(fileName, 'rb') as file:
            bytes = file.read()
            return codecs.decode(bytes, encoding, errors)
