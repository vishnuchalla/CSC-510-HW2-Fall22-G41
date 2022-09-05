import json

class PrettyPrint:

    # Pretty prints the content of the given document.
    def __init__(self):
        pass
    
    # Method to faltten the json structure.
    def o(self, t):
        if type(t) is not list and type(t) is not dict:
            return str(t)
        def show(k, v):
            if not str(k).startswith("_"):
                v = self.o(v)
                return ":{0} {1}".format(k, v) if (type(t)is dict) else str(v)
        u = list()
        if(type(t) is list):
            for each in t:
                if(type(each) is str):
                    u.append(each)
                else:
                    k, v = list(each.items())[0]
                    u.append(":" + k + " " + show(k, v))
        elif(type(t) is dict):
            for k,v in t.items():
                u.append(show(k, v))
        u.sort()
        return "{" + " ".join(u) + "}"
    
    # Method to stringify the given document.
    def oo(self, t):
        print(self.o(t))
        return t

# Main method to test the functionality.
if __name__ == "__main__":
    pp = PrettyPrint()
    json1 = [{"test": "vchalls"}, {"again": "teset"}]
    json2 = ["james", {"test": {"sholay": "bond"}}, {"again": "crap"}]
    pp.oo(json1)
    pp.oo(json2)
    
