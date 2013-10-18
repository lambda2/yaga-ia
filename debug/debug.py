# -*- coding: utf-8 -*-

gdebug = True
_log_color = "\033[94m"
_alert_color = "\033[33m"
_error_color = "\033[91m"
_success_color = "\033[92m"
_reset_color = "\033[0m"

def dbg(str, level=0):
    col = _log_color
    if gdebug:
        if level == -1:
            col = _success_color
        elif level == 1:
            col = _alert_color
        elif level == 2:
            col = _error_color
        print("{}{}{}".format(col, str, _reset_color))