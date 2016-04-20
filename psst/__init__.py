import random


def random_password(choices, length):
    """ Create Random strings

    The random string is created out of the set of `string.ascii_letters` and `string.digits`.

    Args:
        length -- the length of the new random string

    Returns:
        A random string cosisting out of ascii letters and the decimal digits.
    """
    randdom_gen = (random.SystemRandom().choice(choices) for _ in range(length))
    return ''.join(randdom_gen)


def create_pws(services, length, choices):
    pws = {service: random_password(choices, length) for service in services}

    return pws
