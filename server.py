from bottle import route, run, template
from pyudmx import pyudmx
import atexit

def close_device():
    print 'closing'
    dev.close()

atexit.register(close_device)

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/<channel>/<values>')
def set_values(channel, values):
    try:
        values = map(int, values.split('_'))
        channel = int(channel)
    except:
        return 'Please provide numbers!'
    dev = pyudmx.uDMXDevice()
    dev.open()
    # dev.send_multi_value(73, [250,255,200])
    dev.send_multi_value(channel, values)
    dev.close()

    return 'Got it!'

def _initialize():
    print 'init'
    dev = pyudmx.uDMXDevice()
    dev.open()
    dev.send_multi_value(73, [250,255,200])
    print 'opened successfully'

if __name__ == "__main__":
    # _initialize()
    run(host='localhost', port=3737)
