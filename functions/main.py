import requests


def wmlResult(dict):
    apikey = dict['wml_apikey']
    ml_instance_id = dict['wml_instance_id']
    scoring_url = dict['wml_scoring_url']
    payload_scoring = {"input_data": [{"fields": ["ApplicantIncome", "CoapplicantIncome",
                                                  "LoanAmount", "Loan_Amount_Term", "Credit_History"], "values":[[dict['ApplicantIncome'], dict['CoapplicantIncome'], dict['LoanAmount'], dict['Loan_Amount_Term'], 1 if dict['Credit_History'] == 'Yes' else 0]]}]}

    # Get an IAM token from IBM Cloud
    url = "https://iam.bluemix.net/oidc/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = "apikey=" + apikey + "&grant_type=urn:ibm:params:oauth:grant-type:apikey"
    IBM_cloud_IAM_uid = "bx"
    IBM_cloud_IAM_pwd = "bx"
    response = requests.post(url, headers=headers, data=data, auth=(
        IBM_cloud_IAM_uid, IBM_cloud_IAM_pwd))
    iam_token = response.json()["access_token"]

    # NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation
    header = {'Content-Type': 'application/json',
              'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': ml_instance_id}


    response_scoring = (requests.post(
        scoring_url, json=payload_scoring, headers=header)).json()

    # setting response string
    if response_scoring['predictions'][0]['values'][0][0] == "Y":
        return {"result": "Congratulations you are eligible for the loan"}
    else:
        return {"result": "Sorry you are not eligible for the loan at his moment"}


def discoveryResult(dict):

    # setting parameters, please check if the version matches with your instance
    params = (
        ('version', '2018-12-03'),
        ('count', '1'),
        ('deduplicate', 'false'),
        ('highlight', 'true'),
        ('return', 'answer'),
        ('passages', 'false'),
        ('passages.count', '1'),
        ('passages.fields', 'answer'),
        ('natural_language_query', dict['query']),
    )

    # forming the query url
    url = dict['discovery_url']+'/v1/environments/'+dict['discovery_environment_id'] + \
        '/collections/'+dict['discovery_collection_id']+'/query'

    response = (requests.get(url,
                            params=params, auth=('apikey', dict['discovery_apikey']))).json()
    
    return {'result': response['results'][0]['answer'][0]} if len(response['results']) > 0 else {"result":"I did not understand. Please rephrase your query"}


def main(dict):
    # determine what kind of query we have
    if dict['kind'] == 'wml':
        return wmlResult(dict)
    elif dict['kind'] == 'discovery':
        return discoveryResult(dict)

