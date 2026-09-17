import pytest
from pages.about_us import about

@pytest.mark.smoke
def test_verify_about_us(page):
    ou = about(page)
    ou.click_about_us()
