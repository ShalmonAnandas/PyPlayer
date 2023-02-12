import requests
import webbrowser

media_selector = int(input("Do you wanna watch a Movie or a Show?\nMovie [1]\nShow [2]\nEnter a number: "))
if media_selector == 1:
    media_name = input("Enter the name of the Movie: ")
elif media_selector == 2:
    media_name = input("Enter the name of the Show: ")   
media_query = media_name.replace(" ","+")
media_type_dict = {1 : "movie", 2 : "tv"}

response = requests.get(f"https://api.themoviedb.org/3/search/{media_type_dict.get(media_selector)}?api_key=87d5585a5497b373679e8bdc7d6f0d22&query={media_query}\"")
print(media_type_dict.get(media_selector))
request = response.json()
result_list = request.get("results") 
counter = 0
id_list = []

for i in result_list:
    counter = counter + 1

if media_selector == 1:
    for i in range(counter):
        result_first = result_list[i]
        print(f"[{str(i)}]\t{str(result_first.get('original_title'))}")
        # print(f"[Desc]\t{str(result_first.get('overview'))}\n") #+ str(result_first.get('id')))
        id_list.append(str(result_first.get('id')))
elif media_selector == 2:
    for i in range(counter):
        result_first = result_list[i]
        print(f"[{str(i)}]\t{str(result_first.get('name'))}")
        # print(f"[Desc]\t{str(result_first.get('overview'))}\n") #+ str(result_first.get('id')))
        id_list.append(str(result_first.get('id')))

if media_selector == 1:
    play = int(input("\nSelect a movie [type number]: "))
    print(id_list[play])
    webbrowser.open(f"https://vidsrc.me/embed/{str(id_list[play])}")
elif media_selector == 2:
    play = int(input("\nSelect a Show [type number]: "))
    season_number = input("Season Number: ")
    episode_number = input("Episode Number: ")
    webbrowser.open(f"https://vidsrc.me/embed/{str(id_list[play])}/{season_number}-{episode_number}")