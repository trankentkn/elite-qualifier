from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
}
URL = 'https://www.reddit.com/r/aww/top/?t=day'
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

post_dictionary = {}
job_list = []
cute_list = ['dog','cute','cat','adorable', 'sweet', 'beautiful', 'baby', 'precious', 'love', 'happy', 'happiest', 'amazing', 'warm', 'boy', 'boi', 'special', 'good', 'innocent', 'fluffy', 'tiny',  'bean', 'toe', 'tippy', 'tap', 'play', 'favorite', 'animal', 'emotional', 'support', 'grand', 'child', 'mama', 'papa', 'pet', 'melt', 'earn', 'treat', 'feed', 'mom', 'mother', 'dad', 'father', 'young', 'pup', 'kit', 'floof', 'little', 'smol', 'small', 'nap', 'sleep', 'hug', 'excite', 'joy', 'wiggle', 'old', 'aww']

def word_counter(block, word_list):
  count = 0
  newblock = block.lower()
  for word in word_list:
    count += newblock.count(word.lower())
  return count

# Original bubble sort from https://www.geeksforgeeks.org/bubble-sort/
def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if post_dictionary[arr[j]]['cute_score'] < post_dictionary[arr[j + 1]]['cute_score'] :
				arr[j+1], arr[j] = arr[j], arr[j+1]

posts = soup.find_all("div" , class_= "_1poyrkZ7g36PawDueRza-J")
x = 1
for post in posts:
  post_url = post.a["href"]
  if 'https://www.reddit' in post_url:
    post_dictionary[x] = {}

    title = post.find('h3', class_ = '_eYtD2XCVieq6emjKBH3m').text
    upvotes = post.find('div', class_ = '_1rZYMD_4xY3gRcSS3p8ODO').text

    post_dictionary[x]['title'] = title
    post_dictionary[x]['URL'] = post_url
    post_dictionary[x]['upvotes'] = upvotes

    comment_text = ''
    comment_URL = f'{post_url}'
    comment_response = requests.get(comment_URL, headers=headers)
    comment_soup = BeautifulSoup(comment_response.content, 'html.parser')

    comment_post = comment_soup.find_all('div' , class_ = '_3tw__eCCe7j-epNCKGXUKk')

    for post in comment_post:
      comment_text += str(post.find('p', class_ = '_1qeIAgB0cPwnLhDF9XSiJM'))
    post_dictionary[x]['cute_score'] = word_counter(comment_text, cute_list)

    x+=1


for x in range(len(post_dictionary)):
  job_list.append(x + 1)

bubbleSort(job_list)

print("------------------------")
print("Top 5 Cutest Posts Today")
for x in range(5):
  print("------------------------")
  print("")
  print(f"Rank {str(x + 1)} (Cute Score: {str(post_dictionary[job_list[x]]['cute_score'])})")
  print(f"{post_dictionary[job_list[x]]['upvotes']} Upvotes")
  print("")
  print(f"Title: {post_dictionary[job_list[x]]['title']}")
  print(f"URL: {post_dictionary[job_list[x]]['URL']}")