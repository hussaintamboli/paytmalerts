import subprocess


def notify(payload):
    subprocess.Popen(['notify-send', payload['title'], payload['message']])
    return
