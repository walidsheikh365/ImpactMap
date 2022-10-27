import pytest
from dash.testing.application_runners import import_app
from selenium.webdriver.chrome.options import Options

# Setup pytest for continuous integration

def pytest_setup_options():
    options = Options()

    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')

    return options


# Add simple fixture testing app launch

@pytest.fixture(autouse=True)
def run_meteorite_app(dash_duo):
    app = import_app("app.meteorite_app")
    yield dash_duo.start_server(app)