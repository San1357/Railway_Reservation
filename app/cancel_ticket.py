from database import Database


class CancelTicket():

    def __init__(self):
        self.db = Database()

    def get_cancel_ticket(self, pnr_no):
        pnr_details = self.db.all_from_pnr_details(pnr_no)
        pnr_id = pnr_details[0]
        booking_details = self.db.all_from_booking_details(pnr_id)
        t_id = booking_details[1]
        train_details = self.db.all_from_train_details(t_id)
        self.db.delete_row_from_booking_details(pnr_id)
        self.db.delete_row_from_pnr_details(pnr_id)
        avail_seat = train_details[5]
        self.db.update_seats_in_traindetail(avail_seat, t_id)
        print("Pnr_no:", pnr_no)
        print("pnr_details:", pnr_details)
        print("train_details:", train_details)
        print("booking_details:", booking_details)
        print("type_of_pnr_details:", type(pnr_details), "type_of_booking_details:", type(booking_details), "type_of_train_details:", type(train_details))
        print("pnr_id:", pnr_details[0], "train_id:", booking_details[1], "avail_seat", train_details[5])
        print("Your Ticket is  Cancelled!!!")
        print("ThankYou !! Visit Again!! ")


if __name__ == "__main__":
    ticket_cancel = CancelTicket()
    ticket_cancel.get_cancel_ticket(1621750529727682)
