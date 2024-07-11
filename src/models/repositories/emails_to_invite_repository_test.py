import uuid
import pytest
from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRpository

db_connection_handler.connect()
trip_id =  str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_registery_email():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRpository(conn)

    email_trips_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "email": "joao@email.com"
    }

    emails_to_invite_repository.registery_email(email_trips_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_find_emails_from_trip():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRpository(conn)

    emails = emails_to_invite_repository.find_emails_from_trip(trip_id)
