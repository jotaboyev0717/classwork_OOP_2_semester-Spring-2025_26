import counter, auth, shop

auth.login("Alisher")
auth.login("Sevara")
shop.buy("Alisher", "book")
shop.buy("Sevara", "phone")
shop.buy("Alisher", "Pen")
print(f"Total visits: {counter.get_count()}")