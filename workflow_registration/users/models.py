import hashlib
from random import SystemRandom

from sqlalchemy.ext.hybrid import hybrid_property

from workflow_registration.data import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    _password = db.Column(db.LargeBinary(120))
    _salt = db.Column(db.String(120))

    sites = db.relationship('Workflow', back_populate='owner_ldap', lazy='dynamic')

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if self._salt is None:
            self._salt = bytes(SystemRandom.getrandbits(128))
        self._password = self._hash_password(value)

    def _hash_password(self, password):
        pwd = password.encode('utf-8')
        salt = bytes(self._salt)
        buff = hashlib.pbkdf2_hmac("sha512", pwd, salt, iterations=10000)
        return bytes(buff)

    def is_valid_password(self, password):
        new_hash = self._hash_password(password)
        return new_hash == self._password

    def __repr__(self):
        return "<User #{:d}>".format(self.id)


