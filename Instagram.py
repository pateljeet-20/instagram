from bs4 import BeautifulSoup

def get_instagram_links(filename):
    with open(filename, 'r') as f:
        contents = f.read()

    soup = BeautifulSoup(contents, 'html.parser')

    links = set()
    for link in soup.find_all('a'):
        url = link.get('href')
        if 'instagram' in url:
            links.add(url)

    return links

def compare_links(file1, file2):
    links1 = get_instagram_links(file1)
    links2 = get_instagram_links(file2)

    only_in_file1 = links1 - links2
    only_in_file2 = links2 - links1

    return only_in_file1, only_in_file2

file1 = input("Enter the file path of following: ")
file2 = input("Enter the file path of followers: ")

only_in_file1, only_in_file2 = compare_links(file1, file2)

print(f"Follower who don't follow you back {file1}:")
for link in only_in_file1:
    print(link)

print(f"\n Followers you don't follow {file2}:")
for link in only_in_file2:
    print(link)
