import requests
import webbrowser

def get_data(content, name):
    response = requests.get(f"https://api.themoviedb.org/3/search/{content}?api_key=87d5585a5497b373679e8bdc7d6f0d22&query={name}\"")
    request = response.json()
    return request.get("results")

def movie(content, name):
    result_list = get_data(content, name)

    counter = 0
    id_list = []

    for i in result_list:
        counter = counter + 1

    for i in range(counter):
        result_first = result_list[i]
        print(f"[{str(i)}]\t{str(result_first.get('original_title'))}")
        # print(f"[Desc]\t{str(result_first.get('overview'))}\n") #+ str(result_first.get('id')))
        id_list.append(str(result_first.get('id')))
    
    play = int(input("\nSelect a movie [type number]: "))
    print(id_list[play])
    webbrowser.open(f"https://vidsrc.me/embed/{str(id_list[play])}")

def show(content, name, season, episode):
    result_list = get_data(content, name)

    counter = 0
    id_list = []

    for i in result_list:
        counter = counter + 1

    for i in range(counter):
        result_first = result_list[i]
        print(f"[{str(i)}]\t{str(result_first.get('name'))}")
        # print(f"[Desc]\t{str(result_first.get('overview'))}\n") #+ str(result_first.get('id')))
        id_list.append(str(result_first.get('id')))

    play = int(input("\nSelect a Show [type number]: "))
    webbrowser.open(f"https://vidsrc.me/embed/{str(id_list[play])}/{season}-{episode}")


# movie("movie", "Avatar")
show("tv", "breaking+bad", 2, 3)