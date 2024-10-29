def main_loop():

    while(True):    
        print("hello>", end='')
        input_line = input()
        if input_line:
            if input_line != "quit":
                the_command, args = parse_command(input_line)
            else: break
        else: continue
        if is_legit(the_command):
            print(run_command(the_command, args))
        else: print(input_line + " --> is not a legit command")

def parse_command(user_input):
    input_items = user_input.split()
    first_item, rest_items = input_items[0], input_items[1:]
    return [first_item, rest_items]

def run_add_command(user_args):
    ints_args = [int(item) for item in user_args]
    return sum(ints_args)

def run_count_command(user_input):
    return len(user_input)

legit_cmds = { 'add': run_add_command, 'count': run_count_command }

def is_legit(user_cmd):
    if user_cmd in legit_cmds:
        return True
    else: 
        return False

def run_command(user_cmd, user_args):
    return legit_cmds[user_cmd](user_args)

main_loop()