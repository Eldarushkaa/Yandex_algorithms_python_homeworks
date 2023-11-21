import sys


def get_params(url):
    args = dict()
    url = list(filter(bool, url.split('/?')))
    if len(url) <= 1:
        return args
    for key, value in map(lambda x: x.split('='), url[-1].split('&')):
        if key in args:
            if isinstance(args[key], str):
                args[key] = [args[key], value]
            else:
                args[key].append(value)
        else:
            args[key] = value
    return args


def add_params(url, params):
    url += '?'
    for key in params:
        if isinstance(params[key], str):
            url += key + '=' + params[key] + '&'
        else:
            url += '&'.join(map(lambda x: key + '=' + x,params[key])) + '&'
    return url[:-1]


# exec(sys.stdin.read())
print(get_params(''))
print(get_params('asdf.fdsa/'))
print(get_params('asdf.dsf/?'))
