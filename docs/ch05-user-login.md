# CH05 Provide User Logins

## Provide password hashing
```python
from werkzeug.security import generate_password_hash, check_password_hash
# [...]
class User(UserMixin, db.Model):
    # [...]
    def set_pwd(self, password):
        self.password_hash = generate_password_hash(pwd)
    def check_password(self, password):
        return check_password_hash(self.password_hash, pwd)
```

## Implement Flask-Login (LoginManager)
Install Flask-Login (`pip install flask-login`).  
From `app/__init__.py`:
```python
from flask_login import LoginManager
# [...]
app = Flask(__name__)
# [...]
login=LoginManager(app)
```

## Implement the UserMixin in the model
```python
from flask_login import UserMixin
# [...]
class User(UserMixin, db.Model):
    # [...]
```
## Provide the User Loader
Make Sure the User Loads to Memory
In the model:
```python
from app import login
# [...]
@login.user_loader
def load_user(id):
  return User.query.get(int(id))
```
## Log the User In and Out
Provide the login and the logout.
Let Flask-Login know what is the view func(`app/__init__.py`)
```python
login=LoginManager(app)
login.login_view='login'
```
## Protect your functions with `@login_required()` in `app/routes.py`.
```python
from flask_login import login_required
@app.route('/')
@app.route('/index')
@login_required
def index():
  # [...]
```
## Redirect back from the successful login to the requested page
Example of a URL: `/login?next=/index`
```python
from flask import request
from werkzeug.urls import url_parse
@app.route('/login', methods=['GET'])
def login():
    # [...]
    if form.validate_on_submit():
        # [...]
        login_user(user, remember_me=form.remember_me.data)
        next_page = request.args.get('next')
        if not next+page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('index'))
    # [...]
```
## Show the Logged In User in Templates
In the template(`app/templates/index.html`):
```html
<h1>Hi {{ current_user.username }}</h1>
```
Can remove the user argument from the view
```python
def index():
    # [...]
    return render_template('index.html', posts=posts, title="Home")
```
