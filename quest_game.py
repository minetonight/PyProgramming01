deistvie_ili_ne = 0
miasto = 0
level = 1
mqsto_kluch = 1

while True:

	print("                                                        LEVEL" +str(level))
	print("")
	print("")
	print("Ako vi se sluchi da ste v zaklucheni v uchilishte sled kato vsichki sa si tragnali no znaete che nqkade ima rezerven kluch za vratata.")
	print("")
	print("Vie trqbva da go namerite")
	print("")


	miasto = input("imate izbor kade da otidete. Izberete 2: ako iskate da otidete v bibliotekata i 1: ako iskate da otidete v salona po PE: ")
	deistvie_ili_ne = 0


	#proverka kade sme
	if miasto == 1:
		print("")
		print("Vie namirate edna topka")
		print("                #####           ")
		print("              #   #   #         ")
		print("            ###   #   ###       ")
		print("           #   #  #  #   #      ")
		print("           ###############      ")
		print("            ## #  #  # ##       ")
		print("              #   #   #         ")
		print("                #####           ")
		print("")
		deistvie_ili_ne = input("shte igraete li s neia ili ne: 1 - da, 2 - ne: ")
		if deistvie_ili_ne == 1:
			if mqsto_kluch == 3:
				print("Dokato igraesh s neia ia udriash v rab i tia se cepi na dve")
				print("")
				print("raztvariate ia i vajdate che v neia e kucha")
				print("                               #####         ")
				print("                              #     #        ")
				print(" #############################       #       ")
				print(" ######                       #     #        ")   
				print(" ####                          #####         ")
				level = level + 1
				mqsto_kluch = mqsto_kluch + 1
			else:
				print("")
				print("igraete si s neq i posle se vrashtate v parvonachalna pozicia")
		if deistvie_ili_ne == 2:
			if mqsto_kluch == 1:
				print("")
				print("Dokato izlizate bez da iskate ia podritvate tia se obrashta kam vas i vie vijdate che e cepnata")
				print("")
				print("raztvariate ia i vajdate che v neia e kucha")
				print("                               #####         ")
				print("                              #     #        ")
				print(" #############################       #       ")
				print(" ######                       #     #        ")   
				print(" ####                          #####         ")
				level = level + 1
				mqsto_kluch = mqsto_kluch + 1
			else:
				print("")
				print("Vrashtate se v nacaloto")
	if miasto == 2:
		print("")
		print("Vie namirate edna kniga")
		print("       ########################################                ")
		print("      #  #  #    #  #    #  #     #####   #     #               ")
		print("     #   # #     #  #    # ##     #       ##      #             ")
		print("     #   ##      ####    ## #     #       #_#     #             ")
		print("      #  #  #    #  #    #  #     #       #  #   #              ")
		print("       #########################################               ")
		print("")
		deistvie_ili_ne = input("shte ia prochetete li ili ne: 1 - da, 2 - ne: ")
		if deistvie_ili_ne == 1:
			print("")
			print("otvariate ia i vijdate che e:")
			print("           ##############################################")
			print("           #                     #                      #")
			print("           #                     #                      #")
			print("           #                     #                      #")
			print("           #                     #                      #")
			print("           #                     #                      #")
			print("           #                     #                      #")
			print("           #                     #                      #")
			print("           #                     #                      #")
			print("           #                     #                      #")
			print("           #                     #                      #")
			print("           #                     #                      #")
			print("           ##############################################")
			print("PRAZNA STRANICA???")
			if mqsto_kluch == 2:
				print("")
				print("No tam ima kluch")
				print("                               #####         ")
				print("                              #     #        ")
				print(" #############################       #       ")
				print(" ######                       #     #        ")   
				print(" ####                          #####         ")
				level = level + 1
				mqsto_kluch = mqsto_kluch + 1
			else:
				print("")
				print("Vrashtate se v nacaloto")
		if deistvie_ili_ne == 2:
			if mqsto_kluch == 4:
				print("")
				print("Tochno kogato posteaviate knigata ot tam ot kadeto ste q vzeli se spavate i vijdate klucha pod shkafa")
				print("                               #####         ")
				print("                              #     #        ")
				print(" #############################       #       ")
				print(" ######                       #     #        ")   
				print(" ####                          #####         ")
				level = level + 1
				mqsto_kluch = mqsto_kluch + 1
				print("VIE PREVARTIAHTE IGRATA!!!")
			else:
				print("")
				print("Vrashtate se v nacaloto")
	if level == 5:
		break
