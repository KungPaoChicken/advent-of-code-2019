from intcode_computer import str_to_program, parse_intcode

program = str_to_program(open("day5-input.txt").read())

parse_intcode(program.copy(), 0, [1], disable_jumps=True)
parse_intcode(program.copy(), 0, [5])
