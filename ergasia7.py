import json
# reading the data from the file
file_of_dictionaries = open("dictionaries.txt","r")

first_line = file_of_dictionaries.readline()

# reconstructing the data as a dictionary
first_Dict = json.loads(first_line)

file_of_dictionaries.close()


keys = []
for key in first_Dict.keys():
    keys.append(key)

print(keys)
key = input("Choose one of the available keys listed above: ")

Flag = False
while not Flag:
    for i in range(len(keys)):
        if keys[i] == key:
            Flag = True
            break
    else:
        print("\nThe key that you entered is not listed, try again: ")
        print(keys)
        key = input("Choose one of the available keys listed above: ")



# reading the data from the file and reconstructing the data as a dictionary
with open('dictionaries.txt', 'r') as file_of_dictionaries:
    Dicts = [json.loads(line) for line in file_of_dictionaries]

file_of_dictionaries.close()


given_key_data = []
for i in Dicts:
    given_key_data.append(i[key])


if len(set(given_key_data)) != len(given_key_data): #if list's elements are not unique, find which appears more frequently
    def most_common(given_key_data):
        return max(set(given_key_data), key=given_key_data.count)
    print("\n" + str(most_common(given_key_data)) + " is the most frequent element in the " + str(key) + "'s item list")

print("\n" + str(max(given_key_data)) + " is the max value of key: " + key)
print("\n" + str(min(given_key_data)) + " is the min value of key: " + key)
