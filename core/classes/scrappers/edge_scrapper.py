from core.classes.scrappers.base_scrapper import Scrapper
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class EdgeScrapper(Scrapper):
    def setUp(self, **kwargs):
        from selenium.webdriver.edge.options import Options

        options = Options()

        if kwargs.get('headless'):
            options.add_argument('--headless')

        if kwargs.get('start_maximized'):
            options.add_argument('--start-maximized')

        self.driver = webdriver.Edge(options=options)

    def navigate_to(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.TAG_NAME, 'body'))
        )

    def close(self):
        self.driver.quit()
