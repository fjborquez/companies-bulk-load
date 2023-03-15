import csv

import requests
from edgar import Edgar

API_URL = "https://6naqn3cyvi.execute-api.us-east-1.amazonaws.com/api/companies"

edgar_client = Edgar()

def get_cik_by_name(company_name):
    try:
        return edgar_client.get_cik_by_company_name(company_name.upper())
    except:
        return ""


def open_csv():
    lines = []

    with open('./datasets/companies.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                lines.append(row)

            line_count += 1

    return lines

def bulk_load():
    companies = open_csv()
    for company in companies:
        cik = get_cik_by_name(company[0])
        requests.post(API_URL, json={
            "cik": cik,
            "name": company[0],
            "shortname": company[1]
        })


def main():
    bulk_load()


main()
