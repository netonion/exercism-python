from itertools import chain, cycle

def fence_pattern(rails, message_size):
    """
    fence_pattern returns a generator that generates the
    indices of characters from the plaintext.
    """
    # idx goes from 0 to rails-1 and from rails-1 to 1 endlessly
    rail_idx = cycle(chain(range(rails-1), range(rails-1, 0, -1)))
    pattern = [[] for _ in range(rails)]
    for i in range(message_size):
        pattern[next(rail_idx)].append(i)
    return chain(*pattern)


def encode(message, rails):
    return ''.join(message[i] for i in fence_pattern(rails, len(message)))

def decode(encoded_message, rails):
    msg = [None] * len(encoded_message)
    idx = fence_pattern(rails, len(encoded_message))
    for c in encoded_message:
        msg[next(idx)] = c
    return ''.join(msg)