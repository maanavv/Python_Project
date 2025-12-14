from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.widgets import Static, Header, Footer, Button
from textual.reactive import reactive
from datetime import datetime


# ─────────────────── CLOCK ───────────────────
class DigitalClock(Static):
    time = reactive("")

    def on_mount(self):
        self.set_interval(1, self.update_time)

    def update_time(self):
        self.time = datetime.now().strftime("%H:%M:%S")

    def render(self):
        return f"🕒 {self.time}"


# ─────────────────── POST OPEN VIEW ───────────────────
class PostViewer(Vertical):
    can_focus = True

    def show_post(self, title, body):
        self.clear_children()
        self.mount(Static(title, classes="open-title"))
        self.mount(Static(body, classes="open-body"))
        self.mount(Static("Comments", classes="open-comments"))

        for i in range(3):
            self.mount(
                Static(f"User{i+1}: This is a mock comment.", classes="comment")
            )

        self.mount(Static("[ ESC to go back ]", classes="back-hint"))

    def clear_children(self):
        for c in list(self.children):
            c.remove()


# ─────────────────── POST CARD ───────────────────
class PostCard(Static):
    def __init__(self, title: str, short: str, full: str):
        super().__init__()
        self.title = title
        self.short = short
        self.full = full
        self.likes = 0          
        self.comments = []      

    def compose(self) -> ComposeResult:
        with Vertical(classes="post-card"):

            with Horizontal():
                yield Static("LOGO", classes="post-logo")

                with Vertical(classes="post-text"):
                    yield Static(self.title, classes="post-title")
                    yield Static(self.short, classes="post-desc")

            with Horizontal(classes="post-footer"):
                yield Static("tag", classes="post-tag")
                yield Static("meta", classes="post-meta")
                yield Static("♥ 12  💬 3", classes="post-stats")
                yield Button("OPEN", id="open")

    def on_button_pressed(self, event):
        if event.button.id == "open":
            self.app.center.show_post(self.title, self.full)



# ─────────────────── CENTER FEED ───────────────────
class CenterFeed(VerticalScroll):
    can_focus = True

    def on_mount(self):
        self.viewer = PostViewer()
        self.show_feed()

    def clear_children(self):
        for c in list(self.children):
            c.remove()

    def show_feed(self):
        self.clear_children()
        self.mount(Static("PACKET STREAM", classes="title"))

        posts = [
            ("Post One", "Short description one",
             "Full content of post one.\nMore details here."),
            ("Post Two", "Short description two",
             "Full content of post two.\nMore details here."),
            ("Post Three", "Short description three",
             "Full content of post three.\nMore details here."),
        ]

        for p in posts:
            self.mount(PostCard(*p))

    def show_post(self, title, body):
        self.clear_children()
        self.mount(self.viewer)
        self.viewer.show_post(title, body)
        self.set_focus(self.viewer)
 

    def on_key(self, event):
        if event.key == "escape":
            self.show_feed()


# ─────────────────── LEFT PANEL (ALL BUTTONS) ───────────────────
class LeftPanel(Vertical):
    def compose(self) -> ComposeResult:
        yield Static("ASCII BANNER", classes="title")

        for item in [
            "Home", "Search", "Chats", "Notifications",
            "Post/Create", "Profile", "Settings", "Logout"
        ]:
            yield Button(item)


# ─────────────────── RIGHT PANEL ───────────────────
class RightPanel(Vertical):
    def compose(self) -> ComposeResult:
        yield Button("Add Widget")
        yield Button("Widget Settings")

        self.widget_area = Vertical()
        yield self.widget_area

        yield Static("Pending chats: 2", classes="side-box")
        yield Static("Latest notifications", classes="side-box")

    def on_mount(self):
        self.widget_area.mount(DigitalClock(classes="widget-box"))


# ─────────────────── APP ───────────────────
class CyberSocialApp(App):

    CSS = """
    Screen { background: white; color: black; }
    Button { margin-right: 1; }

    LeftPanel { width: 26; border: solid black; padding: 1; }
    CenterFeed { width: 1fr; border: solid black; padding: 1; }
    RightPanel { width: 30; border: solid black; padding: 1; }

    .title { text-style: bold; margin-bottom: 1; }

    .post-card {
        border: solid black;
        padding: 1;
        margin-bottom: 1;
    }

    .post-logo {
        width: 12;
        height: 5;
        border: solid black;
        content-align: center middle;
    }

    .post-text { padding-left: 1; }

    .post-title { text-style: bold; }
    .post-desc { }

    .post-footer {
        margin-top: 1;
    }

    .post-tag, .post-meta, .post-stats {
        border: solid black;
        padding: 0 1;
        margin-right: 1;
    }

    .comment {
        border: solid black;
        padding: 1;
        margin-bottom: 1;
    }

    .widget-box, .side-box {
        border: solid black;
        padding: 1;
        margin-bottom: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header(show_clock=False)

        with Horizontal():
            self.left = LeftPanel()
            self.center = CenterFeed()
            self.right = RightPanel()

            yield self.left
            yield self.center
            yield self.right

        yield Footer()

    def on_mount(self):
        self.set_focus(self.center)


if __name__ == "__main__":
    CyberSocialApp().run()