class MeroShareAuth:
    LOGIN_URL = "https://meroshare.cdsc.com.np/"
    USERNAME_SELECTORS = (
        "input[name='username']",
        "input#username",
        "input[formcontrolname='username']",
    )
    PASSWORD_SELECTORS = (
        "input[name='password']",
        "input#password",
        "input[formcontrolname='password']",
    )
    DP_SELECTORS = (
        "select[name='dpId']",
        "select#selectBank",
        "select[formcontrolname='dpId']",
    )
    LOGIN_BUTTON_SELECTORS = (
        "button[type='submit']",
        "button:has-text('Login')",
    )

    def __init__(self, page, timeout_ms=45000):
        self.page = page
        self.timeout_ms = timeout_ms

    def _fill_first(self, selectors, value):
        for selector in selectors:
            if self.page.locator(selector).count() > 0:
                self.page.fill(selector, value)
                return
        raise RuntimeError(f"Unable to find input selector from: {selectors}")

    def _click_first(self, selectors):
        for selector in selectors:
            if self.page.locator(selector).count() > 0:
                self.page.click(selector)
                return
        raise RuntimeError(f"Unable to find button selector from: {selectors}")

    def _select_dp(self, dp_id):
        for selector in self.DP_SELECTORS:
            if self.page.locator(selector).count() > 0:
                target = str(dp_id)
                selected = self.page.select_option(selector, value=target)
                if selected:
                    return
                selected = self.page.select_option(selector, label=target)
                if selected:
                    return
                raise RuntimeError(f"DP option not found for: {target}")
        raise RuntimeError("Unable to find DP dropdown selector.")

    def login(self, username, password, dp_id=None):
        if not username or not password:
            raise ValueError("username and password are required")

        self.page.goto(
            self.LOGIN_URL,
            wait_until="domcontentloaded",
            timeout=self.timeout_ms,
        )

        if dp_id:
            self._select_dp(dp_id)

        self._fill_first(self.USERNAME_SELECTORS, username)
        self._fill_first(self.PASSWORD_SELECTORS, password)
        self._click_first(self.LOGIN_BUTTON_SELECTORS)

        self.page.wait_for_load_state("networkidle", timeout=self.timeout_ms)

        if "login" in self.page.url.lower():
            raise RuntimeError(
                "Login appears to have failed. Check credentials, DP ID, "
                "and whether CAPTCHA/manual step is required."
            )
