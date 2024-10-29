def main_loop():
    result = ''
    while(result != "quit"):    
        print("hello>", end='')
        input_line = input()
        the_command, args = parse_command(input_line)
        if is_legit(the_command):
            print(run_command(the_command, args))
        else: print(input_line + " --> is not a legit command")

def parse_command(some_input):
    input_items = some_input.split()
    first_item, rest_items = input_items[0], input_items[1:]
    return [first_item, rest_items]

def run_add_command(args):
    ints_args = [int(item) for item in args]
    return sum(ints_args)

def run_count_command(line):
    return len(line)

legit_commands = {'add': run_add_command,'count': run_count_command}

def is_legit(cmd):
    if cmd in legit_commands:
        return True
    else: 
        return False

def run_command(command, some_args):
    return legit_commands[command](some_args)

main_loop()