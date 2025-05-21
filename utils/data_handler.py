import json, yaml, posixpath
import pandas as pd
from io import StringIO

class DataHandler:
    def __init__(self, filesystem, root_path):
        self.filesystem = filesystem
        self.root_path = root_path

    def join(self, *args):
        return posixpath.join(*args)

    def _resolve_path(self, relative_path):
        return self.join(self.root_path, relative_path)

    def exists(self, relative_path):
        full_path = self._resolve_path(relative_path)
        return self.filesystem.exists(full_path)

    def read_text(self, relative_path):
        """
        Read the contents of a text file.
        Tries UTF-8 first; if that fails, falls back to latin1.
        """
        full_path = self._resolve_path(relative_path)
        try:
            with self.filesystem.open(full_path, "r", encoding="utf-8") as f:
                return f.read()
        except UnicodeDecodeError:
            with self.filesystem.open(full_path, "r", encoding="latin1") as f:
                return f.read()

    def read_binary(self, relative_path):
        full_path = self._resolve_path(relative_path)
        with self.filesystem.open(full_path, "rb") as f:
            return f.read()

    def write_text(self, relative_path, content):
        """
        Write text content to a file using UTF-8 encoding.
        """
        full_path = self._resolve_path(relative_path)
        with self.filesystem.open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

    def write_binary(self, relative_path, content):
        full_path = self._resolve_path(relative_path)
        with self.filesystem.open(full_path, "wb") as f:
            f.write(content)

    def load(self, relative_path, initial_value=None, **load_args):
        if not self.exists(relative_path):
            if initial_value is not None:
                return initial_value
            raise FileNotFoundError(f"File does not exist: {relative_path}")

        ext = posixpath.splitext(relative_path)[-1].lower()
        if ext == ".json":
            return json.loads(self.read_text(relative_path))
        elif ext in [".yaml", ".yml"]:
            return yaml.safe_load(self.read_text(relative_path))
        elif ext == ".csv":
            return pd.read_csv(StringIO(self.read_text(relative_path)), **load_args)
        elif ext == ".txt":
            return self.read_text(relative_path)
        else:
            return self.read_binary(relative_path)

    def save(self, relative_path, content):
        full_path = self._resolve_path(relative_path)
        parent_dir = posixpath.dirname(full_path)

        if not self.filesystem.exists(parent_dir):
            self.filesystem.mkdirs(parent_dir, exist_ok=True)

        ext = posixpath.splitext(relative_path)[-1].lower()

        if isinstance(content, pd.DataFrame) and ext == ".csv":
            self.write_text(relative_path, content.to_csv(index=False))
        elif isinstance(content, (dict, list)) and ext == ".json":
            self.write_text(relative_path, json.dumps(content, indent=4))
        elif isinstance(content, (dict, list)) and ext in [".yaml", ".yml"]:
            self.write_text(relative_path, yaml.dump(content, default_flow_style=False))
        elif isinstance(content, str) and ext == ".txt":
            self.write_text(relative_path, content)
        elif isinstance(content, bytes):
            self.write_binary(relative_path, content)
        else:
            raise ValueError(f"Unsupported content type for extension {ext}")


