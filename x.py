tickets = [
    {
        "id": "TK001",
        "issue": "Khong dang nhap duoc App",
        "customer": "Nguyen Van A",
        "commit_time": 30,
        "actual_time": 45,
        "difference": 15,
        "sla": "Cảnh báo"
    }
]

############################ PHAN LOAI SLA #####################################

def classify_sla(commit_time, actual_time):
    difference = int(actual_time) - int(commit_time)

    if difference < 0:
        return difference, "Hoàn hảo"
    elif difference == 0:
        return difference, "Đạt chuẩn"
    elif 1 <= difference < 20:
        return difference, "Cảnh báo"
    else:
        return difference, "Nghiêm trọng"


############################ HIEN THI #####################################

def display_tickets(ticket_list):
    if len(ticket_list) == 0:
        print("DANH SACH TICKET DANG RONG!")
        return

    print("-" * 130)
    print(
        f"{'STT':<5}"
        f"{'MA TK':<10}"
        f"{'NOI DUNG SU CO':<30}"
        f"{'KHACH HANG':<20}"
        f"{'CAM KET':<10}"
        f"{'THUC TE':<10}"
        f"{'CHENH LECH':<12}"
        f"{'SLA':<15}"
    )
    print("-" * 130)

    for index, value in enumerate(ticket_list, start=1):
        print(
            f"{index:<5}"
            f"{value['id']:<10}"
            f"{value['issue']:<30}"
            f"{value['customer']:<20}"
            f"{value['commit_time']:<10}"
            f"{value['actual_time']:<10}"
            f"{value['difference']:<12}"
            f"{value['sla']:<15}"
        )


############################ THEM TICKET #####################################

def add_ticket(ticket_list):

    while True:
        new_id = input("Nhap ma ticket: ").upper()

        if new_id == "":
            print("Ma ticket khong duoc de trong!")
            continue

        flag = 0

        for i in ticket_list:
            if i["id"] == new_id:
                flag = 1
                break

        if flag == 1:
            print("Ma ticket da ton tai!")
            continue

        break

    while True:
        new_issue = input("Nhap noi dung su co: ")

        if new_issue == "":
            print("Noi dung khong duoc de trong!")
            continue

        break

    while True:
        new_customer = input("Nhap ten khach hang: ").title()

        if new_customer == "":
            print("Ten khach hang khong duoc de trong!")
            continue

        break

    while True:
        try:
            new_commit = int(input("Nhap thoi gian cam ket (phut): "))

            if new_commit > 0:
                break

            print("Phai lon hon 0!")

        except ValueError:
            print("Yeu cau nhap so!")

    while True:
        try:
            new_actual = int(input("Nhap thoi gian thuc te (phut): "))

            if new_actual >= 0:
                break

            print("Phai >= 0!")

        except ValueError:
            print("Yeu cau nhap so!")

    difference, sla = classify_sla(new_commit, new_actual)

    ticket_list.append(
        {
            "id": new_id,
            "issue": new_issue,
            "customer": new_customer,
            "commit_time": new_commit,
            "actual_time": new_actual,
            "difference": difference,
            "sla": sla
        }
    )

    print("THEM TICKET THANH CONG!")


############################ CAP NHAT #####################################

def update_ticket(ticket_list):

    while True:
        ticket_id = input("Nhap ma ticket can cap nhat: ").upper()

        if ticket_id == "":
            print("Khong duoc de trong!")
            continue

        flag = None

        for i in ticket_list:
            if i["id"] == ticket_id:
                flag = i
                break

        if flag is None:
            print("Khong tim thay ticket!")
            continue

        break

    while True:
        new_issue = input("Nhap noi dung moi: ")

        if new_issue == "":
            print("Khong duoc de trong!")
            continue

        break

    while True:
        try:
            new_commit = int(input("Nhap thoi gian cam ket moi: "))

            if new_commit > 0:
                break

            print("Phai lon hon 0!")

        except ValueError:
            print("Yeu cau nhap so!")

    while True:
        try:
            new_actual = int(input("Nhap thoi gian thuc te moi: "))

            if new_actual >= 0:
                break

            print("Phai >= 0!")

        except ValueError:
            print("Yeu cau nhap so!")

    difference, sla = classify_sla(new_commit, new_actual)

    flag["issue"] = new_issue
    flag["commit_time"] = new_commit
    flag["actual_time"] = new_actual
    flag["difference"] = difference
    flag["sla"] = sla

    print("CAP NHAT THANH CONG!")


