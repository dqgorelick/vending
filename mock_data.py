import time, sys, json
import requests

from random import randint, uniform

from product_names import names

# CLI arg 1 = number of items, DEFAULT=100
# CLI arg 2 = port, DEFAULT=9000

def main():

    data = []
    number_items = int(sys.argv[1]) or 100
    print(number_items)


    for item in range(0,number_items):
        # TODO: generate random values
        data.append({
            'type': randint(0,len(names) - 1),
            'confidence': uniform(75, 100),
            'shelf': randint(0,3),
            'x': uniform(0,565-20),
            'y': uniform(0,492-20)
        });

    package = {'timestamp':int(time.time()), 'data':json.dumps(data)}
    print(package)

    try:
        response = requests.get('http://0.0.0.0:9000/update', params=package)
        print('response: {}'.format(response))
    except requests.exceptions.RequestException as e:
        print('error: {}',format(e))
        sys.exit(1)

if __name__ == '__main__':
    main()
