class MyASBAPages:
    def __init__(self, page):
        self.page = page
        self.timeout_ms = 20000

    def switch_tab(self, tab_name: str):
        """
        Navigate directly to My ASBA page using URL.
        """
        ASBA_URL = f"https://meroshare.cdsc.com.np/#/{tab_name}"
        self.page.goto(ASBA_URL, wait_until="domcontentloaded", timeout=self.timeout_ms)

        # Wait for the first company-list element, which indicates the page has loaded
        self.page.wait_for_selector("div.company-list", timeout=self.timeout_ms)
