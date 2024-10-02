from abc import abstractmethod


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
