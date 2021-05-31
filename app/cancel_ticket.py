from database import Database


class CancelTicket():

    def __init__(self):
        self.db = Database()

    def enter_pnr_no(self, pnr_no):
        self.pnr_no = pnr_no
        print("pnr_no", self.pnr_no)
        self.pnr_details = self.db.all_from_pnr_details([self.pnr_no])
        return self.pnr_no

    def get_cancel_ticket(self):
        print("pnr:", self.pnr_no)
        pnr_uuid = self.pnr_details[0]
        booking_details = self.db.all_from_booking_details(pnr_uuid)
        train_uuid = booking_details[1]
        train_details = self.db.all_from_train_details(train_uuid)
        avail_seat = train_details[5]
        self.db.delete_row_from_booking_details(pnr_uuid)
        self.db.delete_row_from_pnr_details(pnr_uuid)
        self.db.update_seats_in_train_details(avail_seat, train_uuid)
        print("Pnr_no:", self.pnr_no)
        print("pnr_details:", self.pnr_details)
        print("train_details:", train_details)
        print("booking_details:", booking_details)
        print("type_of_pnr_details:", type(self.pnr_details), "type_of_booking_details:", type(booking_details), "type_of_train_details:", type(train_details))
        print("pnr_id:", self.pnr_details[0], "train_id:", booking_details[1], "avail_seat", train_details[5])
        print("Your Ticket is  Cancelled!!!")
        print("ThankYou !! Visit Again!! ")

    def check_pnr_exist_or_not(self):
        if self.pnr_no not in self.pnr_details:
            self.status = "False"
        else:
            self.status = "True"

    def response_of_pnr(self):
        if self.status == "True":
            self.get_cancel_ticket()
            result = {
                "status": "deleted",
                "no of seat booked": str(0)
            }
        elif self.status == "False":
            result = {
                "status": "pnr doesnt exist",
            }
        print(result)
        return result


if __name__ == "__main__":
    ticket_cancel = CancelTicket()
    ticket_cancel.enter_pnr_no(1622362531927666)
    ticket_cancel.check_pnr_exist_or_not()
    ticket_cancel.response_of_pnr()
