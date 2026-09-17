import pytest
from pages.social_media import socialmedia

def  test_social_media_links(page):
    social_media_page = socialmedia(page)
    social_media_page.socialmediapageclick()
    