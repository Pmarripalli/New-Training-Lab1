from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture
def client():
    activities_snapshot = deepcopy(app_module.activities)
    try:
        with TestClient(app_module.app, follow_redirects=False) as test_client:
            yield test_client
    finally:
        app_module.activities.clear()
        app_module.activities.update(activities_snapshot)