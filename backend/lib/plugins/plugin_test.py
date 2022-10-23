def before_send(*args, **kwargs):
    print(args, kwargs)
    print('Hello from before send')
    return 'Mauaiui'

def after_send(*args, **kwargs):
    print(args, kwargs)
    print('Hello from before send')
    return 'Mauaiui'

def frontend_json(*args, **kwargs):
    print(args, kwargs)
    print('Hello from before send')
    return 'Mauaiui'