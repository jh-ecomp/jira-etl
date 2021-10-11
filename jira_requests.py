import requests
from requests import Session
from requests.auth import HTTPBasicAuth
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.exceptions import Timeout
import traceback


def mount_jira_session(jira_domain):
    auth = HTTPBasicAuth('fake_user', 'not_a_real_password')

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

    if response is None:
        return response

    try:
        issues = response.json()
    except Exception as e:
        print(f'Failed to load response content cause {e}')
        issues = None

    return issues


def get_jira_issues(jira_config, cookies):
    issues_list = list()
    start_at = int(jira_config['start_at'])
    max_results = int(jira_config['max_results'])
    total = 0
    while True:
        jira_issues = get_jira_main_request(jira_config['main_request'], jira_config['jql'], jira_config['fields'],
                                            jira_config['expand'], start_at, max_results, cookies)
        if jira_issues is not None:
            total = jira_issues['total']
            for issue in jira_issues['issues']:
                issues_list.append(issue)

        if start_at + max_results >= total:
            break
        start_at += max_results

    return issues_list
