def bold(text):
    return "**" + str(text) + "**"


def code(text):
    return "```" + str(text) + "```"


def italicize(text):
    return "*" + str(text) + "*"


def get_method_name(method_inspect):
    return f"{method_inspect}()"


def tag_role(role_id):
    return f"<@&{role_id}>"


def tag_user(user_id):
    return f"<@{user_id}>"
