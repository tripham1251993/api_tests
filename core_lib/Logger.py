import logging

MAP_LEVELS = {"ERROR": logging.ERROR, "WARNING": logging.WARNING, "INFO": logging.INFO, "DEBUG": logging.DEBUG}


class Logger:
    def __init__(self, prefix=None, log_level="INFO", is_date=True):
        self.prefix = prefix
        self.log_level = MAP_LEVELS[log_level.upper()]

        if is_date:
            logging.basicConfig(
                level=self.log_level,
                # format='%(asctime)s %(name)-16s %(levelname)-8s %(message)s')
                format="%(asctime)s %(name)s %(levelname)s %(message)s",
            )
        else:
            logging.basicConfig(level=self.log_level)
        logger = logging.getLogger(self.prefix)
        self.map_func = {"ERROR": logger.error, "WARNING": logger.warning, "INFO": logger.info, "DEBUG": logger.debug}

    def error(self, msg):
        self.log("ERROR", msg)

    def warning(self, msg):
        self.log("WARNING", msg)

    def info(self, msg):
        self.log("INFO", msg)

    def debug(self, msg):
        self.log("DEBUG", msg)

    def log(self, level, msg):
        self.map_func[level.upper()](msg)

    def error_in_box(self, msg):
        self.__write_in_box("ERROR", msg)

    def warning_in_box(self, msg):
        self.__write_in_box("WARNING", msg)

    def info_in_box(self, msg):
        self.__write_in_box("INFO", msg)

    def debug_in_box(self, msg):
        self.__write_in_box("DEBUG", msg)

    def __write_in_box(self, level, msg):
        lines = ["╔═" + "═" * len(str(msg)) + "═╗"]
        lines += ["║" + " %s " % msg + "║"]
        lines += ["╚═" + "═" * len(str(msg)) + "═╝"]
        list(map(self.map_func.get(level.upper()), lines))
