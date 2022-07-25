import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print("      ___________________  ")
print("  -->|   Data Analysis   |<---")
print("     |     on Anime      |    ")
print("     |___________________|     ")
dataset = pd.read_csv("anime.csv")

print("WELCOME TO Anime Data Analysis\n")  
  
while True:  
    print("MENU")  
    print("1. Graph on type of anime")  
    print("2. Episodes count of different anime")  
    print("3. Rating  of different anime")  
    print("4. Active members")  
    print("5. Top 5 genre")  
    print("6. Exit")
    users_choice = int(input("\nEnter your Choice: "))  
  
    if users_choice == 1:  
          dataset['type'].value_counts().plot(kind='bar' , figsize=(12,12))
          plt.show()
        
  
    elif users_choice == 2:  
        dataset['episodes'].value_counts().plot(kind='hist' , figsize=(12,12))
        plt.show()

    elif users_choice == 3:  
        dataset['rating'].value_counts().plot(kind='scatter' , figsize=(12,12))
        plt.show()
  
    elif users_choice == 4:  
        dataset['members'].value_counts().plot(kind='hist' , figsize=(12,12))
        plt.show()

    elif users_choice == 5:  
        genreList=[]
        genre_dict = {}
        for key, value in genre_dict.items():
            temp = [key,value]
            genreList.append(temp)

        genre_df=pd.DataFrame(genreList, columns = ["rating", "genre"]) 
        genre_df.sort_values("rating").tail(5)
        plt.show()
    
    elif users_choice == 6:
        break
        
      
    else:  
        print( "Please enter a valid Input from the list")  