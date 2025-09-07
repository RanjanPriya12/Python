#String Slicing

name = "Priya Ranjan";
print(name[2:7]);  #iya R
print(name[:5]); #Priya
print(name[0:]); #PRiya Ranjan
print(name[-5:-1]); #anja
print(len(name));

message= "  Hello, Good morning";
if('llo' in message):
    print('llo is present in '+message);

if('Priya' not in message):
    print('Priya is not present in '+message);

print(message.strip());
print(message.replace('morning','evening'));
print(message.split(","));


price = 59
txt = f"The price is {price:.2f} dollars"
print(txt);
print(txt.endswith('dollars'));
print(txt.count('i'));