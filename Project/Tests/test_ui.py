import time
import pytest
from Project.Business.guide_page_object import GuidePage
from Project.Business.starting_page_object import StartingPage
from Project.Core.logger import get_logger

# Initialize the logger
logger = get_logger(__name__)
logger.info("UI logger initialized successfully!")
logger.info("This is an info message.")
logger.debug("This is a debug message.")


@pytest.mark.ui
def test_try_it(page):
    """Test to validate Try it section on starting page."""
    logger.debug("Starting log for test_try_it")
    home_page = StartingPage(page)
    home_page.navigate()
    assert home_page.result_textbox_elements.count() == 2
    home_page.get_try_it_result()
    time.sleep(2)  # We are waiting for the elements to appear.
    assert home_page.result_textbox_elements.count() == 17
    logger.debug("test_try_it successfully passed")


@pytest.mark.parametrize(
    "number, expected_text",
    [
        ("1", "/posts/1/comments"),
        ("2", "/albums/1/photos"),
        ("3", "/users/1/albums"),
        ("4", "/users/1/todos"),
        ("5", "/users/1/posts"),
    ],
)
@pytest.mark.ui
def test_names_of_routes(page, number, expected_text):
    """Test to validate available nested routes link names on guide page."""
    logger.debug(f"Starting log for test_try_it (input {number})")
    guide_page = GuidePage(page)
    guide_page.open_guide_page()
    assert guide_page.guide_header.inner_text() == "Guide"
    assert guide_page.get_list_item(number).inner_text() == expected_text
    logger.debug(f"test_try_it (input {number}) successfully passed")
