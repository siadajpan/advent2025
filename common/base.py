class TextBaseSolution:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self._data = self._read_data()

    @property
    def data(self) -> list[str]:
        return self._data

    def _read_data(self) -> list[str]:
        with open(self.file_name, "r") as f:
            return f.read().splitlines()

    def solve(self) -> tuple[str, str]:
        raise NotImplementedError