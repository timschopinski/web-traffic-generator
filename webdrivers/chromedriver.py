from selenium.webdriver.chrome.options import Options
from webdrivers.base_webdriver import BaseWebDriver
from selenium import webdriver


class ChromeWebdriver(BaseWebDriver):
    @classmethod
    def get(cls, executable_path: str, *args, **kwargs) -> webdriver:
        """
        This method returns the chrome webdriver instance. You can specify additional options using args
        """
        chrome_options = Options()
        cls._add_chrome_options_(chrome_options, args)
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--start-fullscreen")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument(
            "--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 "
            "Safari/537.36 "
        )
        chrome_options.add_argument("--hide-scrollbars")
        chrome_options.add_argument("--enable-logging")
        chrome_options.add_argument("--log-level=0")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_argument("disable-infobars")

        wd = webdriver.Chrome(options=chrome_options, executable_path=executable_path)
        cls._set_plugins_property(wd)
        cls._set_chrome_property(wd)
        cls._set_webdriver_property(wd)
        cls._set_navigator_langauge(wd)
        cls._set_navigator_proto(wd)
        return wd

    @staticmethod
    def _add_chrome_options_(chrome_options: Options, args: tuple):
        [chrome_options.add_argument(argument) for argument in args]

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
