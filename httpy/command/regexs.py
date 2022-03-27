class CommandRegexs:
    LIST = r".*[,].*"
    INCREMENT = r"\+{2}"
    DEINCREMENT = r"-{2}"
    RAND = r"rand[(][0-9]*[,][0-9]*[)]"
    READ = r"read[(][a-zA-Z0-9\/_\\\.]*[)]"
    TEXT = r".*"
