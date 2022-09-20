from pytest import fixture


@fixture
def chuck_api_response() -> dict:
    return {
        "icon_url": "https://chuck.host/img/avatar/chuck-norris.png",
        "id": "qE0gIoeCSiiQrraMRtResA",
        "url": "",
        "value": "Chuck Norris joke."
    }


@fixture
def dad_api_response() -> dict:
    return {
        "id": "R7UfaahVfFd",
        "joke": "Dad joke",
        "status": 200
    }
