from pathlib import Path
from playwright.sync_api import sync_playwright

AUTH_FILE = Path(
    r"C:\Users\rimjh\Dreamhouse\utils\cookies.json"
)

LOGIN_URL = "https://login.salesforce.com"
HOME_URL = (
    "https://orgfarm-e04209301e-dev-ed.develop.lightning.force.com/"
    "lightning/page/home"
)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False ,  args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    # Open Salesforce login
    page.goto(LOGIN_URL)

    input(
        "Complete login and MFA manually. "
        "Wait until Salesforce Home opens, then press Enter here..."
    )

    # Display the page you are currently on
    print("Current URL:", page.url)

    # Check whether you have reached Salesforce Home
    if "/lightning/page/home" not in page.url:
        print("Salesforce Home was not detected.")
        print("Open Salesforce Home manually in this browser.")
        input("After Home opens, press Enter to continue...")

    print("URL before saving:", page.url)

    # Create the folder if it does not exist
    AUTH_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Save cookies and supported browser storage
    context.storage_state(path=str(AUTH_FILE))

    print("Authentication state saved at:", AUTH_FILE)

    browser.close()
