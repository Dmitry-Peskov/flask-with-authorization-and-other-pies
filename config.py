from dataclasses import dataclass
import os


@dataclass
class config:

    @dataclass
    class database:
        dsn: str = "sqlite:///web_portal_database.db"

    @dataclass
    class app:
        host: str = "localhost"
        port: int = 8000
        debug: bool = True

    @dataclass
    class project:
        secret_key: bytes = os.urandom(32)
