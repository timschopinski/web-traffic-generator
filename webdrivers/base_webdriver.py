import os
from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


class BaseWebDriver(ABC):
    @classmethod
    @abstractmethod
    def get(cls, *args, **kwargs) -> webdriver:
        ...

    @staticmethod
    def _validate_executable_path(executable_path: str) -> None:
        if not os.path.exists(executable_path):
            raise ValueError(f"The binary path does not exist.")

    @staticmethod
    def _get_options(
        options: ChromeOptions | FirefoxOptions, *args
    ) -> ChromeOptions | FirefoxOptions:
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        options.add_argument("--start-fullscreen")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 "
            "Safari/537.36 "
        )
        options.add_argument("--hide-scrollbars")
        options.add_argument("--enable-logging")
        options.add_argument("--log-level=0")
        options.add_argument("--incognito")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("disable-infobars")

        [options.add_argument(argument) for argument in args]
        return options

    @staticmethod
    def _set_viewport_size(wd: webdriver, width: int, height: int) -> None:
        window_size = wd.execute_script(
            """
            return [window.outerWidth - window.innerWidth + arguments[0],
              window.outerHeight - window.innerHeight + arguments[1]];
            """,
            width,
            height,
        )
        wd.set_window_size(*window_size)

    @staticmethod
    def _set_chrome_property(wd: webdriver):
        wd.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {
                "source": 'chrome = { "app": { "isInstalled": false }, "webstore": { "onInstallStageChanged": {}, '
                '"onDownloadProgress": {} }, "runtime": { "PlatformOs": { "MAC": "mac", "WIN": "win", '
                '"ANDROID": "android", "CROS": "cros", "LINUX": "linux", "OPENBSD": "openbsd" }, '
                '"PlatformArch": { "ARM": "arm", "X86_32": "x86-32", "X86_64": "x86-64" }, '
                '"PlatformNaclArch": { "ARM": "arm", "X86_32": "x86-32", "X86_64": "x86-64" }, '
                '"RequestUpdateCheckStatus": { "THROTTLED": "throttled", "NO_UPDATE": "no_update", '
                '"UPDATE_AVAILABLE": "update_available" }, "OnInstalledReason": { "INSTALL": "install", '
                '"UPDATE": "update", "CHROME_UPDATE": "chrome_update", "SHARED_MODULE_UPDATE": '
                '"shared_module_update" }, "OnRestartRequiredReason": { "APP_UPDATE": "app_update", '
                '"OS_UPDATE": "os_update", "PERIODIC": "periodic" } } };window.chrome = { "app": { '
                '"isInstalled": false }, "webstore": { "onInstallStageChanged": {}, "onDownloadProgress": {'
                '} }, "runtime": { "PlatformOs": { "MAC": "mac", "WIN": "win", "ANDROID": "android", '
                '"CROS": "cros", "LINUX": "linux", "OPENBSD": "openbsd" }, "PlatformArch": { "ARM": "arm", '
                '"X86_32": "x86-32", "X86_64": "x86-64" }, "PlatformNaclArch": { "ARM": "arm", '
                '"X86_32": "x86-32", "X86_64": "x86-64" }, "RequestUpdateCheckStatus": { "THROTTLED": '
                '"throttled", "NO_UPDATE": "no_update", "UPDATE_AVAILABLE": "update_available" }, '
                '"OnInstalledReason": { "INSTALL": "install", "UPDATE": "update", "CHROME_UPDATE": '
                '"chrome_update", "SHARED_MODULE_UPDATE": "shared_module_update" }, '
                '"OnRestartRequiredReason": { "APP_UPDATE": "app_update", "OS_UPDATE": "os_update", '
                '"PERIODIC": "periodic" } } };window.navigator.chrome = { "app": { "isInstalled": false }, '
                '"webstore": { "onInstallStageChanged": {}, "onDownloadProgress": {} }, "runtime": { '
                '"PlatformOs": { "MAC": "mac", "WIN": "win", "ANDROID": "android", "CROS": "cros", '
                '"LINUX": "linux", "OPENBSD": "openbsd" }, "PlatformArch": { "ARM": "arm", '
                '"X86_32": "x86-32", "X86_64": "x86-64" }, "PlatformNaclArch": { "ARM": "arm", '
                '"X86_32": "x86-32", "X86_64": "x86-64" }, "RequestUpdateCheckStatus": { "THROTTLED": '
                '"throttled", "NO_UPDATE": "no_update", "UPDATE_AVAILABLE": "update_available" }, '
                '"OnInstalledReason": { "INSTALL": "install", "UPDATE": "update", "CHROME_UPDATE": '
                '"chrome_update", "SHARED_MODULE_UPDATE": "shared_module_update" }, '
                '"OnRestartRequiredReason": { "APP_UPDATE": "app_update", "OS_UPDATE": "os_update", '
                '"PERIODIC": "periodic" } } }; '
            },
        )
        wd.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {
                "source": "const originalQuery = window.navigator.permissions.query;return "
                "window.navigator.permissions.query = (parameters) => (parameters.name === 'notifications' "
                "? Promise.resolve({ state: Notification.permission }) :originalQuery(parameters));}); "
            },
        )

    @staticmethod
    def _set_navigator_langauge(wd: webdriver):
        wd.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {
                "source": "Object.defineProperty(navigator, 'languages', {get: () => ['pl-PL', 'pl', 'en-US', 'en'],});"
            },
        )

    @staticmethod
    def _set_plugins_property(wd: webdriver):
        wd.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {
                "source": "Object.defineProperty(navigator, 'plugins', {get: () => { var ChromiumPDFPlugin = {}; "
                "ChromiumPDFPlugin.__proto__ = PluginArray.prototype;return [ChromiumPDFPlugin];},}); "
            },
        )

    @staticmethod
    def _set_navigator_proto(wd: webdriver):
        wd.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {
                "source": "const newProto = navigator.__proto__;"
                "delete newProto.webdriver;"
                "navigator.__proto__ = newProto;"
            },
        )

    @staticmethod
    def _set_webdriver_property(wd: webdriver):
        wd.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )
