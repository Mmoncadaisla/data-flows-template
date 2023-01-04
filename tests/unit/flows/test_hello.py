import pytest
import logging
from dataflows.flows.hello_flow import hello

logger = logging.getLogger(__name__)


@pytest.mark.parametrize("user_input", ["World", "Prefect"])
def test_hello(user_input, caplog):
    # Given
    caplog.set_level(logging.INFO)

    # When
    hello(user_input=user_input)

    # Then
    assert f"Hello from Prefect, {user_input}! 🚀" in caplog.text
