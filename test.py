import random

import main


def run_case(test_input):
    input_value = test_input
    output = []

    def mock_input(s):
        output.append(s)
        return input_value.pop(0)

    main.input = mock_input
    main.print = lambda s: output.append(s)

    main.main()
    return output


def test_simple():
    output = run_case(['2'])

    assert output == ['Usage: [-C (default)|-F] degrees\n', 'You entered:\t2.0 °C', 'Result:\t35.600 °F']


def test_not_enough_arguments():
    output = run_case([''])

    assert output == ['Usage: [-C (default)|-F] degrees\n', 'Error! Not enough arguments',
                      'Usage: [-C (default)|-F] degrees\n']


def test_incorrect_arguments():
    output = run_case(random.choice([['-С'], ['-Ф'], ['-F -C'], ['Degree']]))

    assert output == ['Usage: [-C (default)|-F] degrees\n', 'Error! Incorrect argument']


def test_unsupported_scale():
    output = run_case(['-K 2'])

    assert output == ['Usage: [-C (default)|-F] degrees\n', 'Error! Unsupported scale',
                      'Usage: [-C (default)|-F] degrees\n']


def test_fahrenheit():
    output = run_case(['-F 2'])

    assert output == ['Usage: [-C (default)|-F] degrees\n', 'You entered:\t2.0 °F', 'Result:\t-16.667 °С']


def test_celsius():
    output = run_case(['-C 2'])

    assert output == ['Usage: [-C (default)|-F] degrees\n', 'You entered:\t2.0 °C', 'Result:\t35.600 °F']


def test_multiple_celsius():
    output = run_case(['-C 2 3456 -789 0'])

    assert output == ['Usage: [-C (default)|-F] degrees\n', 'You entered:\t2.0 °C', 'Result:\t35.600 °F',
                      'You entered:\t3456.0 °C', 'Result:\t6252.800 °F', 'You entered:\t-789.0 °C',
                      'Result:\t-1388.200 °F', 'You entered:\t0.0 °C', 'Result:\t32.000 °F']


def test_multiple_fahrenheit():
    output = run_case(['-F 2 3456 -789 0'])

    assert output == ['Usage: [-C (default)|-F] degrees\n', 'You entered:\t2.0 °F', 'Result:\t-16.667 °С',
                      'You entered:\t3456.0 °F', 'Result:\t1902.222 °С', 'You entered:\t-789.0 °F',
                      'Result:\t-456.111 °С', 'You entered:\t0.0 °F', 'Result:\t-17.778 °С']
