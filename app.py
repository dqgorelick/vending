#!/usr/bin/env python

import os, json

from datetime import datetime
from flask import Flask, request, render_template

from product_names import names

app = Flask(__name__, static_url_path='')
app.debug = True


@app.route('/update')
def create_report():

    ts = request.args.get('timestamp')
    pretty_ts = datetime.fromtimestamp(int(ts)).strftime('%H:%M:%S %d %m %Y')
    data = request.args.get('data')

    all_products = []
    shelfs = [
        {
            'name': 'A',
            'products': []
        }, {
            'name': 'B',
            'products': []
        }, {
            'name': 'C',
            'products': []
        }, {
            'name': 'D',
            'products': []
        }
    ]

    print (names)

    for i in json.loads(data):
        # check for valid shelf number
        shelf = int(i['shelf'])
        if shelf >= 0 and shelf <= 3:
            for p in shelfs[shelf]['products']:
                p['name'] = names[p['type']]
            shelfs[shelf]['products'].append(i)
            all_products.append(i)
        else:
            print('product not valid: {}'.format(i))

    for i in shelfs:
        i['count'] = len(i['products'])


    fname = os.path.join('./static','report_output.html')
    with open(fname, 'w') as f:
        html = render_template('report_template.html', ts=pretty_ts, shelfs=shelfs, all_products=all_products, count=len(all_products))
        f.write(html)

    return ('', 200)


@app.route("/report")
def get_report():
    return app.send_static_file('report_output.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, threaded=False)
