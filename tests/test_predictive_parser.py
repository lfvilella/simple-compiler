from pathlib import Path

import pytest

from predictive_parser.simple_predictive_parser import SimplePredictiveParser


class TestPredictiveParserWithFile:
    def test_instantiate_with_invalid_filepath(self):
        with pytest.raises(ValueError):
            SimplePredictiveParser(filepath='fake_filepath/file.txt')

    def test_valid_input(self):
        spp = SimplePredictiveParser(
            filepath=f'{Path(__file__).parent.resolve()}/payloads/predictive_parser/valid_input.txt'  # noqa: E501
        )
        spp.start()

        assert spp.success_state

    def test_sync_error_input(self):
        spp = SimplePredictiveParser(
            filepath=f'{Path(__file__).parent.resolve()}/payloads/predictive_parser/sync_error_input.txt'  # noqa: E501
        )
        spp.start()

        assert not spp.success_state

    def test_fatal_error_input(self):
        spp = SimplePredictiveParser(
            filepath=f'{Path(__file__).parent.resolve()}/payloads/predictive_parser/fatal_error_input.txt'  # noqa: E501
        )
        with pytest.raises(ValueError):
            spp.start()

        assert not spp.success_state


class TestPredictiveParser:
    def test_instantiate_without_params_raises(self):
        with pytest.raises(AttributeError):
            SimplePredictiveParser(input=None, filepath=None)

    def test_instantiate_with_two_params_raises(self):
        with pytest.raises(AttributeError):
            SimplePredictiveParser(input='(id+id)', filepath='fake_filepath')

    def test_sum_ids(self):
        spp = SimplePredictiveParser(input='(id+id)')
        spp.start()

        assert spp.success_state

    def test_multiply_ids(self):
        spp = SimplePredictiveParser(input='id*id')
        spp.start()

        assert spp.success_state

    def test_subtract_ids_raises_fatal_error(self):
        spp = SimplePredictiveParser(input='id-id')

        with pytest.raises(ValueError):
            spp.start()

        assert not spp.success_state

    def test_divide_ids_raises_fatal_error(self):
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

    def test_invalid_terminals_raises_fatal_error(self):
        spp = SimplePredictiveParser(input='invalid+id')

        with pytest.raises(ValueError):
            spp.start()

        assert not spp.success_state

    def test_invalid_expression_raises_fatal_error(self):
        spp = SimplePredictiveParser(input='+idid*')

        with pytest.raises(ValueError):
            spp.start()

        assert not spp.success_state

    def test_empty_raises_sync_error(self):
        spp = SimplePredictiveParser(input='')
        spp.start()

        assert not spp.success_state

    def test_sum_raises_sync_error(self):
        spp = SimplePredictiveParser(input=')id+id')
        spp.start()

        assert not spp.success_state

    def test_raises_sync_error(self):
        spp = SimplePredictiveParser(input=')id+id**')
        spp.start()

        assert not spp.success_state
