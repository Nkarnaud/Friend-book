# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 17:16:09 2019

@author: nkeumo
"""


from flask import Blueprint, jsonify, request, render_template

from project.models.models import FriendBook
from project import db
from sqlalchemy import exc
from project.api.utils import authenticate


friends_blueprint = Blueprint('friends', __name__, template_folder='../templates')


@friends_blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@friends_blueprint.route('/friends/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

@friends_blueprint.route('/auth/login', methods=['POST'])
def login_user():
    # get post data
    post_data = request.get_json()
    response_object = {
        'status': 'fail',
        'message': 'Invalid payload.'
    }
    if not post_data:
        return jsonify(response_object), 400
    email = post_data.get('email')
    password = post_data.get('password')
    try:
        # fetch the user data
        friend = FriendBook.query.filter_by(email=email).first()
        if friend and bcrypt.check_password_hash(friend.password, password):
            auth_token = friend.encode_auth_token(friend.id)
            if auth_token:
                response_object['status'] = 'success'
                response_object['message'] = 'Successfully logged in.'
                response_object['auth_token'] = auth_token.decode()
                return jsonify(response_object), 200
        else:
            response_object['message'] = 'User does not exist.'
            return jsonify(response_object), 404
    except Exception as e:
        response_object['message'] = 'Try again.'
        return jsonify(response_object), 500


@friends_blueprint.route('/auth/logout', methods=['GET'])
@authenticate
def logout_user(resp):
    auth_header = request.headers.get('Authorization')
    response_object = {
        'status': 'fail',
        'message': 'Provide a valid auth token.'
        }
    if auth_header:
        auth_token = auth_header.split(' ')[1]
        resp = User.decode_auth_token(auth_token)
        if not isinstance(resp, str):
            response_object['status'] = 'success'
            response_object['message'] = 'Successfully logged out.'
            return jsonify(response_object), 200
        else:
            response_object['message'] = resp
            return jsonify(response_object), 401
    else:
        return jsonify(response_object), 403



@friends_blueprint.route('/friends/add_friends', methods=['POST'])
#@authenticate
def add_friends(resp):
    # get post data
    post_data = request.get_json()
    response_object = {
        'status': 'fail',
        'message': 'Invalid payload.'
    }
    try:
        # check for existing friends
        friend = FriendBook.query.filter(FriendBook.email == post_data.get('email')).first()
        if not friend:
            # add new profile to db
            new_friend = FriendBook(
                firstname = post_data.get('firstname'),
                lastname = post_data.get('lastname'),
                email = post_data.get('email'),
                dateofbirth = post_data.get('dateofbirth'),
                gender=post_data.get('gender'),
                tell=post_data.get('tell'),
            )
            db.session.add(new_friend)
            db.session.commit()
            # generate auth token
            auth_token = friend.encode_auth_token(friend.id)
            response_object['status'] = 'success'
            response_object['message'] = 'User personal data was updated.'
            response_object['auth_token'] = auth_token.decode()
            return jsonify(response_object), 201
        else:
            response_object['message'] = 'Sorry. This Friend exists in our system.'
            return jsonify(response_object), 400
    # handler errors
    except (exc.IntegrityError, ValueError) as e:
        db.session.rollback()
        return jsonify(response_object), 400

@friends_blueprint.route('/friends/<id>', methods=['GET'])
#@authenticate
def get_single_firend(id):
    """Get    single    user    details"""
    response_object = {
        'status': 'fail',
        'message': 'Invalid payload.'
    }
    friend = FriendBook.query.filter_by(id=id).first()
    try:
        if friend:
            response_object = {
                'status': 'success',
                'data': {
                    'firstname': friend.firstname,
                    'lastname': friend.lastname,
                    'dateofbirth': friend.dateofbirth,
                    'email': friend.email,
                    'gender':friend.gender,
                    'gov_id': friend.tell
                }
            }
            return jsonify(response_object), 200
        else:
            response_object ={
                'status' : 'fail',
                'message': 'user does not exists.'}
            return jsonify(response_object), 400
    except exc.IntegrityError as e:
        db.session.rollback()
        return jsonify(response_object), 400

@friends_blueprint.route('/friends/lists', methods=['GET'])
#@authenticate
def get_all_customer():
    # This function provide the list of all customers in the system
        response_object = {
            'status': 'success',
            'data': {
                'users': [friend.to_json_friends() for friend in FriendBook.query.all()]
            }
        }
        return jsonify(response_object), 200


@friends_blueprint.route('/friends/delete/<id>', methods=['DELETE'])
#@authenticate
def delete(id):
    """To delete a user in the systeme"""
    response_object = {
        'status': 'fail',
        'message': 'Sorry. The customer does not exists'
    }
    friend = FriendBook.query.get(id)
    if friend:
        try:
            db.session.delete(friend)
            response_object = {'status': 'deleted', 
            'message': 'The customer has been deleted'}
            db.session.commit()
            return response_object, 200
        except Exception as e:
            return jsonify({"message": str(e)}), 500
    else:
        return jsonify(response_object), 400

