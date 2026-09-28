infile = open("raw_logs.txt", "r")
master = open("decrypted_master.txt", "w")
alerts = open("security_alerts.txt", "w")
for line in infile:
    decrypted = ""
    for ch in line:
        if "A" <= ch <= "Z":
            decrypted += chr((ord(ch) - ord("A") - 3) % 26 + ord("A"))
        elif "a" <= ch <= "z":
            decrypted += chr((ord(ch) - ord("a") - 3) % 26 + ord("a"))
        else:
            decrypted += ch
    decrypted = decrypted.strip()
    if decrypted != "":
        master.write(decrypted + "\n")
        if "BREACH" in decrypted.upper():
            alerts.write(decrypted + "\n")
infile.close()
master.close()
alerts.close()
print("Decryption complete. Check decrypted_master.txt and security_alerts.txt.")
