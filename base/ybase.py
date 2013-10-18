# -*- coding: utf-8 -*-

class YBase:
    """
    Cette classe va représenter une classe de base, que les autres vont hériter
    Ceci va nous pemettre de passer un contexte à toutes les classes
    """
    def __init__(self, ctx):
        """Constructeur de notre classe"""
        self.ctx = ctx
        self.__init_colors()
            
    def __init_colors(self):
        self._log_color = "\033[94m"
        self._alert_color = "\033[33m"
        self._error_color = "\033[91m"
        self._success_color = "\033[92m"
        self._reset_color = "\033[0m"

    def dbg(self, str_, level=0):
        col = self._log_color
        if level >= self.ctx.verbose:
            if level == 3:
                col = self._success_color
            elif level == 1:
                col = self._alert_color
            elif level == 2:
                col = self._error_color
            print("{}{}{}".format(col, str_, self._reset_color))

    def out(self, str_):
        print(str_)