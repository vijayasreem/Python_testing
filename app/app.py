Flask API:

from flask import Flask, request, jsonify
from jira import JIRA

app = Flask(__name__)

@app.route('/configure_jira', methods=['GET', 'POST'])
def configure_jira():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        url = request.form.get('url')
        repo_name = request.form.get('repo_name')
        jira = JIRA(username, password, url, repo_name)
        if jira.authenticate():
            return jsonify({
                'result': 'Successfully configured Jira Software'
            })
        else:
            return jsonify({
                'result': 'Failed to configure Jira Software'
            })
    else:
        return jsonify({
            'result': 'Request method must be POST'
        })

@app.route('/list_jira', methods=['GET'])
def list_jira():
    title = request.args.get('title')
    user_name = request.args.get('user_name')
    url = request.args.get('url')
    action = request.args.get('action')
    show_entries = request.args.get('show_entries')
    pagination = request.args.get('pagination')
    jira_list = [
        {
            'title': title,
            'user_name': user_name,
            'url': url,
            'action': action
        }
    ]
    return jsonify({
        'show_entries': show_entries,
        'pagination': pagination,
        'jira_list': jira_list
    })

@app.route('/edit_jira', methods=['PUT'])
def edit_jira():
    title = request.form.get('title')
    user_name = request.form.get('user_name')
    url = request.form.get('url')
    jira_list = [
        {
            'title': title,
            'user_name': user_name,
            'url': url
        }
    ]
    return jsonify({
        'result': 'Successfully edited jira list',
        'jira_list': jira_list
    })

@app.route('/delete_jira', methods=['DELETE'])
def delete_jira():
    title = request.form.get('title')
    jira_list = [
        {
            'title': title
        }
    ]
    return jsonify({
        'result': 'Successfully deleted jira list',
        'jira_list': jira_list
    })

if __name__ == '__main__':
    app.run()