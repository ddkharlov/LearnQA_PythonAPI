import pytest


class TestEx10:
    def test_length_of_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, f"Phrase is not small enough"
