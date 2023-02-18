
people ={
    'rs':'rohan shnde',
    'ds':'dhiraj shinde',
    'bm':'bhumi more',
    'mb':'manish bhadane'
}
#people['rs'] = 'rohan vikas shinde'
#people.update({'mb':'manish sanjay bhadane'}) #it is use for updated new name 
#people['bm']
#print(people['mb']) #it is use for updated checking 

for person in people:
    print(person + " is the key of the value " + people[person])