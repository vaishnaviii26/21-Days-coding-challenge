#: API Rate Limiter (Fixed Window)

request_count = int(input());

def rate_limiter(request_count):
    
    if request_count <= 5:
        print("Allowed!");
    elif request_count > 5:
        print("Blocked (Rate Limit Exceeded)");
    else:
        print("Invalid Input");

rate_limiter(request_count);
    
