# Automated Loan Approval System

credit_score = int(input());
income = int(input());
emi = int(input());
employment = input();



# Credit Score Check 

def loan_approval_System(credit_score,income,emi,employment):

    if credit_score < 600:
        print(" Status : Rejected");
    elif credit_score >= 600 and credit_score <= 749 :
        print(" Status : Rejected");
    else:
        if income < 25000:
            print(" Status : Rejected");
        else:
            if emi < (income%2) :
                print(" Status : Rejected");
            else :
                if employment == "Salaried" or employment =="Self-Employed":
                    print("Status : Approved");
                else:
                    print(" Status : Rejected");

    if credit_score >= 800:
        print("Interest Rate:7%");
    elif credit_score > 750 and credit_score < 799:
        print("Interest Rate:8%");

loan_approval_System(credit_score,income,emi,employment);


