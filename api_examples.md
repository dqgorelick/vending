### Create list of objects

```
data = [
    {"type": 1, "shelf": 4, "confidence": 75.86666150041403, "x": 17, "y": 14},
    {"type": 2, "shelf": 3, "confidence": 97.29603962569972, "x": 9, "y": 23},
    {"type": 3, "shelf": 4, "confidence": 83.65156460756647, "x": 2, "y": 1},
    {"type": 0, "shelf": 2, "confidence": 76.82851810857788, "x": 12, "y": 3},
    {"type": 5, "shelf": 2, "confidence": 86.14495908676233, "x": 21, "y": 1},
    {"type": 4, "shelf": 3, "confidence": 82.0039337110544, "x": 7, "y": 16},
    {"type": 5, "shelf": 1, "confidence": 91.24713242599242, "x": 25, "y": 2},
    {"type": 4, "shelf": 1, "confidence": 77.42836117779183, "x": 9, "y": 22},
    {"type": 0, "shelf": 2, "confidence": 82.05557125588703, "x": 3, "y": 7},
    {"type": 2, "shelf": 3, "confidence": 98.15720836326142, "x": 20, "y": 2},
    {"type": 5, "shelf": 3, "confidence": 83.1688980867798, "x": 13, "y": 25},
    {"type": 4, "shelf": 0, "confidence": 92.72821721198001, "x": 24, "y": 5},
    {"type": 3, "shelf": 2, "confidence": 82.72138586754359, "x": 19, "y": 10},
    {"type": 0, "shelf": 5, "confidence": 95.90567328342829, "x": 6, "y": 19},
    {"type": 4, "shelf": 4, "confidence": 75.2088873577861, "x": 9, "y": 22},
    {"type": 5, "shelf": 1, "confidence": 82.66305500789852, "x": 11, "y": 7},
    {"type": 5, "shelf": 4, "confidence": 86.42911253272621, "x": 25, "y": 23},
    {"type": 1, "shelf": 5, "confidence": 82.12439283833015, "x": 16, "y": 0},
    {"type": 5, "shelf": 3, "confidence": 76.5403814486562, "x": 9, "y": 19},
    {"type": 1, "shelf": 3, "confidence": 91.5479301144299, "x": 2, "y": 53}
]
```

### create JSON object, along with unix timestamp added for when data was collected (this can change)

```
to_send = {
    'timestamp': 1495648288,
    'data': '[{"y": 14, "shelf": 4, "confidence": 75.86666150041403, "type": 1, "x": 17}, {"y": 23, "shelf": 3, "confidence": 97.29603962569972, "type": 2, "x": 9}, {"y": 1, "shelf": 4, "confidence": 83.65156460756647, "type": 3, "x": 2}, {"y": 3, "shelf": 2, "confidence": 76.82851810857788, "type": 0, "x": 12}, {"y": 1, "shelf": 2, "confidence": 86.14495908676233, "type": 5, "x": 21}, {"y": 16, "shelf": 3, "confidence": 82.0039337110544, "type": 4, "x": 7}, {"y": 2, "shelf": 1, "confidence": 91.24713242599242, "type": 5, "x": 25}, {"y": 22, "shelf": 1, "confidence": 77.42836117779183, "type": 4, "x": 9}, {"y": 7, "shelf": 2, "confidence": 82.05557125588703, "type": 0, "x": 3}, {"y": 2, "shelf": 3, "confidence": 98.15720836326142, "type": 2, "x": 20}, {"y": 25, "shelf": 3, "confidence": 83.1688980867798, "type": 5, "x": 13}, {"y": 5, "shelf": 0, "confidence": 92.72821721198001, "type": 4, "x": 24}, {"y": 10, "shelf": 2, "confidence": 82.72138586754359, "type": 3, "x": 19}, {"y": 19, "shelf": 5, "confidence": 95.90567328342829, "type": 0, "x": 6}, {"y": 22, "shelf": 4, "confidence": 75.2088873577861, "type": 4, "x": 9}, {"y": 7, "shelf": 1, "confidence": 82.66305500789852, "type": 5, "x": 11}, {"y": 23, "shelf": 4, "confidence": 86.42911253272621, "type": 5, "x": 25}, {"y": 0, "shelf": 5, "confidence": 82.12439283833015, "type": 1, "x": 16}, {"y": 19, "shelf": 3, "confidence": 76.5403814486562, "type": 5, "x": 9}, {"y": 5, "shelf": 3, "confidence": 91.5479301144299, "type": 1, "x": 23}]'
}
```

