from dataclasses import dataclass

from environs import Env


@dataclass
class Config:
    token: str
    admin: int


def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        token=env.str('BOT_TOKEN'),
        admin=env.int('ADMIN_ID')
    )
