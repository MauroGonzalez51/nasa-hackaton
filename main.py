from abc import abstractmethod
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import argparse


class Scrapper(object):
    @abstractmethod
    def setUp(self, **kwargs):
        pass

    @abstractmethod
    def navigate_to(self):
        pass

    @abstractmethod
    def close(self):
        pass


class EdgeScrapper(Scrapper):
    def setUp(self, **kwargs):
        from selenium.webdriver.edge.options import Options

        options = Options()

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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Various options')

    parser.add_argument('--headless', dest='headless',
                        help='Whether the scrapper should run headless or not', default=True, nargs='?')

    parser.add_argument('--disable-gpu', dest='disable_gpu',
                        help='Whether the scrapper should disable the usage of gpu or not', default=False, nargs='?')

    parser.add_argument('--start-maximized', dest='start_maximized',
                        help='Whether the Window should start maximized or not', default=False, nargs='?')

    args = parser.parse_args()
    scrapper = EdgeScrapper()
    scrapper.setUp(**vars(args))
    scrapper.navigate_to('https://www.google.com')
    scrapper.close()
