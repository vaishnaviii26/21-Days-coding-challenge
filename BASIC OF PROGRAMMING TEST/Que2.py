# Chat Context Window Optimizer

total_messages = int(input());

if total_messages <= 100:
    compressed = 0;
    print(f"Status : Normal, Active : {total_messages}, Compressed:{compressed}");
else :
    compressed = total_messages - 100;
    total_active = 100;
    print(f"Status : Optimized, Active : {total_active}, Compressed:{compressed}");
