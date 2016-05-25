CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web',
    # 'python': '/usr/bin/python3',
    'args': (
        '--bind=0.0.0.0:8080',
        '--daemon',
        '--workers=4',
        '--timeout=60',
        'hello:app'
    )
}