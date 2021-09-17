from requests import Request, Session
from requests.auth import HTTPBasicAuth
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.exceptions import Timeout
import traceback


def mount_jira_session():
    auth = HTTPBasicAuth('fake@example.com', 'not_a_real_password')

    with open('jira.config') as jira_config:
        line = jira_config.readline()
        while line:
            if line.find('jira-domain'):
                url = jira_config.readline()
                break
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

