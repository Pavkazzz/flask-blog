# encoding: utf-8
import re
import string
import random
from urlparse import urljoin
from flask import request, url_for, session, flash, redirect
from functools import wraps
import hashlib
import hmac


def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)


def extract_tags(tags):
    whitespace = re.compile('\s')
    nowhite = whitespace.sub("", tags)
    tags_array = nowhite.split(',')

    cleaned = []
    for tag in tags_array:
        if tag not in cleaned and tag != "":
            cleaned.append(tag)

    return cleaned


def random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = random_string()
    return session['_csrf_token']


def make_external(url):
    return urljoin(request.url_root, url)


def login_required():
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if not session.get('user'):
                flash('You must be logged in..', 'error')
                return redirect(url_for('login'))
            return f(*args, **kwargs)
        return wrapped
    return wrapper


def logout_required():
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if session.get('user'):
                flash('You must be logout in..', 'error')
                return redirect(url_for('login'))
            return f(*args, **kwargs)
        return wrapped
    return wrapper


def _validate_signature(header, data):
    sha_name, signature = header.split('=')
    if sha_name != 'sha1':
        return True

    print sha_name, signature, json
    # HMAC requires its key to be bytes, but data is strings.
    mac = hmac.new('pavka', msg=data, digestmod=hashlib.sha1)
    return hmac.compare_digest(mac.hexdigest(), signature)

