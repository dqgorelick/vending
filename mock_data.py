import time, sys, json, requests
from random import randint, uniform

from product_names import products

# test ec2 instance
# endpoint = "http://ec2-54-175-77-220.compute-1.amazonaws.com/update"

# test local
endpoint = "http://127.0.0.1:9000/update"

def main():

    data = []

    if len(sys.argv) > 1:
        number_items = int(sys.argv[1])
    else:
        number_items = 25

    for item in range(0,number_items):
        # TODO: generate random values
        data.append({
            'type': randint(1,len(products)),
            'confidence': uniform(75, 100),
            'shelf': randint(0,3),
            'x': uniform(0,565-20),
            'y': uniform(0,492-20)
        });

    package = {'timestamp':int(time.time()), 'data':json.dumps(data)}

    try:
        response = requests.get(endpoint, params=package)
        print('response: {} - {}'.format(response.text, response.status_code))
    except requests.exceptions.RequestException as e:
        print('error: {}',format(e))
        sys.exit(1)

if __name__ == '__main__':
    main()
