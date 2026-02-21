from automation_api.core.config import get_settings

settings = get_settings()


class MeroShareAuth:
    LOGIN_URL = "https://meroshare.cdsc.com.np/"

    def __init__(self, page, timeout_ms=45000):
        self.page = page
        self.timeout_ms = timeout_ms

    def login(self):
        username = str(settings.meroshare_username).strip()
        password = str(settings.meroshare_password).strip()
        dp_value = str(settings.meroshare_dp)

        if not username or not password or not dp_value:
            raise RuntimeError("Missing MeroShare credentials or DP value")

        self.page.goto(
            self.LOGIN_URL, wait_until="domcontentloaded", timeout=self.timeout_ms
        )
        self.page.wait_for_selector("input#username", timeout=self.timeout_ms)

        # Click the Select2 container to open dropdown
        self.page.click("span.select2-selection")
        self.page.wait_for_selector("li.select2-results__option")
        self.page.click(f"li.select2-results__option:has-text('{dp_value}')")

        # Fill username & password
        self.page.fill("input#username", username)
        self.page.fill("input#password", password)

        # Submit login
        self.page.click("button[type='submit']")
        self.page.wait_for_load_state("networkidle", timeout=self.timeout_ms)

        # Check login success
        if self.page.locator("input#username").count() > 0:
            raise RuntimeError(
                "Login appears to have failed. Check credentials, DP, CAPTCHA, or OTP."
            )

        print("Login successful")
