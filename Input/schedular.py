
import sys; 


full_name = sys.argv[1];
last_name = sys.arg[2];

email = full_name.lower().replace(" " , ","python ) + last_name +"@company.com";

print('\n---- your profile ----');
print("Full Name:",full_name);
print('Generated Email:',email);