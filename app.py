#!/usr/bin/env python

import os, json

from datetime import datetime
from flask import Flask, request, render_template

from product_names import products

app = Flask(__name__, static_url_path='')
app.debug = True


@app.route('/update')
def create_report():

    ts = request.args.get('timestamp')
    pretty_ts = datetime.fromtimestamp(int(ts)).strftime('%H:%M:%S - %d %b %Y')
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


    for i in json.loads(data):
        # check for valid shelf number
        shelf = int(i['shelf'])
        if shelf >= 0 and shelf <= 3:
            shelfs[shelf]['products'].append(i)
            all_products.append(i)
            for p in shelfs[shelf]['products']:
                p['name'] = products[str(p['type'])]['name']
                p['src'] = products[str(p['type'])]['src']
        else:
            print('product not valid: {}'.format(i))

    shelf_counts = []
    for s in shelfs:
        shelf_counts.append(
            {
                'count': len(s['products']),
                'name': s['name']
            }
        )

    products_by_brand = {}
    for p in all_products:
        try:
            products_by_brand[p['name']]['count'] += 1
        except:
            products_by_brand[p['name']] = {}
            products_by_brand[p['name']]['count'] = 1
            products_by_brand[p['name']]['src'] = products[str(p['type'])]['src']

    sorted_alpha = sorted(products_by_brand, key=str.lower)
    sorted_count = sorted(products_by_brand, key=products_by_brand.get, reverse=True)

    fname = os.path.join('./static','report_output.html')
    with open(fname, 'w') as f:
        html = render_template('report_template.html',
            ts=pretty_ts,
            shelfs=reversed(shelfs),
            shelf_counts=reversed(shelf_counts),
            all_products=all_products,
            products_by_brand=products_by_brand,
            sorted_alpha=sorted_alpha,
            sorted_count=sorted_count
        )
        f.write(html)

    return ('', 200)


@app.route("/report")
def get_report():
    return app.send_static_file('report_output.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, threaded=False)
