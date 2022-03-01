import requests
import webbrowser
import os

os.system("cls")
media_selector = int(input("Do you wanna watch a Movie or a Show?\nMovie [1]\nShow [2]\nEnter a number: "))
os.system("cls")
if media_selector == 1:
    media_name = input("Enter the name of the Movie: ")
elif media_selector == 2:
    media_name = input("Enter the name of the Show: ")   
media_query = media_name.replace(" ","+")
media_type_dict = {1 : "movie", 2 : "tv"}

response = requests.get("https://api.themoviedb.org/3/search/" + media_type_dict.get(media_selector) + "?api_key=87d5585a5497b373679e8bdc7d6f0d22&query=" + media_query + "\"")
#print("https://api.themoviedb.org/3/search/" + media_type_dict.get(media_selector) + "?api_key=87d5585a5497b373679e8bdc7d6f0d22&query=" + media_query + "\"")
request = response.json()
result_list = request.get("results") 
counter = 0
id_list = []

for i in result_list:
    counter = counter + 1

os.system("cls")

if media_selector == 1:
    for i in range(counter):
        print("-----------------------------------------------------------------------------------------------------------------------")
        result_first = result_list[i]
        print(str(result_first.get('original_title')) + " ["+str(i)+']\n' + str(result_first.get('overview'))+ "\n") #+ str(result_first.get('id')))
        id_list.append(str(result_first.get('id')))
        print("-----------------------------------------------------------------------------------------------------------------------")
elif media_selector == 2:
    for i in range(counter):
        print("-----------------------------------------------------------------------------------------------------------------------")
        result_first = result_list[i]
        print(str(result_first.get('name')) + " ["+str(i)+']\n' + str(result_first.get('overview')) + "\n") #+ str(result_first.get('id')))
        id_list.append(str(result_first.get('id')))
        print("-----------------------------------------------------------------------------------------------------------------------")

if media_selector == 1:
    play = int(input("\nSelect a movie [type number]: "))
    webbrowser.open("https://fsapi.xyz/tmdb-movie/" + str(id_list[play]))
elif media_selector == 2:
    play = int(input("\nSelect a Show [type number]: "))
    os.system("cls")
    season_number = input("Season Number: ")
    os.system("cls")
    episode_number = input("Episode Number: ")
    webbrowser.open("https://fsapi.xyz/tv-tmdb/" + str(id_list[play]) + "-" + season_number + "-" + episode_number)