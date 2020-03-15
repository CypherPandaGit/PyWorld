import copy

# menu = []
# menu.append(["egg", "spam", "bacon"])
# menu.append(["egg", "sausage", "bacon"])
# menu.append(["egg", "spam"])
# menu.append(["egg", "bacon", "spam"])
# menu.append(["egg", "bacon", "sausage", "spam"])
# menu.append(["spam", "bacon", "sausage", "spam"])
# menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
# menu.append(["spam", "egg", "sausage", "spam"])
#
# print(menu)
#
# for meal in menu:
#     if not "spam" in meal:
#         print(meal)
#         for item in meal:
#             print(item)

spam = ['A', 'B', 'C', 'D'] # list
# spam = cheese # this is just reference to spam list
cheese = copy.deepcopy(spam) # copy spam list to cheese

print(cheese)
print(spam)
