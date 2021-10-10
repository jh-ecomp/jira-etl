
from base_model import build_db_session
from jira_requests import mount_jira_session, get_jira_issues
from my_jira_project import MyJiraProject
from db_connection import update_issues, search_issue


config_dict = {'domain': '', 'main_request': '', 'jql': '', 'fields': '', 'expand': '', 'start_at': '', 'max_results': ''}

with open('jira.config', 'r') as config:
    while True:
        line = config.readline()
        if line == '# end':
            break
        if line == '\n' or line.startswith('#'):
            continue

        config_dict[line.split('#')[0]] = line.split('#')[1][0:-1]
jira_session = mount_jira_session(config_dict['domain'])

issues = list()
if jira_session is not None:
    issues = get_jira_issues(config_dict, jira_session.cookies)
    jira_session.close()

issues_to_update = list()
if len(issues):
    for issue in issues:
        try:
            alchemy_session = build_db_session()
            issue_imported = search_issue(MyJiraProject().__tablename__, issue['id'])
            issue_parsed = MyJiraProject().parse(issue)
            if issue_imported is False:
                alchemy_session.add(issue_parsed)
            else:
                issues_to_update.append(issue_parsed)
            alchemy_session.commit()
            alchemy_session.close()
        except Exception as e:
            print(e)

    if len(issues_to_update):
        update_issues(MyJiraProject.__tablename__, issues_to_update)


