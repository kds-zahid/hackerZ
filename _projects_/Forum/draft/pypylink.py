from urllib.parse import urlparse

# Provided link
link = "http://old.jrweike.com/forum.php?mod=viewthread&tid=42478&page=1&extra=#pid53592"

# Parse the URL
parsed_url = urlparse(link)

# Extract the main homepage address
home = parsed_url.scheme + "://" + parsed_url.netloc

# Print the main homepage address
print(home)
