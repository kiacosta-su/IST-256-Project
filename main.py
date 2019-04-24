from stockxsdk import Stockx

stockx = Stockx()

def get_product(email = "boringjohndoe@gmail.com", password = "Ihatethisclass.100"):
	# Looping until login is successfull
	while True:
		# Prompting user for their account
		# email = input("enter your stockx email: ")
		# password = input("enter your stockx password: ")

		# Authenticate the user
		logged_in = stockx.authenticate(email, password)

		# Check to see if credentials are currect, if not
		# they will have to enter their correct crendentails
		if logged_in:
			break
		else:
			print("WRONG, GOODBYE")

	# loop until user is done looking at the price of a sneaker
	while True:
		# Prompt user for a name of a sneaker
		product_id = input("enter the name of your sneaker or 'QUIT' to stop: ")

		# Check to see if user is done searching
		# if not, print out what sneaker price
		if product_id == "QUIT" or product_id == "":
			print("BYE BYE")
			break
		else:
			product = stockx.search(product_id)
			sneaker = product[0]
			print(sneaker['name'])