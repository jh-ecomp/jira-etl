import jiraetl

issues = jiraetl.get_issues()

if len(issues):
    processed_issues = jiraetl.process_issues(issues)

    jiraetl.store_issues(processed_issues)


