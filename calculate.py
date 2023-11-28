# SLIDE 26
# Question one.

name = " JOHn ."
name = name.replace(".","").lower().strip("")
print(name)


# Question 2
sentence_one = "The Dog Breed is German Shepherd"
print(sentence_one[8:24])
sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_two[16:30])


first_name="  Joh.n"
last_name="   Do,e"
first_name = first_name.strip().replace(".","")
last_name = last_name.strip().replace(",","")
full_name = first_name + " " + last_name
print (full_name)


sent = "The lazy dog; ran so fast; it hit the wall."
sent1 = sent.split((";"))
print(len(sent1))


r = ["E","W","C"]
r2 = ''.join(filter(str.isalpha, r))
print(r2)

num = 23.7
print(int(num))