from __future__ import annotations

from .imports import lazy_import
from .version import version as __version__  # noqa: F401


__all__ = [
    "AbortHandshake",
    "basic_auth_protocol_factory",
    "BasicAuthWebSocketServerProtocol",
    "broadcast",
    "ClientProtocol",
    "connect",
    "ConnectionClosed",
    "ConnectionClosedError",
    "ConnectionClosedOK",
    "Data",
    "DuplicateParameter",
    "ExtensionName",
    "ExtensionParameter",
    "InvalidHandshake",
    "InvalidHeader",
    "InvalidHeaderFormat",
    "InvalidHeaderValue",
    "InvalidMessage",
    "InvalidOrigin",
    "InvalidParameterName",
    "InvalidParameterValue",
    "InvalidState",
    "InvalidStatus",
    "InvalidStatusCode",
    "InvalidUpgrade",
    "InvalidURI",
    "LoggerLike",
    "NegotiationError",
    "Origin",
    "parse_uri",
    "PayloadTooBig",
    "ProtocolError",
    "RedirectHandshake",
    "SecurityError",
    "serve",
    "ServerProtocol",
    "Subprotocol",
    "unix_connect",
    "unix_serve",
    "WebSocketClientProtocol",
    "WebSocketCommonProtocol",
    "WebSocketException",
    "WebSocketProtocolError",
    "WebSocketServer",
    "WebSocketServerProtocol",
    "WebSocketURI",
]

lazy_import(
    globals(),
    aliases={
        "auth": ".legacy",
        "basic_auth_protocol_factory": ".legacy.auth",
        "BasicAuthWebSocketServerProtocol": ".legacy.auth",
        "broadcast": ".legacy.protocol",
        "ClientProtocol": ".client",
        "connect": ".legacy.client",
        "unix_connect": ".legacy.client",
        "WebSocketClientProtocol": ".legacy.client",
        "Headers": ".datastructures",
        "MultipleValuesError": ".datastructures",
        "WebSocketException": ".exceptions",
        "ConnectionClosed": ".exceptions",
        "ConnectionClosedError": ".exceptions",
        "ConnectionClosedOK": ".exceptions",
        "InvalidHandshake": ".exceptions",
        "SecurityError": ".exceptions",
        "InvalidMessage": ".exceptions",
        "InvalidHeader": ".exceptions",
        "InvalidHeaderFormat": ".exceptions",
        "InvalidHeaderValue": ".exceptions",
        "InvalidOrigin": ".exceptions",
        "InvalidUpgrade": ".exceptions",
        "InvalidStatus": ".exceptions",
        "InvalidStatusCode": ".exceptions",
        "NegotiationError": ".exceptions",
        "DuplicateParameter": ".exceptions",
        "InvalidParameterName": ".exceptions",
        "InvalidParameterValue": ".exceptions",
        "AbortHandshake": ".exceptions",
        "RedirectHandshake": ".exceptions",
        "InvalidState": ".exceptions",
        "InvalidURI": ".exceptions",
        "PayloadTooBig": ".exceptions",
        "ProtocolError": ".exceptions",
        "WebSocketProtocolError": ".exceptions",
        "protocol": ".legacy",
        "WebSocketCommonProtocol": ".legacy.protocol",
        "ServerProtocol": ".server",
        "serve": ".legacy.server",
        "unix_serve": ".legacy.server",
        "WebSocketServerProtocol": ".legacy.server",
        "WebSocketServer": ".legacy.server",
        "Data": ".typing",
        "LoggerLike": ".typing",
        "Origin": ".typing",
        "ExtensionHeader": ".typing",
        "ExtensionParameter": ".typing",
        "Subprotocol": ".typing",
    },
    deprecated_aliases={
        "framing": ".legacy",
        "handshake": ".legacy",
        "parse_uri": ".uri",
        "WebSocketURI": ".uri",
    },
)
