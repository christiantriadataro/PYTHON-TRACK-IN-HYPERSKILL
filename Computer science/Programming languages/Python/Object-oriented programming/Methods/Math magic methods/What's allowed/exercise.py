# Below you can see the class Account. It has 2 instance
# attributes, account_id and amount, as well as some methods.

class Account:
    def __init__(self, account_id, amount):
        self.account_id = account_id
        self.amount = amount

    def __iadd__(self, other):
        self.amount += other.amount
        return self
    def __eq__(self, other):
        return ((self.account_id == other.account_id) and (self.amount == other.amount))


account1 = Account("acc0000927", 999.99)
account2 = Account("acc0083972", 1564.26)

print(account1 == account2)
# print(account1 > account2)
# account2 += account1
# print(account1 * account2)
account3 = account1 + account2
print(account3)