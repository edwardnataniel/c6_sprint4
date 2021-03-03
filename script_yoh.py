from bs4 import BeautifulSoup
import json

def generate_html():
	return"""
		<html>
			<head></head>
			<body>
				<a href="/a.html">A</a>
				<a href="/b.html">B</a>
				<a href="/c.html">C</a>
				<a href="/d.html">D</a>	

				<script>
					var hello = "yoh";
					alert(hello);
				</script>

				
			</body>
		</html>
	"""

def main():
	html_doc = generate_html()
	soup = BeautifulSoup(html_doc, 'html.parser')
	#div_elements = soup.find_all('script')
	
	script2 = soup.find('script').string
	print(script2.strip().split(";")[0][-4:-1])
	
	
if __name__ == "__main__":
	main()