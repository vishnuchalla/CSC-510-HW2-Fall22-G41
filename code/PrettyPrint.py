import json


class PrettyPrint:

    # Pretty prints the content of the given document.
    def __init__(self):
        pass

    """
    Method to flatten the json structure.
    Run the test framework to see the logged output to check
    what all formats are handled.
    """

    def o(self, t):
        if type(t) is not list and type(t) is not dict:
            return str(t)

        def show(k, v):
            if not str(k).startswith("_"):
                v = self.o(v)
                return ":{0} {1}".format(k, v) if (type(t) is dict) else str(v)

        u = list()
        if type(t) is list:
            for each in t:
                if type(each) in (str, int, float):
                    u.append(str(each))
                else:
                    k, v = list(each.items())[0]
                    u.append(":" + k + " " + show(k, v))
        elif type(t) is dict:
            for k, v in t.items():
                u.append(show(k, v))
        return "{" + " ".join(u) + "}"

    # Method to stringify the given document.
    def oo(self, t):
        print(self.o(t))
        return t
