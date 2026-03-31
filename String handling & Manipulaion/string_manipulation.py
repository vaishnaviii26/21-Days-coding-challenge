driver_name = "vaishnavi V";

print(driver_name.lower());
print(driver_name.upper());
print(driver_name.capitalize());

driver_name = " vaishnavi v";
mobile = "6382996597";
masked = mobile[:2] + "******" + mobile[-2:];
print(masked);


# Format String 

song = "shape OF you";
artist = "VAISHNAVI v";

formatted=f"{song.title()} - {artist.title()}";
print(formatted);

location = "Chennai central";
fixed_location = location.replace("Chennai central","Tambaram");
print(fixed_location);

message = "Your uber booking id is : UB12345.Please keep it safe";
booking_id = message.split(":")[1].split(".")[0].strip()
print(booking_id);

promo_msg = "use zomato100 to get 100 off on your first order";

if "zomato100" in promo_msg:
    print("offer applied");


feedback = "the driver was polite and the ride was smooth"
print("position is:",feedback.find("polite"))
