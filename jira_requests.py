import requests
from requests import Session
from requests.auth import HTTPBasicAuth
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.exceptions import Timeout
import traceback


def mount_jira_session(jira_domain):
    auth = HTTPBasicAuth('fake@example.com', 'not_a_real_password')

    url = f'{jira_domain}'
    retries = Retry(total=5, backoff_factor=1)
    session = Session()
    session.mount('http://', HTTPAdapter(max_retries=retries))
    response = None

    try:
        response = session.get(url, auth=auth)
    except Timeout as t:
        print(f'Session request timeout {t}')
        traceback.print_exc()
    except Exception as e:
        print(f'Session request exception {e}')
        traceback.print_exc()

    return response


def get_jira_main_request(main_request, jql, fields, expand, start_at, max_results, cookies):

    url = f'{main_request}?jql={jql}&fields={fields}&expand={expand}&startAt={start_at}&maxResults={max_results}'
    response = None
    try:
        response = requests.get(url=url, cookies=cookies, timeout=60)
    except Timeout as t:
        print(f'Jira request timeout {t}')
        traceback.print_exc()
    except Exception as e:
        print(f'Jira request exception {e}')
        traceback.print_exc()

    if response is None: return response

    try:
        issues = response.json()
    except Exception as e:
        print(f'Failed to load response content cause {e}')
        issues = None


    return issues

