def flat(d):
    for key, val in d.items():
        if isinstance(val, dict):
            yield from flat(val)
        else:
            yield (key, val)


def flat_prefix(d):
    for key, val in d.items():
        if isinstance(val, dict):
            for k, v in flat_prefix(val):
                yield (f'{key}_{k}', v)
        else:
            yield (key, val)


if __name__ == '__main__':
    d = {
        'a': 1,
        'b': {
            'c': 2,
            'd': 3,
            'e': {'f': 4}
        },
        'g': {'h': 5},
        'i': 6,
        'j': {'k': {'l': {'m': 7}}},
    }
    print({k: v for k, v in flat(d)})
    print({k: v for k, v in flat_prefix(d)})