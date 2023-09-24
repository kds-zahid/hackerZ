import pyperclip



pasteurls=pyperclip.paste()
url_array=pasteurls.splitlines()

# Print the data
print("Data from clipboard:")
print(url_array)
input()