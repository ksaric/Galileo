__author__ = 'ksaric'
# -*- coding: utf-8 -*-

from app import db


class Network(db.Model):
    __tablename__ = 'network'

    id = db.Column(db.Integer, db.Sequence('%s_seq' % __tablename__), primary_key=True)
    name = db.Column(db.String(32), unique=True)
    note = db.Column(db.String(32))

    def __init__(self, name, note):
        self.name = name
        self.note = note


class Computer(db.Model):
    __tablename__ = 'computer'
    id = db.Column(db.Integer, db.Sequence('%s_seq' % __tablename__), primary_key=True)
    name = db.Column(db.String(32))
    ip_address = db.Column(db.String(32))

    network_id = db.Column(db.Integer, db.ForeignKey('network.id'))
    network = db.relationship(
        Network,
        backref=db.backref('computers',
                           uselist=True,
                           lazy='dynamic',
                           cascade='delete,all'))

    db.UniqueConstraint(
        'network.name',
        'name',
        name='cmp_net_uk'
    )


class Port(db.Model):
    __tablename__ = 'port'
    id = db.Column(db.Integer, db.Sequence('%s_seq' % __tablename__), primary_key=True)
    pnumber = db.Column(db.Integer)
    info = db.Column(db.String(32))
    data = db.Column(db.String(2000))
    protocol = db.Column(db.String(32))

    computer_id = db.Column(db.Integer, db.ForeignKey('computer.id'))
    computer = db.relationship(
        Computer,
        backref=db.backref('ports',
                           uselist=True,
                           lazy='dynamic',
                           cascade='delete,all'))

    db.UniqueConstraint(
        'computer.network.name',
        'computer.ip_address',
        'name',
        name='port_cmp_uk'
    )


class Database(db.Model):
    __tablename__ = 'database'
    id = db.Column(db.Integer, db.Sequence('%s_seq' % __tablename__), primary_key=True)

    name = db.Column(db.String(32))
    port = db.Column(db.String(32))
    user = db.Column(db.String(32))
    passw = db.Column(db.String(32))

    computer_id = db.Column(db.Integer, db.ForeignKey('computer.id'))
    computer = db.relationship(
        Computer,
        backref=db.backref('databases',
                           uselist=True,
                           lazy='dynamic',
                           cascade='delete,all'))

    db.UniqueConstraint(
        'computer.network.name',
        'computer.ip_address',
        'name',
        name='db_cmp_uk'
    )


class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, db.Sequence('%s_seq' % __tablename__), primary_key=True)

    username = db.Column(db.String(32))
    account_status = db.Column(db.String(32))
    default_tablespace = db.Column(db.String(32))
    temp_tablespace = db.Column(db.String(32))

    database_id = db.Column(db.Integer, db.ForeignKey('database.id'))
    database = db.relationship(
        Database,
        backref=db.backref('users',
                           uselist=True,
                           lazy='dynamic',
                           cascade='delete,all'))

    db.UniqueConstraint(
        'database.computer.network.name',
        'database.computer.ip_address',
        'database.name',
        'username',
        name='user_db_cmp_uk'
    )


class Tablespaces(db.Model):
    __tablename__ = 'tablespace'
    id = db.Column(db.Integer, db.Sequence('%s_seq' % __tablename__), primary_key=True)

    name = db.Column(db.String(32))
    status = db.Column(db.String(32))
    default_tablespace = db.Column(db.String(32))
    temp_tablespace = db.Column(db.String(32))

    database_id = db.Column(db.Integer, db.ForeignKey('database.id'))
    database = db.relationship(
        Database,
        backref=db.backref('tablespaces',
                           uselist=True,
                           lazy='dynamic',
                           cascade='delete,all'))

    db.UniqueConstraint(
        'database.computer.network.name',
        'database.computer.ip_address',
        'database.name',
        'name',
        name='user_db_cmp_uk'
    )


class Documents(db.Model):
    __tablename__ = 'document'
    id = db.Column(db.Integer, db.Sequence('%s_seq' % __tablename__), primary_key=True)

    name = db.Column(db.String(32))
    user = db.Column(db.String(32))

    def __init__(self, name, user):
        self.name = name
        self.user = user