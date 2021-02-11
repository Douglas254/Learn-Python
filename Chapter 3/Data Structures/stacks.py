# stscks uses a last in first out method - LiFO
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])

# operations in stack
browsing_session = []
browsing_session.append(1)  # add an item on top of the stack
browsing_session.pop()  # remove an item on top of the stack
if not browsing_session:  # check if the stack is empty or not
    browsing_session[-1]  # get an item on top of the stack
