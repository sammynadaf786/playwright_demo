import pytest
from pages.technology import technologies

@pytest.mark.smoke
def test_verify_cd(page):
    tech_obj1 = technologies(page)
    tech_obj1.verify_and_check_commerce()

@pytest.mark.smoke
def test_verify_md(page):
    tech_obj = technologies(page)
    tech_obj.verify_and_check_mobile()