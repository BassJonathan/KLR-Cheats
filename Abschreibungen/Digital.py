betrag_I = float(input("Betrag I in €: "))
restwert_L = float(input("Restwert L in €: "))
nutzungsdauer_T = int(input("Nutzungsdauer T in €: "))

fall_d = (2*(betrag_I - restwert_L)) / (nutzungsdauer_T * (nutzungsdauer_T+1))

print("Periode|Betrag Beginn|Abschreibungsbetrag|Betrag Ende")
for year in range(nutzungsdauer_T):
  betrag_davor = betrag_I
  abschreibungsbetrag_a = fall_d * (nutzungsdauer_T-year)
  betrag_I -= abschreibungsbetrag_a

  print("{:^7}|{:^13}|{:^19}|{:^11}".format((year+1), round(betrag_davor, 2), round(abschreibungsbetrag_a, 2), round(betrag_I, 2)))
