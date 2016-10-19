#! -*- encoding:utf-8 -*-
"""test for hello.py."""

import unittest

from hello import HelloWorld


class TestHelloWorld(unittest.TestCase):
    """test class for hello.HelloWorld."""

    def test_say_hello(self):
        """test function for say_hello."""
        hello = HelloWorld()
        self.assertEqual(type("Hello, World"), type(hello.say_hello("TK")))


def suite():
    """suite function."""
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestHelloWorld))
    return suite
