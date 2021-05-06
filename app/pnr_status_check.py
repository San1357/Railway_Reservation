from database import Database

class PnrChecker:
    def __init__(self):
        self.db = Database()

    def pnr_connect(self, pnr_nos):
        h = self.db.pnr_of_pnr_status(pnr_nos)
        f = ('Not confirmed', 'yes')
        j = ('confirmed', 'yes')
        #h = pnr_connect(pnr_nos)
        if h == f:
            print("h : ", h)
            print(f"{pnr_nos} is a valid Pnr number")
            result = {
                "PNR NUMBER": pnr_nos,
                "Status": "Valid",
                "CNF STATUS": "Not Confirmed",
                "Present": "This PNR number is present.",
                "Overall Status": False
            }

        if h == j:
            print("h : ", h)
            print(f"{pnr_nos} is a valid Pnr number")
            result = {
                "PNR NUMBER": pnr_nos,
                "Status": "Valid",
                "CNF STATUS": "Confirmed",
                "Present": "This PNR number is present.",
                "Overall Status": True
            }
        else:
            print(None)
            print(f"{pnr_nos} is Not a valid Pnr number")
            result = {
                "PNR NUMBER": pnr_nos,
                "Status": "Not Valid",
                "CNF STATUS": "Not Confirmed",
                "Present": "This PNR number is not present.",
                "Overall Status": None
            }
        print(result)
        return result


if __name__ == "__main__":
    s = PnrChecker()
    s.pnr_connect(9274018223)