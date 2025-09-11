import hinhhoc_1

print('HINH CHU NHAT:')
w = int(input('Nhap chieu rong:'))
l = int(input('Nhap chieu dai:'))
print(f"Dien tich: {hinhhoc_1.rectangle_area(w, l)}, "
      f"chu vi: {hinhhoc_1.rectangle_perimeter(w, l)}")

print('HINH TAM GIAC:')
a = int(input('Nhap do dai canh a:'))
b = int(input('Nhap do dai canh b:'))
c = int(input('Nhap do dai canh c:'))
print(f"Dien tich: {hinhhoc_1.triangle_area(a, b, c)}, "
      f"chu vi: {hinhhoc_1.triangle_perimeter(a, b, c)}")

print('HINH TRON:')
r = int(input('Nhap ban kinh:'))
print(f"Dien tich: {hinhhoc_1.circle_area(r)}, "
      f"chu vi: {hinhhoc_1.circle_perimeter(r)}")
