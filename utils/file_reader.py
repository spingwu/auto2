import yaml
import os


class YamlReader:
    def __init__(self, yaml):
        if os.path.exists(yaml):
            self.yaml = yaml
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None

    @property
    def data(self):
        if self._data:
            return self._data
        else:
            with open(self.yaml, 'rb') as f:
                return list(yaml.safe_load_all(f))