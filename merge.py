from github import Github

# Authenticate with GitHub API using your PAT
g = Github("YOUR_PERSONAL_ACCESS_TOKEN")

# Get the repositories
admin_repo = g.get_repo("Admin_Name/Admin")
developer_repo = g.get_repo("Dev_Name/Developer")

# Get all open pull requests in the developer's repository
pull_requests = developer_repo.get_pulls(state="open")

# Iterate over the pull requests
for pull_request in pull_requests:
    # Get the branch names of the base and head
    base_branch = pull_request.base.ref
    head_branch = pull_request.head.ref

    # Check if the pull request satisfies the branch rules
    if base_branch == "main" and head_branch == "feature-branch":
        # Merge the pull request
        admin_repo.merge_pull(pull_request.number)
        print(f"Pull request #{pull_request.number} merged successfully.")
    else:
        print(f"Pull request #{pull_request.number} does not satisfy branch rules and cannot be merged.")
