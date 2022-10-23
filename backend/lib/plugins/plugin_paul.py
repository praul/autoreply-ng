def before_send(*args, **kwargs):
    print(args, kwargs)
    print('Hello from before send PAUL')
    return 'MauaiuiPAUL'

def after_send(*args, **kwargs):
    print(args, kwargs)
    print('Hello from before sendPAUL')
    return 'MauaiuiPAUL'

def frontend_json(*args, **kwargs):
    print(args, kwargs)
    print('Hello from before sendPAUL')
    return 'MauaiuiPAUL'