############################ XOA #####################################

def delete_ticket(ticket_list):

    while True:
        ticket_id = input("Nhap ma ticket can xoa: ").upper()

        if ticket_id == "":
            print("Khong duoc de trong!")
            continue

        flag = None

        for i in ticket_list:
            if i["id"] == ticket_id:
                flag = i
                break

        if flag is None:
            print("Khong tim thay ticket!")
            continue

        break

    question = input(
        "Ban co chac muon xoa ve ho tro nay khong? (Y/N): "
    ).lower()

    if question == "y":
        ticket_list.remove(flag)
        print("XOA THANH CONG!")
    else:
        print("HUY XOA!")


############################ TIM KIEM #####################################

def find_ticket(ticket_list):

    while True:

        choose = input("""
1. Tim theo ma ticket
2. Tim theo ten khach hang
3. Thoat
Chon:
""")

        match choose:

            case "1":

                while True:

                    ticket_id = input("Nhap ma can tim: ").upper()

                    if ticket_id == "":
                        print("Khong duoc de trong!")
                        continue

                    result = []

                    for i in ticket_list:
                        if i["id"] == ticket_id:
                            result.append(i)

                    if len(result) == 0:
                        print("Khong tim thay!")
                    else:
                        display_tickets(result)

                    break

            case "2":

                while True:

                    keyword = input(
                        "Nhap ten khach hang can tim: "
                    ).lower()

                    if keyword == "":
                        print("Khong duoc de trong!")
                        continue

                    result = []

                    for i in ticket_list:
                        if keyword in i["customer"].lower():
                            result.append(i)

                    if len(result) == 0:
                        print("Khong tim thay!")
                    else:
                        display_tickets(result)

                    break

            case "3":
                break

            case _:
                print("Lua chon khong hop le!")


############################ THONG KE #####################################

def statistic_ticket(ticket_list):

    perfect = 0
    standard = 0
    warning = 0
    serious = 0

    for i in ticket_list:

        if i["sla"] == "Hoàn hảo":
            perfect += 1

        elif i["sla"] == "Đạt chuẩn":
            standard += 1

        elif i["sla"] == "Cảnh báo":
            warning += 1

        else:
            serious += 1

    print("\n===== THONG KE SLA =====")
    print(f"Hoan hao     : {perfect}")
    print(f"Dat chuan    : {standard}")
    print(f"Canh bao     : {warning}")
    print(f"Nghiem trong : {serious}")


############################ TICKET MAX #####################################

def ticket_max_time(ticket_list):

    if len(ticket_list) == 0:
        print("Danh sach rong!")
        return

    max_ticket = ticket_list[0]

    for i in ticket_list:

        if i["actual_time"] > max_ticket["actual_time"]:
            max_ticket = i

    print("\nTICKET CO THOI GIAN XU LY LON NHAT")
    print(f"Ma ticket : {max_ticket['id']}")
    print(f"Su co     : {max_ticket['issue']}")
    print(f"Khach hang: {max_ticket['customer']}")
    print(f"Thuc te   : {max_ticket['actual_time']} phut")


############################ SAP XEP #####################################

def sort_ticket(ticket_list):

    if len(ticket_list) == 0:
        print("Danh sach rong!")
        return

    ticket_list.sort(
        key=lambda x: x["difference"],
        reverse=True
    )

    print("DA SAP XEP THEO MUC DO VI PHAM SLA GIAM DAN!")


############################ MENU #####################################

def main():

    while True:

        print("""
================ MENU ================

1. Hien thi danh sach ticket
2. Them ticket moi
3. Cap nhat ticket
4. Xoa ticket
5. Tim kiem ticket
6. Thong ke SLA
7. Tim ticket xu ly lau nhat
8. Sap xep ticket theo muc do vi pham
9. Thoat

======================================
""")

        choose = input("Nhap chuc nang: ")

        match choose:

            case "1":
                display_tickets(tickets)

            case "2":
                add_ticket(tickets)

            case "3":
                update_ticket(tickets)

            case "4":
                delete_ticket(tickets)

            case "5":
                find_ticket(tickets)

            case "6":
                statistic_ticket(tickets)

            case "7":
                ticket_max_time(tickets)

            case "8":
                sort_ticket(tickets)

            case "9":
                print("CAM ON BAN DA SU DUNG CHUONG TRINH!")
                break

            case _:
                print("Vui long nhap tu 1 -> 9!")


main()
