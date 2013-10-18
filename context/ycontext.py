# -*- coding: utf-8 -*-


class YContext:
    """
    Cette classe va représenter un contexte, permettant au programme de savoir
    des informations tels que la langue ou la plateforme
    """
    def __init__(self):
        """Constructeur de notre classe"""
        self.platform = ["all"]
        self.lang = "fr"
        self.verbose = 4

    def __repr__(self):
        return "|\tplatform : {}\n| \tlang : {}".format(
            self.platform, self.lang)