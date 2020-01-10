# def dollarize(money_int):
# 	if "." in str(money_int):
# 		money = str(money_int).split(".")
# 		if len(money[1]) > 2:
# 			for i in range(len(money[1])):
# 				if i == 2:
# 					money[1] = money[1][:i]
# 					break
# 				else:
# 					continue
# 		else:
# 			pass


# 		count = 0
# 		new_list = []
# 		new_string = ''
# 		dollars = money[0]
# 		for i in dollars:
# 			new_list.append(i)

# 		for i in range(len(dollars)):
# 			if count % 3 == 0 and count != 0 and new_list[len(dollars) - i - 1] != '-':
# 				new_list.insert(len(dollars) - i, ',')
# 				count += 1
# 			else:
# 				count += 1

# 		for i in new_list:
# 			new_string += i

# 		print(f"${new_string}.{money[1]}")

# 	else:
# 		money = str(money_int)
# 		count = 0
# 		new_string = ''
# 		new_list = []

# 		for i in money:
# 			new_list.append(i)

# 		for i in range(len(money)):
# 			if count % 3 == 0 and count != 0 and new_list[len(money) - i - 1] != '-':
# 				new_list.insert(len(money) - i, ',')
# 				count += 1
# 			else:
# 				count += 1

# 		for i in new_list:
# 			new_string += i

# 		print(f"${new_string}")





import moneyfmt

cash = moneyfmt.MoneyFmt(123452385746238456923847566329457.78901)
print(cash)
cash.update(100000.4567)
print(cash)
cash.update(-0.3)
print(cash)
repr(cash)

