from core.classes.scrappers.edge_scrapper import EdgeScrapper
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Various options')

    parser.add_argument('--headless', dest='headless',
                        help='Whether the scrapper should run headless or not', action='store_true')

    parser.add_argument('--disable-gpu', dest='disable_gpu',
                        help='Whether the scrapper should disable the usage of gpu or not',
                        action='store_true')

    parser.add_argument('--no-start-maximized', dest='start_maximized',
                        help='Whether the Window should start maximized or not',
                        action='store_false')

    args = parser.parse_args()
    scrapper = EdgeScrapper()
    scrapper.setUp(**vars(args))
    scrapper.navigate_to('https://www.google.com')
    scrapper.close()
