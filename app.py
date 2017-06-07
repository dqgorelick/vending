#!/usr/bin/env python

import os, sys, json
from dateutil import tz

from flask import Flask, request, render_template, url_for
from datetime import datetime
import boto3
from dotenv import load_dotenv
import pdfkit

from product_names import products

app = Flask(__name__, static_url_path='')
# app.debug = True


@app.route('/update')
def create_report():

    try:
        ts = request.args.get('timestamp')
        utc_ts = datetime.fromtimestamp(int(ts))
    except Exception as e:
        return('invalid data sent: {}'.format(e), 422)

    from_zone = tz.tzutc()
    to_zone = tz.gettz('America/New_York')
    utc_ts = utc_ts.replace(tzinfo=from_zone).astimezone(to_zone)
    pretty_ts = utc_ts.strftime('%H:%M:%S - %d %b %Y')

    try:
        data = request.args.get('data')
    except Exception as e:
        return('invalid data sent: {}'.format(e), 422)

    all_products = []
    shelfs = [
        { 'name': 'D', 'products': [] },
        { 'name': 'C', 'products': [] },
        { 'name': 'B', 'products': [] },
        { 'name': 'A', 'products': [] }
    ]

    try:
        json_data = json.loads(data)
    except Exception as e:
        return('cannot parse JSON: {}'.format(e), 422)

    for i in json_data:
        # check for valid shelf number
        shelf = int(i['shelf'])
        if shelf >= 0 and shelf <= 3:
            shelfs[shelf]['products'].append(i)
            all_products.append(i)
            for p in shelfs[shelf]['products']:
                try:
                    p['name'] = products[str(p['type'])]['name']
                    p['src'] = products[str(p['type'])]['src']
                except Exception as e:
                    return('Invalid key: {}, error: {}'.format(p['type'], e), 422)
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

    # create reference for sorted lists
    products_by_brand = {}
    for p in all_products:
        try:
            products_by_brand[p['name']]['count'] += 1
        except:
            products_by_brand[p['name']] = {}
            products_by_brand[p['name']]['count'] = 1
            products_by_brand[p['name']]['src'] = products[str(p['type'])]['src']

    # create sorted lists
    sorted_alpha = sorted(products_by_brand, key=str.lower)
    sorted_count = sorted(products_by_brand, key=products_by_brand.get, reverse=True)

    output_file = os.path.join('./static','report_output.html')
    with open(output_file, 'w') as f:
        try:
            html = render_template('report_template.html',
                ts=pretty_ts,
                shelfs=shelfs,
                shelf_counts=shelf_counts,
                all_products=all_products,
                products_by_brand=products_by_brand,
                sorted_alpha=sorted_alpha,
                sorted_count=sorted_count
            )
        except Exception as e:
            return('Cannot render HTML: {}'.format(e), 422)
        try:
            f.write(html)
            print('writing html file')
        except Exception as e:
            return('Error writing file error: {}'.format(e), 422)

    try:
        upload_report()
    except Exception as e:
        return('Cannot upload report to S3: {}'.format(e), 422)

    return ('{} products sent successfully'.format(len(all_products)), 200)

@app.route("/upload")
def upload_report():
    try:
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    except Exception as e:
        return('Cannot find .env path: {}'.format(e), 500)

    load_dotenv(dotenv_path)

    aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
    aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']

    # create profile in ~/.aws/credentials for "smart-fridge"
    session = boto3.session.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name="us-east-1"
    )
    s3 = session.resource("s3")

    bucket_name = "smart-fridge-dark-matter"
    file_path = os.path.join('./static','report_output.html')
    object_name = 'report_output.html'

    try:
        response = s3.Object(bucket_name, object_name).put(Body=open(file_path, 'rb'), ContentType='text/html')
        return('uploaded!', 200)
    except Exception as e:
        return('could not upload: {}'.format(e), 500)

@app.route("/report")
def get_report():
    return app.send_static_file('report_output.html')

@app.route('/render')
def create_pdf():

    input_html = os.path.join('./static','report_output.html')
    output_pdf = os.path.join('./static','report_output.pdf')

    options = {
        'lowquality': None
    }

    pdfkit.from_file(input_html, output_pdf, options=options)
    return app.send_static_file('report_output.pdf')


if __name__ == '__main__':
    port = 9000
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    app.run(host='0.0.0.0', port=port, threaded=False)
