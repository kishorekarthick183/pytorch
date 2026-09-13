class FileManager:
    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"Closed file: {self.filename}")
        # Return False so exceptions raised inside the block aren't swallowed
        return False


# Usage
with FileManager("sample.txt", "w") as f:
    f.write("Hello, World!")