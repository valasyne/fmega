# CH05 Provide User Logins

## Provide password hashing
```python
from flask_login import UserMixin
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

Make Sure the User Loads to Memory
In the model:
```python
from app import login
# [...]
@login.user_loader
def load_user(id):
  return User.query.get(int(id))
```
