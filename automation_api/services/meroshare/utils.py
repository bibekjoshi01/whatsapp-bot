def get_new_apply_for_issues(page):
    """
    Returns a list of new issues (not applied yet) in the "Apply for Issue" tab.
    Each item is a dict with company name, share type, and IPO info.
    """
    issues = []

    # Wait for the company list container to appear
    page.wait_for_selector("div.company-list", timeout=20000)

    company_blocks = page.locator("div.company-list")
    count = company_blocks.count()

    for i in range(count):
        block = company_blocks.nth(i)
        # Check if the Apply button exists in this block
        if block.locator("button.btn-issue").count() > 0:
            # Extract company info
            company_name = (
                block.locator("div.company-name span[tooltip='Company Name']")
                .inner_text()
                .strip()
            )
            share_type = (
                block.locator("div.company-name span.share-of-type")
                .inner_text()
                .strip()
            )
            sub_group = (
                block.locator("div.company-name span[tooltip='Sub Group']")
                .inner_text()
                .strip()
            )
            issues.append(
                {
                    "company_name": company_name,
                    "share_type": share_type,
                    "sub_group": sub_group,
                }
            )

    return issues
