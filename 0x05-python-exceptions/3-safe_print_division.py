#!/usr/bin/python3
def afe_print_division(a, b):
        try:
            div = a / b
        except (TypeError, ZeroDivisionError):
            div = None
        finally:
            print("Inside result: {}".format(div))
        return (div)
