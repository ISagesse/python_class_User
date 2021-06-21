from user import *

jack = User("Jack Bauer", "jackbauer@jb.com")
bond = User("James Bond", "superagent@jb.com")
israel = User("Israel Sagesse", "israelsagesse@gmail.com")

#Have the first user make 3 deposits and 1 withdrawal and then display their balance
jack.make_deposit(5000000)
jack.make_deposit(3000)
jack.make_deposit(15000000)
jack.make_withdrawal(4500000)
jack.display_user_balance()

#Have the second user make 2 deposits and 2 withdrawals and then display their balance
bond.make_deposit(300000)
bond.make_deposit(5000000)
bond.make_withdrawal(50000)
bond.make_withdrawal(450000)
bond.display_user_balance()

#Have the third user make 1 deposits and 3 withdrawals and then display their balance
israel.make_deposit(400)
israel.make_withdrawal(75)
israel.make_withdrawal(9.99)
israel.make_withdrawal(19.99)
israel.display_user_balance()