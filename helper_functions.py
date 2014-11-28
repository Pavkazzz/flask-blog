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


def _validate_signature(self, data):
    sha_name, signature = self.headers['X-Hub-Signature'].split('=')
    if sha_name != 'sha1':
        return True

    # HMAC requires its key to be bytes, but data is strings.
    mac = hmac.new('pavka', msg=data, digestmod=hashlib.sha1)
    return hmac.compare_digest(mac.hexdigest(), signature)
