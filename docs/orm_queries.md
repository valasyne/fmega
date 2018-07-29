# Various ORM Queries

Get a user
```python
user = User.query.filter_by(username=form.username.data).first()
```
