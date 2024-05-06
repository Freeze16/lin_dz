from dataclasses import dataclass

from environs import Env


@dataclass
class Config:
    token: str
    prefix: str
    admin: int


def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        token=env.str('BOT_TOKEN'),
        prefix=env.str('BOT_PREFIX'),
        admin=env.int('ADMIN_ID')
    )