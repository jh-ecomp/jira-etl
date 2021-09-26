import jira_requests


def process_issue(issue):
    return True

def get_jira_issues(config, cookies):
    issues_list = list()
    start_at = int(config['start_at'])
    max_results = int(config['max_results'])
    while True:
        jira_issues = jira_requests.get_jira_main_request(config['main_request'], config['jql'], config['fields'],
                                                          config['expand'], start_at, max_results,
                                                          cookies)
        if jira_issues is not None:
            total = jira_issues['total']
            for issue in jira_issues['issues']:
                issues_list.append(process_issue(issue))
        if start_at +  max_results>= total: break
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