#### Encode data into query string parameters, send GET request to API endpoint /update (IP address to come)

```
/update?timestamp=1495648288&data=%5B%7B%22y%22%3A+14%2C+%22shelf%22%3A+4%2C+%22confidence%22%3A+75.86666150041403%2C+%22type%22%3A+1%2C+%22x%22%3A+17%7D%2C+%7B%22y%22%3A+23%2C+%22shelf%22%3A+3%2C+%22confidence%22%3A+97.29603962569972%2C+%22type%22%3A+2%2C+%22x%22%3A+9%7D%2C+%7B%22y%22%3A+1%2C+%22shelf%22%3A+4%2C+%22confidence%22%3A+83.65156460756647%2C+%22type%22%3A+3%2C+%22x%22%3A+2%7D%2C+%7B%22y%22%3A+3%2C+%22shelf%22%3A+2%2C+%22confidence%22%3A+76.82851810857788%2C+%22type%22%3A+0%2C+%22x%22%3A+12%7D%2C+%7B%22y%22%3A+1%2C+%22shelf%22%3A+2%2C+%22confidence%22%3A+86.14495908676233%2C+%22type%22%3A+5%2C+%22x%22%3A+21%7D%2C+%7B%22y%22%3A+16%2C+%22shelf%22%3A+3%2C+%22confidence%22%3A+82.0039337110544%2C+%22type%22%3A+4%2C+%22x%22%3A+7%7D%2C+%7B%22y%22%3A+2%2C+%22shelf%22%3A+1%2C+%22confidence%22%3A+91.24713242599242%2C+%22type%22%3A+5%2C+%22x%22%3A+25%7D%2C+%7B%22y%22%3A+22%2C+%22shelf%22%3A+1%2C+%22confidence%22%3A+77.42836117779183%2C+%22type%22%3A+4%2C+%22x%22%3A+9%7D%2C+%7B%22y%22%3A+7%2C+%22shelf%22%3A+2%2C+%22confidence%22%3A+82.05557125588703%2C+%22type%22%3A+0%2C+%22x%22%3A+3%7D%2C+%7B%22y%22%3A+2%2C+%22shelf%22%3A+3%2C+%22confidence%22%3A+98.15720836326142%2C+%22type%22%3A+2%2C+%22x%22%3A+20%7D%2C+%7B%22y%22%3A+25%2C+%22shelf%22%3A+3%2C+%22confidence%22%3A+83.1688980867798%2C+%22type%22%3A+5%2C+%22x%22%3A+13%7D%2C+%7B%22y%22%3A+5%2C+%22shelf%22%3A+0%2C+%22confidence%22%3A+92.72821721198001%2C+%22type%22%3A+4%2C+%22x%22%3A+24%7D%2C+%7B%22y%22%3A+10%2C+%22shelf%22%3A+2%2C+%22confidence%22%3A+82.72138586754359%2C+%22type%22%3A+3%2C+%22x%22%3A+19%7D%2C+%7B%22y%22%3A+19%2C+%22shelf%22%3A+5%2C+%22confidence%22%3A+95.90567328342829%2C+%22type%22%3A+0%2C+%22x%22%3A+6%7D%2C+%7B%22y%22%3A+22%2C+%22shelf%22%3A+4%2C+%22confidence%22%3A+75.2088873577861%2C+%22type%22%3A+4%2C+%22x%22%3A+9%7D%2C+%7B%22y%22%3A+7%2C+%22shelf%22%3A+1%2C+%22confidence%22%3A+82.66305500789852%2C+%22type%22%3A+5%2C+%22x%22%3A+11%7D%2C+%7B%22y%22%3A+23%2C+%22shelf%22%3A+4%2C+%22confidence%22%3A+86.42911253272621%2C+%22type%22%3A+5%2C+%22x%22%3A+25%7D%2C+%7B%22y%22%3A+0%2C+%22shelf%22%3A+5%2C+%22confidence%22%3A+82.12439283833015%2C+%22type%22%3A+1%2C+%22x%22%3A+16%7D%2C+%7B%22y%22%3A+19%2C+%22shelf%22%3A+3%2C+%22confidence%22%3A+76.5403814486562%2C+%22type%22%3A+5%2C+%22x%22%3A+9%7D%2C+%7B%22y%22%3A+5%2C+%22shelf%22%3A+3%2C+%22confidence%22%3A+91.5479301144299%2C+%22type%22%3A+1%2C+%22x%22%3A+23%7D%5D
```

