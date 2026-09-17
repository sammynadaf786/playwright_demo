from pathlib import Path

import pytest
from pytest_html import extras
from playwright.sync_api import sync_playwright
from config import BASE_URL

@pytest.fixture
def page(request):
    p = sync_playwright().start()
    browser=p.chromium.launch(headless=False)
    videos_dir = Path("videos")
    videos_dir.mkdir(exist_ok=True)
    context = browser.new_context(
        ignore_https_errors=True,
        record_video_dir=str(videos_dir),
    )
    page = context.new_page()

    try:
        page.goto(BASE_URL)
        page.wait_for_load_state("load")
        yield page
    finally:
        context.close()
        request.node.video_path = str(page.video.path())
        browser.close()
        p.stop()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extras_list = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            file_name = screenshots_dir / f"{item.name}.png"

            page.screenshot(path=str(file_name))

            extras_list.append(extras.image(str(file_name)))

            if report.when == "call":
                item.call_report = report

    if report.when == "teardown":
        video_path = getattr(item, "video_path", None)
        if video_path and hasattr(item, "call_report"):
            item.call_report.extras.append(extras.video(video_path))

    report.extras = extras_list