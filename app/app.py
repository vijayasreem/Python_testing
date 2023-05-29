Answer:

Flask API:

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'] 
        password = request.form['password'] 
        url = request.form['url'] 
        repository_name = request.form['repository_name']
        if authenticate(username, password, url, repository_name):
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
 
    return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form['title']
        username = request.form['username']
        url = request.form['url']
 
        if not validate_details(username, url):
            return redirect(url_for('home'))
 
        if request.form.get('edit'):
            edit_jira_details(title, username, url)
        elif request.form.get('delete'):
            delete_jira_details(title, username, url)
        elif request.form.get('add_more'):
            return redirect(url_for('configure_jira'))
 
        jira_details = get_jira_details()
        pagination = get_pagination()
 
    return render_template('home.html', jira_details=jira_details, pagination=pagination)

@app.route('/configure_jira', methods=['GET', 'POST'])
def configure_jira():
    if request.method == 'POST':
        username = request.form['username'] 
        password = request.form['password'] 
        url = request.form['url'] 
        repository_name = request.form['repository_name']
 
        response = java_api_validate(username, password, url, repository_name)
 
        if response == 'success':
            add_jira_details(username, url, repository_name)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('configure_jira'))
 
    return render_template('configure_jira.html')