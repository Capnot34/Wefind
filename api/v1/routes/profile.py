from flask import Blueprint, request, jsonify
from models import User, Company
from flask_jwt_extended import jwt_required, get_jwt_identity

profile_bp = Blueprint('profile', __name__)


@profile_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    current_user = get_jwt_identity()

    if current_user['role'] == 'user':
        user = User.objects(id=current_user['id']).first()
        if user:
            return jsonify(user.to_json()), 200
    else:
        company = Company.objects(id=current_user['id']).first()

        if company:
            return jsonify(company.to_json()), 200

    return jsonify({"msg": "Profile not found"}), 404


@profile_bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    current_user = get_jwt_identity()
    data = request.get_json()
    user = User.objects(id=current_user['id']).first()

    if user:
        user.update(**data)
        return jsonify({"msg": "User profile updated"}), 200

    company = Company.objects(id=current_user['id']).first()

    if company:
        company.update(**data)
        return jsonify({"msg": "Company profile updated"}), 200

    return jsonify({"msg": "Profile not found"}), 404


# New route to fetch user profiles by ID for companies
@profile_bp.route("/user_profile/<user_id>", methods=["GET"])
@jwt_required()
def get_user_profile(user_id):
    current_user = get_jwt_identity()

    if current_user["role"] == "company":
        user = User.objects(id=user_id).first()
        if user:
            return jsonify(user.to_json()), 200

    return jsonify({"msg": "User profile not found or unauthorized"}), 404