if __name__ == '__main__':
    json = """{
  "ref": "refs/heads/master",
  "before": "c49e9a3588a2e24d25211e065e2d1ef37e4b83f9",
  "after": "24d9b5d6c1e44928f7cf3a593eede7a94d0cc0c5",
  "created": false,
  "deleted": false,
  "forced": false,
  "base_ref": null,
  "compare": "https://github.com/Pavkazzz/flask-blog/compare/c49e9a3588a2...24d9b5d6c1e4",
  "commits": [
    {
      "id": "24d9b5d6c1e44928f7cf3a593eede7a94d0cc0c5",
      "distinct": true,
      "message": "nav",
      "timestamp": "2014-11-28T17:17:21+03:00",
      "url": "https://github.com/Pavkazzz/flask-blog/commit/24d9b5d6c1e44928f7cf3a593eede7a94d0cc0c5",
      "author": {
        "name": "Pavka",
        "email": "pavkazzz@mail.ru",
        "username": "Pavkazzz"
      },
      "committer": {
        "name": "Pavka",
        "email": "pavkazzz@mail.ru",
        "username": "Pavkazzz"
      },
      "added": [

      ],
      "removed": [
        "1.txt"
      ],
      "modified": [
        "templates/nav.html",
        "web.py"
      ]
    }
  ],
  "head_commit": {
    "id": "24d9b5d6c1e44928f7cf3a593eede7a94d0cc0c5",
    "distinct": true,
    "message": "nav",
    "timestamp": "2014-11-28T17:17:21+03:00",
    "url": "https://github.com/Pavkazzz/flask-blog/commit/24d9b5d6c1e44928f7cf3a593eede7a94d0cc0c5",
    "author": {
      "name": "Pavka",
      "email": "pavkazzz@mail.ru",
      "username": "Pavkazzz"
    },
    "committer": {
      "name": "Pavka",
      "email": "pavkazzz@mail.ru",
      "username": "Pavkazzz"
    },
    "added": [

    ],
    "removed": [
      "1.txt"
    ],
    "modified": [
      "templates/nav.html",
      "web.py"
    ]
  },
  "repository": {
    "id": 27255626,
    "name": "flask-blog",
    "full_name": "Pavkazzz/flask-blog",
    "owner": {
      "name": "Pavkazzz",
      "email": "Pavkazzz@mail.ru"
    },
    "private": true,
    "html_url": "https://github.com/Pavkazzz/flask-blog",
    "description": "Практика ИСИС Караваев П-2-11",
    "fork": false,
    "url": "https://github.com/Pavkazzz/flask-blog",
    "forks_url": "https://api.github.com/repos/Pavkazzz/flask-blog/forks",
    "keys_url": "https://api.github.com/repos/Pavkazzz/flask-blog/keys{/key_id}",
    "collaborators_url": "https://api.github.com/repos/Pavkazzz/flask-blog/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/Pavkazzz/flask-blog/teams",
    "hooks_url": "https://api.github.com/repos/Pavkazzz/flask-blog/hooks",
    "issue_events_url": "https://api.github.com/repos/Pavkazzz/flask-blog/issues/events{/number}",
    "events_url": "https://api.github.com/repos/Pavkazzz/flask-blog/events",
    "assignees_url": "https://api.github.com/repos/Pavkazzz/flask-blog/assignees{/user}",
    "branches_url": "https://api.github.com/repos/Pavkazzz/flask-blog/branches{/branch}",
    "tags_url": "https://api.github.com/repos/Pavkazzz/flask-blog/tags",
    "blobs_url": "https://api.github.com/repos/Pavkazzz/flask-blog/git/blobs{/sha}",
    "git_tags_url": "https://api.github.com/repos/Pavkazzz/flask-blog/git/tags{/sha}",
    "git_refs_url": "https://api.github.com/repos/Pavkazzz/flask-blog/git/refs{/sha}",
    "trees_url": "https://api.github.com/repos/Pavkazzz/flask-blog/git/trees{/sha}",
    "statuses_url": "https://api.github.com/repos/Pavkazzz/flask-blog/statuses/{sha}",
    "languages_url": "https://api.github.com/repos/Pavkazzz/flask-blog/languages",
    "stargazers_url": "https://api.github.com/repos/Pavkazzz/flask-blog/stargazers",
    "contributors_url": "https://api.github.com/repos/Pavkazzz/flask-blog/contributors",
    "subscribers_url": "https://api.github.com/repos/Pavkazzz/flask-blog/subscribers",
    "subscription_url": "https://api.github.com/repos/Pavkazzz/flask-blog/subscription",
    "commits_url": "https://api.github.com/repos/Pavkazzz/flask-blog/commits{/sha}",
    "git_commits_url": "https://api.github.com/repos/Pavkazzz/flask-blog/git/commits{/sha}",
    "comments_url": "https://api.github.com/repos/Pavkazzz/flask-blog/comments{/number}",
    "issue_comment_url": "https://api.github.com/repos/Pavkazzz/flask-blog/issues/comments/{number}",
    "contents_url": "https://api.github.com/repos/Pavkazzz/flask-blog/contents/{+path}",
    "compare_url": "https://api.github.com/repos/Pavkazzz/flask-blog/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/Pavkazzz/flask-blog/merges",
    "archive_url": "https://api.github.com/repos/Pavkazzz/flask-blog/{archive_format}{/ref}",
    "downloads_url": "https://api.github.com/repos/Pavkazzz/flask-blog/downloads",
    "issues_url": "https://api.github.com/repos/Pavkazzz/flask-blog/issues{/number}",
    "pulls_url": "https://api.github.com/repos/Pavkazzz/flask-blog/pulls{/number}",
    "milestones_url": "https://api.github.com/repos/Pavkazzz/flask-blog/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/Pavkazzz/flask-blog/notifications{?since,all,participating}",
    "labels_url": "https://api.github.com/repos/Pavkazzz/flask-blog/labels{/name}",
    "releases_url": "https://api.github.com/repos/Pavkazzz/flask-blog/releases{/id}",
    "created_at": 1417158409,
    "updated_at": "2014-11-28T14:15:11Z",
    "pushed_at": 1417184276,
    "git_url": "git://github.com/Pavkazzz/flask-blog.git",
    "ssh_url": "git@github.com:Pavkazzz/flask-blog.git",
    "clone_url": "https://github.com/Pavkazzz/flask-blog.git",
    "svn_url": "https://github.com/Pavkazzz/flask-blog",
    "homepage": "",
    "size": 0,
    "stargazers_count": 0,
    "watchers_count": 0,
    "language": "JavaScript",
    "has_issues": true,
    "has_downloads": true,
    "has_wiki": true,
    "has_pages": false,
    "forks_count": 0,
    "mirror_url": null,
    "open_issues_count": 0,
    "forks": 0,
    "open_issues": 0,
    "watchers": 0,
    "default_branch": "master",
    "stargazers": 0,
    "master_branch": "master"
  },
  "pusher": {
    "name": "Pavkazzz",
    "email": "Pavkazzz@mail.ru"
  },
  "sender": {
    "login": "Pavkazzz",
    "id": 3702034,
    "avatar_url": "https://avatars.githubusercontent.com/u/3702034?v=3",
    "gravatar_id": "",
    "url": "https://api.github.com/users/Pavkazzz",
    "html_url": "https://github.com/Pavkazzz",
    "followers_url": "https://api.github.com/users/Pavkazzz/followers",
    "following_url": "https://api.github.com/users/Pavkazzz/following{/other_user}",
    "gists_url": "https://api.github.com/users/Pavkazzz/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/Pavkazzz/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/Pavkazzz/subscriptions",
    "organizations_url": "https://api.github.com/users/Pavkazzz/orgs",
    "repos_url": "https://api.github.com/users/Pavkazzz/repos",
    "events_url": "https://api.github.com/users/Pavkazzz/events{/privacy}",
    "received_events_url": "https://api.github.com/users/Pavkazzz/received_events",
    "type": "User",
    "site_admin": false
  }
}"""
    print _validate_signature('sha1=7b7f2b681dd204480d128bce6c0e9af204ffcb49', json.replace(' ', '').replace('\n', ''))
