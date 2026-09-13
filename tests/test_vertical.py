import pytest
from pages.vertical import verticals

@pytest.mark.smoke
def test_verify_trading(page):
    trade = verticals(page)
    trade.click_verify_trading()

@pytest.mark.smoke
def test_verify_retail(page):
    retail = verticals(page)
    retail.click_verify_retail()

@pytest.mark.smoke
def test_verify_healthcare(page):
    hc = verticals(page)
    hc.click_verify_healthcare()

@pytest.mark.smoke
def test_verify_fintech(page):
    ft = verticals(page)
    ft.click_verify_fintech()

@pytest.mark.smoke
def test_verify_custom(page):
    ct = verticals(page)
    ct.click_verify_custom_app()


    