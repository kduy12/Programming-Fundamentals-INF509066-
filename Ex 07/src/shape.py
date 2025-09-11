import hinhhoc

print('HINH CHU NHAT:')
w = int(input('Nhap chieu rong:'))
l = int(input('Nhap chieu dai:'))
print(f"Dien tich: {hinhhoc.hinhchunhat.area(w, l)}, "
      f"chu vi: {hinhhoc.hinhchunhat.perimeter(w, l)}")

print('HINH TAM GIAC:')
a = int(input('Nhap do dai canh a:'))
b = int(input('Nhap do dai canh b:'))
c = int(input('Nhap do dai canh c:'))
print(f"Dien tich: {hinhhoc.hinhtamgiac.area(a, b, c)}, "
      f"chu vi: {hinhhoc.hinhtamgiac.perimeter(a, b, c)}")

print('HINH TRON:')
r = int(input('Nhap ban kinh:'))
print(f"Dien tich: {hinhhoc.hinhtron.area(r)}, "
      f"chu vi: {hinhhoc.hinhtron.circumference(r)}")


