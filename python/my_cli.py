def main_loop():
    result = ''
    while(result != "quit"):    
        print("hello>", end='')
        input_line = input()
        the_command, args = find_command(input_line)
        run_command(the_command, args)

def find_command(input_line):
    # add command:
    #    sum 3 5 4 18
    # count command:
    #    count hello goodbye birthday
    first_item, rest_items = input_line[0], input_line[1:]
    return [first_item, rest_items]


def run_command(command, args):
    legit_commands = ['add', 'count']
    if command in legit_commands:
        if command == legit_commands[0]:
            return run_add_command(command, args)
        elif command == legit_commans[1]:
            return run_count_command(command, args)
    else: return "The command should be add or count"

def run_add_command(command):
    pass

def run_count_command(command):
    pass

main_loop()