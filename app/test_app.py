from unittest.mock import patch

import app as counter


def test_build_message():
    msg = counter.build_message(3, "abc123")
    assert msg == "Bonjour ! Cette page a été vue 3 fois. Je suis le conteneur abc123"


def test_index_increments_hits():
    client = counter.app.test_client()
    with patch.object(counter.redis, "incr", return_value=7) as incr:
        response = client.get("/")
    incr.assert_called_once_with("hits")
    assert "vue 7 fois" in response.get_data(as_text=True)
