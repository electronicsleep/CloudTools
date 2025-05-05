from time import monotonic

import logging
import subprocess

from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, Static, Collapsible, Label

logs = "test"

logging.basicConfig(filename='tui.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
log = logging.getLogger("main")
log.setLevel(logging.INFO)


class TimeDisplay(Static):
    """Display elapsed time"""

    start_time = reactive(monotonic)
    time = reactive(0.0)
    total = reactive(0.0)

    def on_mount(self) -> None:
        """Event handler called when widget is added to the app"""
        self.update_timer = self.set_interval(1 / 60, self.update_time, pause=True)

    def update_time(self) -> None:
        """Update time to current"""
        self.time = self.total + (monotonic() - self.start_time)

    def watch_time(self, time: float) -> None:
        """Called when the time attribute changes"""
        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        self.update(f"{hours:02,.0f}:{minutes:02.0f}:{seconds:05.2f}")

    def start(self) -> None:
        """Start (or resume) time"""
        self.start_time = monotonic()
        self.update_timer.resume()

    def stop(self):
        """Stop the time display update"""
        self.update_timer.pause()
        self.total += monotonic() - self.start_time
        self.time = self.total

    def reset(self):
        """Reset the time"""
        self.total = 0
        self.time = 0


class RunTask(Static):
    """Run Task widget"""

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed"""

        log = logging.getLogger("on_button_pressed")
        log.info("run_cmd1")
        run_cmd1_str = "ls -ltra *log"
        result = run_cmd(run_cmd1_str)
        log.info("RESULT: " + result)

        button_id = event.button.id
        time_display = self.query_one(TimeDisplay)
        if button_id == "start":
            log.info("RunTask: start")
            time_display.start()
            self.add_class("started")
        elif button_id == "stop":
            log.info("RunTask: stop")
            time_display.stop()
            self.remove_class("started")
        elif button_id == "reset":
            log.info("RunTask: reset")
            time_display.reset()

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch"""

        yield Button("RunTask1", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")
        yield TimeDisplay()


class RunTask2(Static):
    """Run Task widget"""

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed"""

        log = logging.getLogger("on_button_pressed")
        log.info("run_cmd2")
        run_cmd2_str = "ls *log"
        result = run_cmd(run_cmd2_str)
        log.info("RESULT: " + result)

        button_id = event.button.id
        time_display = self.query_one(TimeDisplay)
        if button_id == "start":
            log.info("RunTask: start")
            time_display.start()
            self.add_class("started")
        elif button_id == "stop":
            log.info("RunTask: stop")
            time_display.stop()
            self.remove_class("started")
        elif button_id == "reset":
            log.info("RunTask: reset")
            time_display.reset()

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch"""

        yield Button("RunTask2", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")
        yield TimeDisplay()


class CloudToolsApp(App):
    """A Textual app to run tasks"""

    CSS_PATH = "tui.tcss"

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit_tui", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app"""
        yield Header()
        yield Footer()
        yield ScrollableContainer(RunTask(), RunTask2(), id="timers")
        with Collapsible(collapsed=True, title="Logs"):
            yield Label(logs)

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode"""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def action_quit_tui(self) -> None:
        """An action to quit"""
        log.info("action_quit_tui exit")
        self.exit()


def run_cmd(cmd):
    """Run command using subprocess"""
    log = logging.getLogger("run_cmd")
    log.info(f"cmd:{cmd}")
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    result: str = ""
    if pipe.stdout is not None:
        for line in pipe.stdout:
            line = line.decode("utf-8")
            print(line.strip())
            result += line
    return result


if __name__ == "__main__":
    app = CloudToolsApp()
    app.run()
