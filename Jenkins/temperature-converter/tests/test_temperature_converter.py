
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from temperature_converter import fahrenheit_to_celsius, celsius_to_fahrenheit

def test_fahrenheit_to_celsius_boiling():
    assert round(fahrenheit_to_celsius(212), 2) == 100.0

def test_fahrenheit_to_celsius_freezing():
    assert round(fahrenheit_to_celsius(32), 2) == 0.0

def test_celsius_to_fahrenheit_body_temp():
    assert round(celsius_to_fahrenheit(37), 2) == 98.6

def test_celsius_to_fahrenheit_freezing():
    assert round(celsius_to_fahrenheit(0), 2) == 32.0