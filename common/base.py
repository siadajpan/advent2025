class TextBaseSolution:
    def __init__(self, file_name: str, split_by: str = "\n") -> None:
        self.file_name = file_name
        self._data = self._read_data(split_by)

    @property
    def data(self) -> list[str]:
        return self._data

    def _read_data(self, split_by: str = "\n") -> list[str]:
        with open(self.file_name, "r") as f:
            return f.read().split(split_by)
    
    def solve(self) -> tuple[str, str]:
        raise NotImplementedError