from flask import jsonify, Blueprint, request

trips_routes_bp = Blueprint("trip_routes", __name__)

from src.controlers.trip_creator import TripCreator
from src.controlers.trip_finder import TripFinder
from src.controlers.trip_confirmer import TripConfirmer

from src.controlers.link_creator import LinkCreator
from src.controlers.link_finder import LinkFinder

from src.controlers.participant_creator import ParticipantCreator
from src.controlers.participants_finder import ParticipantsFinder
from src.controlers.participant_confirmer import ParticipantConfirmer

from src.controlers.activity_creator import ActivityCreator
from src.controlers.activity_finder import ActivityFinder

from src.models.repositories.trips_repository import TripsRpository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRpository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.participants_repository import ParticipantsRepository
from src.models.repositories.activities_repository import ActivitiesRepository

from src.models.settings.db_connection_handler import db_connection_handler

@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRpository(conn)
    emails_repository = EmailsToInviteRpository(conn)
    controller = TripCreator(trips_repository, emails_repository)

    response = controller.create(request.json)

    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>", methods=["GET"])
def find_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRpository(conn)
    controller = TripFinder(trips_repository)

    response = controller.find_trip_details(tripId)

    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/confirm", methods=["GET"])
def confirm_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRpository(conn)
    controller = TripConfirmer(trips_repository)

    response = controller.confirm(tripId)

    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/links", methods=["POST"])
def create_trip_link(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkCreator(links_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/links", methods=["GET"])
def find_trip_link(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkFinder(links_repository)

    response = controller.find(tripId)

    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/invites", methods=["POST"])
def invite_participants_to_trip(tripId):
    conn = db_connection_handler.get_connection()
    emails_repository = EmailsToInviteRpository(conn)
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantCreator(participants_repository,emails_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/activities", methods=["POST"])
def create_activity(tripId):
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    controller = ActivityCreator(activities_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/participants", methods=["GET"])
def find_participants_from_trip(tripId):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantsFinder(participants_repository)

    response = controller.find_participants_from_trip(tripId)

    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/activities", methods=["GET"])
def find_activities_from_trip(tripId):
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    controller = ActivityFinder(activities_repository)

    response = controller.find_activities_from_trip(tripId)
    
    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/participants/<participantId>/confirm", methods=["PATCH"])
def confirm_participant(participantId):
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantsRepository(conn)
    controller = ParticipantConfirmer(participant_repository)

    response = controller.confirm(participantId)

    return jsonify(response["body"]), response["status_code"]
