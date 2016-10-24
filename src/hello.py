#!/usr/bin/env python
#! -*- encoding:utf-8 -*-
"""Hello World."""


class HelloWorld(object):
    """varius hello world function class."""

    def say_hello(self, country):
        """return hello world in each country."""
        if country == 'JA':
            return "これが世界だ..."
        elif country == 'US':
            return "Hello World!!! Yeahhhh!!!!"
        elif country == 'UK':
            return "Could you say Hello World, please."
        elif country == 'FR':
            return "Bonjour! Enchante, le monde."
        else:
            return "Hello, World"
