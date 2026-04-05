meme_dict = {'CRINGE': 'Raro, vergonzoso',
'SHEESH':'ligera desaprobación',
'CREEPY':'Raro, espeluznante',
'AGGRO':'ponerse agresivo',
'SUS':'Sospechoso',
'SIMP':'Persona que hace cualquier cosa por alguien que le gusta',
'LOL':'Respuesta a algo gracioso',
'ROFL':'Respuesta a algo muy gracioso',
'LMAO':'Respuesta a algo extremadamente gracioso',
'BRUH':'Respuesta a algo que no tiene sentido',
'GG':'Good game',
'NPC':'No playable character',
'BRB':'Be right back',
'IDK':'I don´t know',
'ZZZ':'Dormido',
'FPS':'Fotogramaa por segundo o First person shooter',
'XP':'Experience points',
'NOOB':'Novato',
'HITBOX':'Caja de daño',
'BUFF':'Mejora',
'DEBUFF':'Empeoramiento',
'GLITCH':'Falla en el juego',
'RAGEQUIT':'Abandonar el juego por frustración',
'PVP':'Player versus player',
'PVE':'Player versus environment',
'AFK':'Away from keyboard'
}

print (meme_dict.keys())
while True:
  palabra = input ('que palabra quieres saber')
  if palabra in meme_dict.keys():
    print(meme_dict[palabra])
  else:
    print('Esa palabra no la tenemos') 