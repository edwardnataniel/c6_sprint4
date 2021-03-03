from bs4 import BeautifulSoup
from IPython import embed

def generate_html():
	return"""
		<html>
		<head>
			<title>Head's title</title>
		</head>
		
		<body>
			<p class="title"><b>Body's title</b></p>
			<p class="story">line begins
				<a href="http://example.com/element1" class="element" id="link1">1</a>
				<a href="http://example.com/element2" class="element" id="link2">2</a>
				<a href="http://example.com/avatar1" class="avatar" id="link3">3</a>
			</p>
			<p> line ends</p>
		</body>
		</html>
		"""

def main():
	html_doc = generate_html()
	soup = BeautifulSoup(html_doc, 'html.parser')
#	print(soup.get_text())
	
	all_a = soup.find_all("a", href=True)

#	div_elements = soup.find_all('p')
#	print(all_a)

	for elem in all_a:
		print(elem.get_text())

	
if __name__ == "__main__":
	main()