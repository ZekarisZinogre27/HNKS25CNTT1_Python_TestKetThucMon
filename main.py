class Booking:
    def __init__(self, id, customer_name, room_number, room_price, nights, service_fee, discount):
        self.id = id
        self.customer_name = customer_name
        self.room_number = room_number
        self.room_price = room_price
        self.nights = nights
        self.service_fee = service_fee
        self.discount = discount
        
        self.calculate_total_rent()
        self.classify_rent()
        
    def calculate_total_rent(self):
        total_rent = self.room_price * self.nights + self.service_fee - self.discount
        return total_rent
        
    def classify_rent(self):
        total_rent = self.calculate_total_rent()
        if total_rent < 1000000:
            rent_type = "Tiết kiệm"
        elif total_rent < 3000000:
            rent_type = "Tiêu chuẩn"
        elif total_rent < 7000000:
            rent_type = "Cao cấp"
        else:
            rent_type = "VIP"
        return rent_type  
        
    
class BookingManager(Booking):
    def __init__(self):
        self.bookings = []

    def add_booking(self):
        pass

    def show_all(self):
        print("================ DANH SÁCH ĐẶT PHÒNG ================")
        print(" Mã đặt phòng | Họ tên khách hàng | Số phòng | Giá phòng một đêm | Số đêm thuê | Phụ phí dịch vụ | Giảm giá | Tổng tiền thuê | Phân loại tiền thuê ")
        for i in self.bookings:
            total_rent = i.calculate_total_rent()
            rent_type = i.classify_rent()
            print(f"{i.id} | {i.customer_name} | {i.room_number} | {i.room_price} | {i.nights} | {i.service_fee} | {i.discount} | {total_rent} | {rent_type}")
        print("=====================================================")
        
    def update_booking(self):
        while True:
            if len(self.bookings) == 0:
                print("Danh sách đang rỗng.")
                break
            find_id = input("Nhập mã đặt bạn muốn tìm để cập nhật (Enter để thoát): ").strip().upper()
            if not find_id:
                break
            
            found = False
            for i in self.bookings:
                if find_id == i.id:
                    found = True
                    print("======== CHỌN CHỨC NĂNG CẬP NHẬT BẠN MUỐN SỬ DỤNG ========")
                    print("1.Giá phòng một đêm")
                    print("2.Số đêm thuê")
                    print("3.Phụ phí dịch vụ")
                    print("4.Giảm giá")
                    try:
                        choice = int(input("Nhập lựa chọn cập nhật bạn muốn: "))
                    except ValueError:
                        print("Lựa chọn nhập không đúng định dạng. Vui lòng nhập lại.")
                        continue
                    if choice == 1:
                        val = input("Nhập giá phòng mới: ")
                        if len(val) == 0:
                            print("Không được để trống.")
                            continue
                        i.room_price = int(val)
                        print("Cập nhật đặt phòng thành công")
                    elif choice == 2:
                        val = input("Cập nhập số đêm thuê: ")
                        if len(val) == 0:
                            print("Không được để trống.")
                            continue
                        i.nights = int(val)
                        print("Cập nhật số đêm thuê thành công")
                    elif choice == 3:
                        val = input("Cập nhập giá phụ phí dịch vụ mới: ")
                        if len(val) == 0:
                            print("Không được để trống.")
                            continue
                        i.service_fee = int(val)
                        print("Cập nhật phụ phí dịch vụ thành công")
                    elif choice == 4:
                        val = input("Cập nhập giá giảm giá mới: ")
                        if len(val) == 0:
                            print("Không được để trống.")
                            continue
                        i.discount = int(val)
                        print("Cập nhật giảm giá thành công")
                    break
            if not found:
                print("Không tìm thấy id bạn muốn tìm")
                break
                
    def delete_booking(self):
        while True:
            if len(self.bookings) == 0:
                print("Danh sách đang rỗng.")
                break
            find_id = input("Nhập mã đặt bạn muốn tìm để xóa (Enter để thoát): ").strip().upper()
            if not find_id:
                break
                
            found = False
            for i in self.bookings:
                if find_id == i.id:
                    self.bookings.remove(i)
                    print("Đã xóa đặt phòng thành công.")
                    found = True
                    break
            if not found:
                print("Không tìm thấy id bạn muốn tìm")
            break

    def search_booking(self):
        while True:
            if len(self.bookings) == 0:
                print("Danh sách đang rỗng.")
                break
            find_id = input("Nhập mã đặt bạn muốn tìm để tìm kiếm (Enter để thoát): ").strip().upper()
            if not find_id:
                break
                
            found = False
            for i in self.bookings:
                if find_id == i.id:
                    print(" Mã đặt phòng | Họ tên khách hàng | Số phòng | Giá phòng một đêm | Số đêm thuê | Phụ phí dịch vụ | Giảm giá | Tổng tiền thuê | Phân loại tiền thuê ")
                    total_rent = i.calculate_total_rent()
                    rent_type = i.classify_rent()
                    print(f"{i.id} | {i.customer_name} | {i.room_number} | {i.room_price} | {i.nights} | {i.service_fee} | {i.discount} | {total_rent} | {rent_type}")
                    found = True
                    break
            if not found:
                print("Không tìm thấy id bạn muốn tìm")
            break
    
def main_menu():
    Result = BookingManager()
    while True:
        print("\n================ MENU ================")
        print("1. Hiển thị danh sách đặt phòng")
        print("2. Thêm đặt phòng mới")
        print("3. Cập nhật đặt phòng")
        print("4. Xóa đặt phòng")
        print("5. Tìm kiếm đặt phòng")
        print("6. Thoát")
        print("=====================================")
        try:
            choice = int(input("Nhập lựa chọn của bạn: "))
        except ValueError:
            print("Nhập sai định dạng lựa chọn. Vui lòng nhập lại.")
            continue
        if choice == 1:
            Result.show_all()
        elif choice == 2:
            Result.add_booking()
        elif choice == 3:
            Result.update_booking()
        elif choice == 4:
            Result.delete_booking()
        elif choice == 5:
            Result.search_booking()
        elif choice == 6:
            print("Cảm ơn bạn đã sử dụng hệ thống quản lý đặt phòng khách sạn!")
            break
        else:
            print("Nhập sai chức năng. Vui lòng nhập lại (Từ 1-6)")
            continue

main_menu()