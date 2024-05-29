import time

res = "{:,.4f}".format(time.time())

scientific = "{:.2e}".format(time.time())

date = time.strftime("%b %d %Y")

print("Seconds since January 1, 1970:", res, "or", scientific, "in scientific notation")
print(date)