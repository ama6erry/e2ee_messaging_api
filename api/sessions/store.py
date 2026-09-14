# api/sessions/store.py
from dataclasses import dataclass


@dataclass
class SessionData:
    token: str
    user_id: str


# Temporary: replace with a DB query later.
_SESSIONS: dict[str, SessionData] = {
    "token1": SessionData("token1", "user1"),
}


def get_session(token: str) -> SessionData | None:
    return _SESSIONS.get(token)


def put_session(session: SessionData) -> None:
    _SESSIONS[session.token] = session


def clear_sessions() -> None:
    _SESSIONS.clear()