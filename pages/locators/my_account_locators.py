from playwright.sync_api import Locator, Page


class MyAccountLocators:
    def __init__(self, page: Page) -> None:
        self.heading: Locator = page.get_by_role(
            "heading", name="My Account", level=2, exact=True
        )
        self.my_orders_heading: Locator = page.get_by_role(
            "heading", name="My Orders", level=2, exact=True
        )
        self.affiliate_heading: Locator = page.get_by_role(
            "heading", name="My Affiliate Account", level=2, exact=True
        )
        self.newsletter_heading: Locator = page.get_by_role(
            "heading", name="Newsletter", level=2, exact=True
        )

        content = page.locator("#content")
        self.edit_account_link: Locator = content.get_by_role(
            "link", name="Edit your account information", exact=True
        )
        self.change_password_link: Locator = content.get_by_role(
            "link", name="Change your password", exact=True
        )
        self.address_book_link: Locator = content.get_by_role(
            "link", name="Modify your address book entries", exact=True
        )
        self.wish_list_link: Locator = content.get_by_role(
            "link", name="Modify your wish list", exact=True
        )
        self.order_history_link: Locator = content.get_by_role(
            "link", name="View your order history", exact=True
        )
        self.downloads_link: Locator = content.get_by_role(
            "link", name="Downloads", exact=True
        )
        self.reward_points_link: Locator = content.get_by_role(
            "link", name="Your Reward Points", exact=True
        )
        self.returns_link: Locator = content.get_by_role(
            "link", name="View your return requests", exact=True
        )
        self.transactions_link: Locator = content.get_by_role(
            "link", name="Your Transactions", exact=True
        )
        self.recurring_payments_link: Locator = content.get_by_role(
            "link", name="Recurring payments", exact=True
        )
        self.affiliate_link: Locator = content.get_by_role(
            "link", name="Register for an affiliate account", exact=True
        )
        self.newsletter_link: Locator = content.get_by_role(
            "link", name="Subscribe / unsubscribe to newsletter", exact=True
        )

        sidebar = page.locator("#column-right")
        self.sidebar_links: Locator = sidebar.get_by_role("link")
        self.sidebar_logout_link: Locator = sidebar.get_by_role(
            "link", name="Logout", exact=True
        )
