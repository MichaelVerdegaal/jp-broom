import regex as re


# Define Japanese brackets
# Ref: https://en.wikipedia.org/wiki/List_of_Japanese_typographic_symbols#Brackets_and_quotation_marks
LEFT_BRACKET_PATTERN = re.compile(r"[「『（〔［｛｟〈《【〖〘〚＜]", re.UNICODE)
RIGHT_BRACKET_PATTERN = re.compile(r"[」』）〕］｝｠〉》】〗〙〛＞]", re.UNICODE)
STANDARD_LEFT_BRACKET = "「"
STANDARD_RIGHT_BRACKET = "」"

# Define Japanese commas
# Ref: https://en.wikipedia.org/wiki/Japanese_punctuation#Comma
COMMA_PATTERN = re.compile(r"[、，﹐]", re.UNICODE)
STANDARD_COMMA = "、"

# Define Japanese double hyphens
# Ref: https://en.wikipedia.org/wiki/Japanese_punctuation#Double_hyphen
DOUBLE_HYPHEN_PATTERN = re.compile(r"[゠＝]", re.UNICODE)
STANDARD_DOUBLE_HYPHEN = "＝"

# Define Japanese ellipses
# Ref: https://en.wikipedia.org/wiki/Japanese_punctuation#Ellipsis
ELLIPSIS_PATTERN = re.compile(r"[…‥]", re.UNICODE)
STANDARD_ELLIPSIS = "…"

# Define full stops
# Ref: https://en.wikipedia.org/wiki/Japanese_punctuation#Full_stop
FULL_STOP_PATTERN = re.compile(r"[。．.]", re.UNICODE)
STANDARD_FULL_STOP = "。"