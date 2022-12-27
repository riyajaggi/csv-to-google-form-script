import requests
import pandas as pd

path = ""
csv = pd.read_csv(path)

url = ""

form_ids = {
    "name": "entry.1640497130",
    "country": "entry.2070807863",
    "amount": "entry.1546099309"
}


def submit(url, submission):
    response = requests.post(url, submission)
    response_code = response.status_code
    response_message = response.reason
    print(response_code)
    print(response_message)


for index, row in csv.iterrows():
    # print(row)
    name = row['Name']
    country = row['Country']
    amount = row['Amount']

    submission = {form_ids["name"]: name,
                  form_ids["country"]: country,
                  form_ids["amount"]: amount}
    print(submission)
    submit(url, submission)

    print(index, 'request sent')
