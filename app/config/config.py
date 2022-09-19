import os

from envyaml import EnvYAML


class Config:

    def __init__(self):
        config_file_path = os.path.join(
            os.getcwd(),
            'app',
            'config',
            'config.yml'
        )
        self.config_file = EnvYAML(config_file_path)

    def get(self, key: str, default_value: str = None) -> str:
        """Get env variable value following the structure
        of config yaml file.

        Args:
            -   key: str = Env variable key.

        Returns:
            -   str: Value of the provided env variable.
        """
        return self.config_file.get(key, default_value)
