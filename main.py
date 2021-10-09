import jira_requests
from datetime import datetime
from dateutil.parser import parse


def days_diference(out_date, in_date):
    if out_date is None or in_date is None:
        return 0
    return round(abs((out_date - in_date).total_seconds()) / 86400, 4)


def process_issue(issue):
    issue_dict = dict()
    issue_fields = issue['fields']

    issue_dict['id'] = issue['id']
    issue_dict['key'] = issue['key']

    issue_dict['project'] = issue_fields['project']['key']
    issue_dict['issuetype'] = issue_fields['issuetype']['name']
    issue_dict['summary'] = issue_fields['summary']
    issue_dict['description'] = issue_fields['description']
    issue_dict['priority'] = issue_fields['priority']['name']
    issue_dict['priority_id'] = issue_fields['priority']['id']

    links = issue_fields['issuelinks']
    outward_issues = list()
    for link in links:
        try:
            outward_issues.append(link['outwardIssue']['key'])
        except:
            pass
    issue_dict['issuelinks'] = outward_issues

    issue_dict['creator'] = issue_fields['creator']['displayName']

    issue_dict['assignee'] = None if issue_fields['assignee'] is None else issue_fields['assignee']['displayName']
    issue_dict['reporter'] = None if issue_fields['reporter'] is None else issue_fields['reporter']['displayName']
    issue_dict['status'] = issue_fields['status']['name']
    issue_dict['status_category'] = issue_fields['status']['statusCategory']['name']
    issue_dict['resolution'] = None if issue_fields['resolution'] is None else issue_fields['resolution']['name']

    issue_dict['created'] = parse(issue_fields['created'].split('+')[0])
    issue_dict['updated'] = parse(issue_fields['updated'].split('+')[0])
    resolutiondate = issue_fields['resolutiondate']
    if resolutiondate is not None:
        resolutiondate = resolutiondate.split('+')[0]
        issue_dict['resolutiondate'] = parse(resolutiondate)
        issue_dict['duration'] = days_diference(issue_dict['created'], issue_dict['resolutiondate'])
    else:
        now = datetime.now().replace(microsecond=0)
        issue_dict['resolutiondate'] = None
        issue_dict['duration'] = days_diference(issue_dict['created'], now)

    issue_dict['duedate'] = None if issue_fields['duedate'] is None else parse(issue_fields['duedate']).date()

    return issue_dict


def get_jira_issues(jira_config, cookies):
    issues_list = list()
    start_at = int(jira_config['start_at'])
    max_results = int(jira_config['max_results'])
    total = 0
    while True:
        jira_issues = jira_requests.get_jira_main_request(jira_config['main_request'], jira_config['jql'], jira_config['fields'],
                                                          jira_config['expand'], start_at, max_results,
                                                          cookies)
        if jira_issues is not None:
            total = jira_issues['total']
            for issue in jira_issues['issues']:
                issues_list.append(process_issue(issue))

        if start_at + max_results >= total:
            break
        start_at += max_results

    return issues_list


if __name__ == "__main__":
    config_dict = {'domain': '', 'main_request': '', 'jql': '', 'fields': '', 'expand': '', 'start_at': '', 'max_results': ''}
    with open('jira.config', 'r') as config:
        while True:
            line = config.readline()
            if line == '# end': break
            if line == '\n' or line.startswith('#'): continue

            config_dict[line.split('#')[0]] = line.split('#')[1][0:-1]

    jira_session = jira_requests.mount_jira_session(config_dict['domain'])
    if jira_session is not None:
        issues = get_jira_issues(config_dict, jira_session.cookies)
        jira_session.close()

        print(len(issues))
        for i in issues:
            print(i)



