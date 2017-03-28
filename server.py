from bottle import route, run, template
from pyudmx import pyudmx

@route('/<channel>/<values>')
def set_values(channel, values):
    try:
        values = map(int, values.split('_'))
        channel = int(channel)
    except:
        return 'Please provide numbers!'
    dev = pyudmx.uDMXDevice()
    dev.open()
    dev.send_multi_value(channel, values)
    dev.close()

    return 'Got it!'

if __name__ == "__main__":
    run(host='localhost', port=3737)
