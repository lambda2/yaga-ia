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
        self.history = dict()
        self.server = False
        self.interactive = False
        self.exitRequired = False
        self.logs = []
        
    def reset(self):
        self.logs = []

    def __repr__(self):
        a = "Platform : {}\nLang : {}\n".format(
            self.platform, self.lang)
        if self.interactive:
            a = a + "[x] INTERACTIVE\n"
        if self.server:
            a = a + "[x] SERVEUR\n"
        a = a + "Verbose : {}\n".format(self.verbose)
        return a
