import robin_stocks as robinhood

username = input("Enter User Name:\n")
password = input("Enter Password:\n")

login = robinhood.login(username, password)