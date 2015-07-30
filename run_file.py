"""Run motor program from given file.

Usage: `sudo python3 run_file.py FILE

FILE is a list of commands in JSON format.

Valid commands are:
 * "repeat", which takes a "repeats" parameter and list of subcommands
 * "move", which takes "position" and "speed" parameters
 * "comment", which takes a "comment" parameter

See example_prog.json as an example

Copyright (C) 2015 Tom Oakley
MIT licence
"""

import json
import logging
import sys

import motor


def execute(step):
    """Execute the program step."""

    command = step['command']

    if command == 'repeat':
        n_repeats = step['repeats']

        if n_repeats < 0:
            # Loop indefinitely
            logging.warning('Entering infinite loop')

            while True:
                for sub_step in step['steps']:
                    execute(sub_step)

        # 0 or more repeats requested
        for repeat in range(n_repeats):
            for sub_step in step['steps']:
                execute(sub_step)

    elif command == 'move':
        mtr.drive(step['duty'], step['time'])

    elif command == 'comment':
        logging.info(step['comment'])

    else:
        raise ValueError('Command {} not expected'.format(command))


if __name__ == '__main__':
    log_fmt = '%(asctime)s %(levelname)-8s %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=log_fmt)

    mtr = motor.Motor()

    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    with open(sys.argv[1]) as f:
        program = json.load(f)

    for step in program:
        execute(step)
