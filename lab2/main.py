from parser.parser import Parser
import sys


if __name__ == '__main__':
    if len(sys.argv) == 3:
        input_str = sys.argv[1]

        parser = Parser()

        tree = parser.parse(input_str, modification=sys.argv[2] == "true")
        output_str = str(tree)

        print(f'input   = {input_str}')
        print(f'output  = {output_str}')
        print(f'equals? - {input_str == output_str}')

        tree.to_dot().render('syntax-tree.gv', view=True, cleanup=True)
