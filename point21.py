# Игра 21 очко
import random

class point21():
	print('Игра 21 очко!')

	def card_issuance(self, points):

		num = ( 2, 3, 4, 5, 6, 7, 8, 9, 10 )

		rnd = random.choice(num)
		points = 0
		
		if rnd == num[-1]:
			if points > 10:
				points += 1
			else:
				points += 10

		elif rnd != num[-1]:
			points += rnd

		return points

	# Подсчёт очков игрока
	def player(self):
		points = 0
		z = 0

		while z != 2:
			z += 1
			points += self.card_issuance(points)

		print("Ваше начальное кол-во очков:", points)

		print('Желаете продолжить?')
		nxt = str( input("yes/no? ") )
		print(" ")

		if nxt == 'yes':
			answer = True
			z = 0

			while z != 3 and answer == True:
				z += 1
				points += self.card_issuance(points)
				print(points)

				if points > 21:
					print("Очков больше чем 21, увы(")
					print(" ")
					break

				print('Дальше?')
				nxt = str( input("yes/no? " ) )

				if nxt == 'yes':
					answer = True
				elif nxt == 'no':
					answer = False
				print(" ")
		else:
			answer = False

		print("Количество очков игрока:", points)
		print(" ")

		return points

	# Подсчёт очков дилера		
	def dealer(self):		
		points = 0
		z = 0

		while z != 2:
			z += 1
			points+= self.card_issuance(points)

		z = 0
		while z != 3:
			z += 1

			if points <= 15:
				points += self.card_issuance(points)

		print("Количество очков дилера:", points)
		print(" ")

		return points

	# Сравнение очков и кто победил
	def game(self):

		player_points = self.player()
		dealer_points = self.dealer()
		
		if player_points > 21 and dealer_points > 21:
			print("Ничья!")

		if player_points > 21 and dealer_points <= 21:
			print("Победил Дилер!")

		if player_points <= 21 and dealer_points > 21:
			print("Победил Игрок!")

		if player_points <= 21 and dealer_points <= 21:
			if player_points > dealer_points:
				print("Победил Игрок!")
			elif player_points < dealer_points:
				print("Победил Дилер!")
			elif player_points == dealer_points:
				print("Ничья!")

		print("-------------------------------------------------------")
		print(" ")

		contin = input("Играть ещё yes/no? ")

		if contin == "yes":
			point21().game()

if __name__ == '__main__':
	point21().game()