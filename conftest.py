import json
import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright
from config import Config
import time

AUTH_FILE = Path(
    r"C:\Users\rimjh\Dreamhouse\utils\cookies.json"
)

RESULTS_DIR = Path(__file__).resolve().parent / "test_results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

def has_saved_state():
    if not AUTH_FILE.is_file() or AUTH_FILE.stat().st_size == 0:
        return False

    try:
        with open(AUTH_FILE, "r", encoding="utf-8") as file:
            state = json.load(file)

        return bool(state.get("cookies") or state.get("origins"))

    except (json.JSONDecodeError, OSError):
        return False


@pytest.fixture(scope="session")
def app_config():
    return Config()


@pytest.fixture
def logged_in_chrome():
    print("Cookies file:", AUTH_FILE)
    print("File exists:", AUTH_FILE.is_file())

    if not has_saved_state():
        pytest.fail(
            f"No saved browser authentication state found at {AUTH_FILE}. "
            "Complete browser login and MFA once, then save storage_state."
        )

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--start-maximized"]
        )

        context = browser.new_context(
            storage_state=str(AUTH_FILE),
            viewport=None
        )

        

        page = context.new_page()

        # Maximize the active Windows window
        import pyautogui
        page.bring_to_front()
        pyautogui.hotkey("win", "up")

        time.sleep(2)

        yield page

        context.close()
        browser.close()

        

