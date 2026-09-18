def main():
    numbers = [3, 5, 17, 4, 7, 6]
    result1 = max(numbers)
    result2 = min(numbers)
    result3 = sum(numbers)
    print(f"Number list: {numbers}")
    print("Max: ", result1)
    print("Min: ", result2)
    print("Sum: ", result3)
    print()
    # append() and insert() method
    fruits = ["grapes", "oranges", "apples"]
    fruits.append("bananas") #this adds the new value in the list at the end
    print(fruits)
    fruits.insert(2, "lemons") #the number sets the value in the order of the list
    print(fruits)
    print()
    #sort() method
    numbers2 = [1,4,5,7,9,3]
    numbers2.sort() #the method puts the list of numers in numerical order
    print(numbers)
    items= ["Lettuce", "Tomato", "Bread", "Jam", "Mayo"]
    items.sort() #and a list of strings in alphabetical order
    print(items)
    print()
    #pop() and remove() methods
    lista = ["Rojo", "Amarillo", "Verde", "Naranja", "Azul"]
    print(lista)
    lista.remove("Verde") #This removes a string or value in a list (must be specified)
    print(lista)
    lista.pop(3) #Removes the value in the position of the functions number
    print(lista)
    print()
    #len() function
    objects = ["Pencil", "Computer", "Chair", "Paper", "Yoyo", "Nickel"]
    print(objects)
    print(len(objects)) #len(x) counts the amount of values in a list
    objects[len(objects)-1] = "Rock" #len() can also replace the last value in a list (or more idk)
    print(objects)
    print(len(objects))
if __name__ == "__main__":
    main()
