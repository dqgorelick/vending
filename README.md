# Smart Fridge Web Server

Flask app which receives updates, creates HTML reports, and uploads to S3.

Static Files S3: `http://smart-fridge-dark-matter.s3-website-us-east-1.amazonaws.com`
EC2 Instance: `http://ec2-54-175-77-220.compute-1.amazonaws.com/`

[Sample Report](http://smart-fridge-dark-matter.s3-website-us-east-1.amazonaws.com/report_output.html)


#### Setup

- set up virtual environment:

`virtualenv venv`
`. venv/bin/activate`

- install packages

`pip install`

#### Running the app locally

Run app: `python app.py <PORT_NUMBER>`
Send test data: `python mock_data.py <AMOUNT_OF_PRODUCTS>` (default is 25)


#### Updating product names

As more types are added, update `product_names.py` file.


#### Setting up AWS

Create `.env` in root directory, follow format of `.env.default` with provided credentials.


#### TODO:

- Add (and get) dimensions to different products for layout
- Crop all images to be square
- Finish HTML -> PDF converting
- Create DB and API endpoints for viewing historical reports

