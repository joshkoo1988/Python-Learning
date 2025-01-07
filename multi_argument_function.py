def triple_attack(damage_one, damage_two, damage_three):
    total_damage = damage_one + damage_two + damage_three
    return total_damage

attack_one = 2
attack_two = 4
attack_three = 3
first_triple_attack_damage = triple_attack(attack_one, attack_two, attack_three)

print("attack one : " ,attack_one)
print("attack two : " ,attack_two)
print("attack three : " ,attack_three)
print("total damage = " ,first_triple_attack_damage )

print("=====================================")

attack_four = -1
attack_five = 10
attack_six = 5
second_triple_attack_damage = triple_attack(attack_four, attack_five, attack_six)

print("attack one : " ,attack_four)
print("attack two : " ,attack_five)
print("attack three : " ,attack_six)
print("total damage = " ,second_triple_attack_damage )
print("=====================================")
