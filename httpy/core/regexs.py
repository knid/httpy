class CommandRegexs:
    _LIST = r".*[,].*"
    _INCREMENT = r"\+{2}"
    _DEINCREMENT = r"-{2}"
    _RAND = r"rand[(][0-9]*[,][0-9]*[)]"
    _READ = r"read[(][a-zA-Z0-9/\\\.]*[)]"
    _TEXT = r".*"
