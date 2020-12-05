import os
from dotenv import load_dotenv

from feather_simple_api.core import create_app

load_dotenv()

app = create_app(os.environ)

# import route back
from .routes import app  # noqa: F401, E402
