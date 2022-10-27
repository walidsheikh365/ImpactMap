from dash.testing.application_runners import import_app
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.relative_locator import By
from selenium.webdriver.support import expected_conditions as EC

# RUN FROM TERMINAL WITH
# python -m pytest --cov-report term-missing --cov=app


def test_mete001_h1_alt_equals(dash_duo):
    """
    GIVEN the app is running
    WHEN the webpage is available
    THEN the element subtitle should include the text
    'A Dash app created by Group 1 for COMP0034'
    """
    app = import_app(app_file='app.meteorite_app')

    dash_duo.start_server(app)

    dash_duo.wait_for_element("#subtitle", timeout=120)

    h1_alt = dash_duo.find_element("#subtitle").text

    assert h1_alt.casefold() ==\
           "A Dash app created by Group 1 for COMP0034".casefold()

'''
(UNUSED)

def test_mete002_slider_default(dash_duo):
    """
    GIVEN the app is running
    WHEN the slider for the mass histogram is located
    THEN the value by default should be set to 9 (All)
    """
    app = import_app(app_file='app.meteorite_app')

    dash_duo.start_server(app)

    dash_duo.wait_for_element("#histogram_mass", timeout=120)

    WebDriverWait(dash_duo.driver, 10).until(
        EC.presence_of_element_located((By.ID, "histogram_mass"))
        )

    assert dash_duo.driver.find_element(
            By.XPATH,
            '//*[@id="histogram_mass"]/div[2]/div/div/svg[1]/g[4]/g[1]/g[11]/g[4]/text'
        ).text == "60M"
    
    #assert dash_duo.driver.find_element("#rc_slider_handle").  == "9"
    
    # NOT WORKING: Couldn't locate element
'''