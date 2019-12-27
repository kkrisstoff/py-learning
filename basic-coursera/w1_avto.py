# авропробег
km_day = int(input())
total_km = int(input())

d_kms = total_km // km_day
ost = total_km % km_day

ost_d = (ost + km_day - 1) // km_day

print(d_kms + ost_d)
