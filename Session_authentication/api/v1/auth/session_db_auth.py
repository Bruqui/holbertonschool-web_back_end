#!/usr/bin/env python3
"""
SessionDBAuth module.
"""
from datetime import datetime, timedelta
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """
    SessionDBAuth class that stores sessions in a database.
    """

    def create_session(self, user_id=None):
        """
        Creates and stores a new instance of UserSession.
        """
        session_id = super().create_session(user_id)
        if not session_id:
            return None

        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Returns the User ID by requesting UserSession in the database.
        """
        if session_id is None:
            return None

        try:
            sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return None

        if not sessions or len(sessions) == 0:
            return None

        session = sessions[0]

        if self.session_duration <= 0:
            return session.user_id

        if not session.created_at:
            return None

        expiration_time = session.created_at + timedelta(
            seconds=self.session_duration)

        if datetime.now() > expiration_time:
            return None

        return session.user_id

    def destroy_session(self, request=None):
        """
        Destroys the UserSession based on the Session ID from the request.
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if not session_id:
            return False

        try:
            sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return False

        if not sessions or len(sessions) == 0:
            return False

        session = sessions[0]
        session.remove()
        return True
