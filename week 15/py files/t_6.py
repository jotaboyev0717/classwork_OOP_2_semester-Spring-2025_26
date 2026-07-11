total = 0
def fetch_data(url):
    global total
    total += 1
    if total < 3:
        raise ConnectionError("timeout")
    elif total == 3:
        return f"data from {url}"
    
# @retry
# def retry():
#     max_attempts = 3
