from collections import deque

try:
    from . import table
except:
    import table


EOF = '$'


class SimplePredictiveParser:
    def __init__(self, input):
        self.input = self._inject_eof(content=input)
        self._input = list(self.input)

        self._stack = self._get_stack()
        self._terminal = set('id')
        self._nonterminal = set(table.PARSING_TABLE.keys())

        self.success_state = False

    def _inject_eof(self, content: str) -> str:
        """Inject End Of File

        Args:
            content (str): 'id+id'

        Returns:
            str: 'id+id$'
        """
        return content + EOF

    def _get_stack(self) -> deque:
        _stack = deque()
        _stack.append(EOF)
        _stack.append(table.START_SYMBOL)
        return _stack

    def start(self):
        stack_symbol = self._stack.pop()
        while stack_symbol != EOF:
            idx = 0

            if stack_symbol == "'":
                tmp = stack_symbol
                stack_symbol = self._stack.pop()
                stack_symbol += tmp

            print(stack_symbol)
            if (
                stack_symbol == 'id'
                or stack_symbol == '+'
                or stack_symbol == '*'
                or stack_symbol == '('
                or stack_symbol == ')'
            ):
                self._input.pop(0)
                if stack_symbol == 'id':
                    self._input.pop(0)

                stack_symbol = self._stack.pop()

            if stack_symbol not in self._nonterminal:
                raise ValueError(
                    f'The stack symbol "{stack_symbol}" is a unexpected terminal.'
                )

            char = self._input[idx]
            if char == 'i':
                idx += 1
                char += self._input[idx]

            _derivate = self.derivative(stack_symbol=stack_symbol, symbol=char)
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

        self.success_state = True

    def derivative(self, stack_symbol: str, symbol: str):
        _derivate = table.PARSING_TABLE[stack_symbol].get(symbol)
        if not _derivate:
            raise ValueError(
                f'The stack symbol "{stack_symbol}" has no derivation to "{symbol}"'
            )

        return _derivate


if __name__ == '__main__':
    spp = SimplePredictiveParser(input='id+id')
    spp.start()
