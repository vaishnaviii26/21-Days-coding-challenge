# Real-Time Fraud Detection System

amount = int(input());
location = input();
time = input("Enter Time as HH:MM format");
failed_attempts = int(input());



def fraud_detection_logic(amount,location,time,failed_attempts):
    count_risk = 0;

    if amount > 50000:
        count_risk += 1;
    
    if time < "00:00" and time < "05:00" :
        count_risk += 1;

    if location == "new":
        count_risk += 1;

    if failed_attempts >= 3:
        print("The Output is LOCK");

    if count_risk >= 3:
        print(F"Since {count_risk} risk factors are present, the output is HIGH.")

    elif count_risk < 3:
        print("The Output is LOW")    


fraud_detection_logic(amount,location,time,failed_attempts);