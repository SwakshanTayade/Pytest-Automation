import os
import pytest
from datetime import datetime

from selenium import webdriver
driver = None

# config options adoption/ registration
def pytest_addoption(parser):
    parser.addoption(
        "--browsername", 
        action="store", 
        default="chrome", 
        help="Specify a name for the test run (default: default_name)"
    )
@pytest.fixture(scope="class")
def browserInvoke(request):
    global driver
    print("Broswer Initiated")
    browser_name =  request.config.getoption("browsername")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__),'report')
            file_name = os.path.join(reports_dir,report.nodeid.replace("::","_") + ".png")
            print("File name is "+file_name)
            _capture_screenshot(file_name)
            if file_name:               
                html = (f'<div>'f'<img src="{file_name}" alt="screenshot" 'f'style="width:304px; height:228px;" 'f'onclick="window.open(this.src)" align="right" />'f'</div>')
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(filename):
    driver.get_screenshot_as_file(filename)
