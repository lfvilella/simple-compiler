from pathlib import Path
from collections import deque


from . import table


class SimplePredictiveParser:
    def __init__(self, input: str = None, filepath: str = None):
        if input is None and not filepath:
            raise AttributeError('One of the parameters must be informed')

        if input and filepath:
            raise AttributeError('Only one of the parameters must be informed')

        if filepath:
            filepath = Path(filepath)
            if not filepath.is_file():
                raise ValueError(
                    f'The filepath "{filepath}" file does not exist or is not a file'  # noqa: E501
                )

            with open(filepath) as file:
                input = file.read()
                input = input.replace('\n', '')

        self.input = self._inject_eof(content=input)
        self._input = list(self.input)

        self._stack = self._get_stack()
        self._sync_erros = []

        self.success_state = False

    def _inject_eof(self, content: str) -> str:
        """Inject End Of File

        Args:
            content (str): 'id+id'

        Returns:
            str: 'id+id$'
        """
        return content + table.EOF

    def _get_stack(self) -> deque:
        _stack = deque()
        _stack.append(table.EOF)
        _stack.append(table.START_SYMBOL)
        return _stack

    def start(self):
        stack_symbol = self._stack.pop()
        while stack_symbol != table.EOF:
            idx = 0

            if stack_symbol == "'":
                tmp = stack_symbol
                stack_symbol = self._stack.pop()
                stack_symbol += tmp

            if stack_symbol in table.TERMINAL:
                self._input.pop(0)
                if stack_symbol == 'id':
                    self._input.pop(0)

                stack_symbol = self._stack.pop()

            if stack_symbol not in table.NONTERMINAL:
                raise ValueError(
                    f'The stack symbol "{stack_symbol}" is a unexpected terminal.'  # noqa: E501
                )

            char = self._input[idx]
            if char == 'i':
                idx += 1
                char += self._input[idx]

            _derivate = self.derivative(stack_symbol=stack_symbol, symbol=char)
            if _derivate == table.SYNC_ERROR:
                self._sync_erros.append(_derivate)
                stack_symbol = self._stack.pop()
                continue

            if _derivate == table.EMPTY:
                stack_symbol = self._stack.pop()
                continue

            next_alredy_added = False
            reversed_derivate = list(reversed(_derivate))
            for idx, item in enumerate(reversed_derivate):
                if next_alredy_added:
                    next_alredy_added = False
                    continue

                if item == "'":
                    item = f"{reversed_derivate[idx + 1]}'"
                    next_alredy_added = True

                if item == 'i':
                    item = 'id'

                elif item == 'd':
                    continue

                self._stack.append(item)

            # if error.type == 'fatal_error':
            #     raise SystemError(error.description)

            # elif error.type == 'sync':
            #     pass

            stack_symbol = self._stack.pop()

        self.success_state = True if not self._sync_erros else False

    def derivative(self, stack_symbol: str, symbol: str):
        _derivate = table.PARSING_TABLE[stack_symbol].get(symbol)
        if not _derivate or _derivate == table.FATAL_ERROR:
            raise ValueError(
                f'The stack symbol "{stack_symbol}" has no derivation to "{symbol}"'  # noqa: E501
            )

        return _derivate


if __name__ == '__main__':
    spp = SimplePredictiveParser(input='id+id')
    spp.start()
