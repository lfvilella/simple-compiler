import pytest

from predictive_parser.simple_predictive_parser import SimplePredictiveParser


class TestPredictiveParser:
    def test_sum_ids(self):
        spp = SimplePredictiveParser(input='id+id')
        spp.start()

        assert spp.success_state

    def test_multiply_ids(self):
        spp = SimplePredictiveParser(input='id*id')
        spp.start()

        assert spp.success_state

    def test_subtract_ids_raises(self):
        spp = SimplePredictiveParser(input='id-id')

        with pytest.raises(ValueError):
            spp.start()

        assert not spp.success_state

    def test_divide_ids_raises(self):
        spp = SimplePredictiveParser(input='id/id')

        with pytest.raises(ValueError):
            spp.start()

        assert not spp.success_state

    def test_complete_math_expression(self):
        spp = SimplePredictiveParser(
            input='(id*id)+((id+id)*id+(id*id))*(id+(id*id+id*(id*id)))'
        )
        spp.start()

        assert spp.success_state

    def test_invalid_terminals_raises(self):
        spp = SimplePredictiveParser(input='invalid+id')

        with pytest.raises(ValueError):
            spp.start()

        assert not spp.success_state

    def test_invalid_expression_raises(self):
        spp = SimplePredictiveParser(input='+idid*')

        with pytest.raises(ValueError):
            spp.start()

        assert not spp.success_state
