import pytest
from pages.contact import contacts

@pytest.mark.smoke
def test_contact(page):
    cn = contacts(page)
    cn.fill_data_verify()