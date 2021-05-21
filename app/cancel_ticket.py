from database import Database


class CancelTicket():

    def __init__(self, pnr_no):
        self.pnr_no = pnr_no

    def get_cancel_ticket(self):
        print("Pnr_no:", self.pnr_no)
        db = Database()
        self.rows = db.all_from_pnr_details(self.pnr_no)
        print(self.rows)
        print(type(self.rows))
        print("pnr_id:", self.rows[0])
        #print("train id:", self.rows[5])
        self.pnr_id = self.rows[0]

        self.rows3 = db.all_from_booking_details(self.pnr_id)
        print(self.rows3)
        print(type(self.rows3))
        print("train_id:", self.rows3[1])
        self.t_id = self.rows3[1]


        self.train_no = self.rows[7]
        self.rows2 = db.all_from_train_Details(self.train_no)

        print(self.rows2)
        print(type(self.rows2))
        print("avail_seat", self.rows2[5])
        self.avail_seat = self.rows2[5]

        db.delete_row_from_booking_details(self.pnr_id)
        db.update_traindetail(self.avail_seat, self.train_no)
        print("Your Ticket is  Cancelled!!!")
        print("ThankYou !! Visit Again!! ")
        return self.pnr_no


if __name__ == "__main__":
    ticket_cancel = CancelTicket(1619445211108681)
    ticket_cancel.get_cancel_ticket()
