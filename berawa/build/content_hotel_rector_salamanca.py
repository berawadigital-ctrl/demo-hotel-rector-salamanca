# Contenido de la demo Hotel Rector (Salamanca) (es/en/fr/de). Hechos de hotelrector.com leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächlichen Zimmer.'}
H={'es':['Dobles e individual deluxe','Suites y familiar'],'en':['Doubles and deluxe single','Suites and family room'],'fr':['Doubles et individuelle deluxe','Suites et chambre familiale'],'de':['Doppelzimmer und Einzelzimmer Deluxe','Suiten und Familienzimmer']}
RD={
'es':['Doble y doble superior con muebles de caoba y baño de mármol, e individual deluxe con cama de 160 cm. Aire acondicionado, Smart TV, WiFi gratuito, cafetera y hervidor, albornoz y zapatillas.','Junior Suite Interior con dos camas dobles y salón, Suite Deluxe con salón interior, y familiar: dos dobles completas con dos baños unidas por un pasillo privado (hasta 5 huéspedes).'],
'en':['Double and superior double with mahogany furniture and marble bathroom, and a deluxe single with a 160 cm bed. Air conditioning, Smart TV, free WiFi, coffee maker and kettle, bathrobe and slippers.','Interior Junior Suite with two double beds and a lounge, Deluxe Suite with an inner sitting area, and the family room: two full doubles with two bathrooms joined by a private corridor (up to 5 guests).'],
'fr':['Double et double supérieure aux meubles en acajou et salle de bains en marbre, et individuelle deluxe avec lit de 160 cm. Climatisation, Smart TV, WiFi gratuit, cafetière et bouilloire, peignoir et chaussons.','Junior Suite intérieure avec deux lits doubles et salon, Suite Deluxe avec coin salon, et chambre familiale : deux doubles complètes avec deux salles de bains reliées par un couloir privé (jusqu\'à 5 personnes).'],
'de':['Doppelzimmer und Superior-Doppelzimmer mit Mahagonimöbeln und Marmorbad sowie Einzelzimmer Deluxe mit 160-cm-Bett. Klimaanlage, Smart-TV, kostenloses WLAN, Kaffeemaschine und Wasserkocher, Bademantel und Hausschuhe.','Junior Suite Interior mit zwei Doppelbetten und Wohnbereich, Suite Deluxe mit Sitzbereich und Familienzimmer: zwei vollständige Doppelzimmer mit zwei Bädern, verbunden durch einen privaten Flur (bis zu 5 Gäste).']}
ART={
'hero':('columns',9701,['#efe8dc','#f7f2ea','#6b3a24','#472616','#28150c']),
'intro':('arches',9702,['#f0e6d4','#e4b07a','#6b3a24','#472616','#28150c']),
'r1':('skyline',9711,['#472616','#e6a766','#f4d5a3','#2f4f5e','#25414e','#172b34']),
'r2':('hills',9712,['#ebeee6','#f1e6cf','#e3b46f','#a7b394','#7a8c6c','#52644a']),
'g1':('columns',9721,['#6b3a24','#ecbe86','#f6deb6','#8a5036','#6b3a24','#472616']),
'g2':('arches',9722,['#edeae2','#f7f4ee','#2f4f5e','#472616','#28150c']),
'g3':('waves',9723,['#ecdfca','#dcab76','#9e5a2e','#472616','#28150c']),
'g4':('skyline',9724,['#472616','#e0a064','#f2cf9c','#2c4b59','#223d49','#152730'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Rector · Hotel boutique en el centro histórico de Salamanca',see_rooms='Ver las habitaciones',hero_k='Salamanca · Centro histórico',hero_t='Hotel histórico en el centro de Salamanca',hero_s='Un hotel boutique en una antigua casa de 1930, cerca de la Casa Lis, la Catedral y el Puente Romano.',
 intro_t='Pensado para el descanso',intro_p1='14 habitaciones amplias. La cafetería y los salones son de uso exclusivo para huéspedes alojados, y se cuida la intimidad de cada estancia.',
 intro_p2='Desayuno bufet en el comedor y carta de room service. Garaje privado con acceso directo al lobby y un pequeño gimnasio perfectamente equipado.',
 stats=['Casa de 1930','14 habitaciones','Garaje privado','Gimnasio'],nav_rooms='Habitaciones',rooms_t='Nuestras habitaciones',rooms_s='Seis clases de habitación, de la individual deluxe a la familiar.',
 svcs=['Desayuno bufet','Room service','Garaje privado con acceso al lobby','Puntos de carga para vehículos eléctricos','Gimnasio','Cafetería y salones solo para huéspedes'],
 around_s='A pocos minutos andando: Plaza Mayor, Catedral, Universidad, Convento de San Esteban, Puente Romano y Jardines de Calixto y Melibea.',
 loc_p='P.º del Rector Esperabé, 10 · 37008 Salamanca, en el centro histórico.',
 chips=['¿Qué habitaciones tenéis?','¿Tenéis garaje?','¿Hay desayuno?','¿Dónde está el hotel?']),
'en':dict(title='Hotel Rector · Boutique hotel in the historic centre of Salamanca',see_rooms='See the rooms',hero_k='Salamanca · Historic centre',hero_t='A historic hotel in the centre of Salamanca',hero_s='A boutique hotel in a former 1930 house, near the Casa Lis, the Cathedral and the Roman Bridge.',
 intro_t='Designed for rest',intro_p1='14 spacious rooms. The cafeteria and lounges are for resident guests only, and the privacy of every stay is respected.',
 intro_p2='Buffet breakfast in the dining room and a room service menu. Private garage with direct access to the lobby and a small, fully equipped gym.',
 stats=['House from 1930','14 rooms','Private garage','Gym'],nav_rooms='Rooms',rooms_t='Our rooms',rooms_s='Six room types, from the deluxe single to the family room.',
 svcs=['Buffet breakfast','Room service','Private garage with lobby access','Electric vehicle charging points','Gym','Cafeteria and lounges for guests only'],
 around_s='A few minutes on foot: Plaza Mayor, Cathedral, University, San Esteban Convent, Roman Bridge and Calixto y Melibea Gardens.',
 loc_p='P.º del Rector Esperabé, 10 · 37008 Salamanca, in the historic centre.',
 chips=['Which rooms do you have?','Do you have a garage?','Is there breakfast?','Where is the hotel?']),
'fr':dict(title='Hotel Rector · Hôtel boutique dans le centre historique de Salamanque',see_rooms='Voir les chambres',hero_k='Salamanque · Centre historique',hero_t='Un hôtel historique au centre de Salamanque',hero_s='Un hôtel boutique dans une ancienne maison de 1930, près de la Casa Lis, de la cathédrale et du pont romain.',
 intro_t='Pensé pour le repos',intro_p1='14 chambres spacieuses. La cafétéria et les salons sont réservés aux clients de l\'hôtel, et l\'intimité de chaque séjour est préservée.',
 intro_p2='Petit-déjeuner buffet dans la salle à manger et carte de room service. Garage privé avec accès direct au hall et petite salle de sport parfaitement équipée.',
 stats=['Maison de 1930','14 chambres','Garage privé','Salle de sport'],nav_rooms='Chambres',rooms_t='Nos chambres',rooms_s='Six types de chambres, de l\'individuelle deluxe à la familiale.',
 svcs=['Petit-déjeuner buffet','Room service','Garage privé avec accès au hall','Bornes de recharge pour véhicules électriques','Salle de sport','Cafétéria et salons réservés aux clients'],
 around_s='À quelques minutes à pied : Plaza Mayor, cathédrale, université, couvent de San Esteban, pont romain et jardins de Calixto y Melibea.',
 loc_p='P.º del Rector Esperabé, 10 · 37008 Salamanque, dans le centre historique.',
 chips=['Quelles chambres avez-vous ?','Avez-vous un garage ?','Y a-t-il un petit-déjeuner ?',"Où se trouve l'hôtel ?"]),
'de':dict(title='Hotel Rector · Boutique-Hotel in der Altstadt von Salamanca',see_rooms='Zimmer ansehen',hero_k='Salamanca · Altstadt',hero_t='Ein historisches Hotel im Zentrum von Salamanca',hero_s='Ein Boutique-Hotel in einem Haus von 1930, nahe der Casa Lis, der Kathedrale und der Römerbrücke.',
 intro_t='Für erholsame Tage',intro_p1='14 geräumige Zimmer. Cafeteria und Salons sind ausschließlich Hotelgästen vorbehalten, und die Privatsphäre jedes Aufenthalts wird gewahrt.',
 intro_p2='Frühstücksbuffet im Speisesaal und Room-Service-Karte. Private Garage mit direktem Zugang zur Lobby und ein kleiner, bestens ausgestatteter Fitnessraum.',
 stats=['Haus von 1930','14 Zimmer','Private Garage','Fitnessraum'],nav_rooms='Zimmer',rooms_t='Unsere Zimmer',rooms_s='Sechs Zimmerkategorien, vom Einzelzimmer Deluxe bis zum Familienzimmer.',
 svcs=['Frühstücksbuffet','Room Service','Private Garage mit Lobbyzugang','Ladepunkte für Elektroautos','Fitnessraum','Cafeteria und Salons nur für Gäste'],
 around_s='Wenige Gehminuten: Plaza Mayor, Kathedrale, Universität, Kloster San Esteban, Römerbrücke und Gärten Calixto y Melibea.',
 loc_p='P.º del Rector Esperabé, 10 · 37008 Salamanca, in der Altstadt.',
 chips=['Welche Zimmer gibt es?','Haben Sie eine Garage?','Gibt es Frühstück?','Wo liegt das Hotel?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RB={'es':'https://www.hotelrector.com/reservar.html','en':'https://www.hotelrector.com/EN/book.html','fr':'https://www.hotelrector.com/EN/book.html','de':'https://www.hotelrector.com/EN/book.html'}
BOOK=dict(mode='engine',url=RB)
D=dict(name='Hotel Rector',ac='#472616',ac2='#2f4f5e',ac2_a11y='#25414e',book=BOOK,around=['Catedral','Puente Romano'],foot=FOOT,
 address='P.º del Rector Esperabé, 10 · 37008 Salamanca',phones=['+34 923 218 482'],emails=['info@hotelrector.com'],maps='Hotel Rector, Paseo del Rector Esperabé 10, Salamanca',t=T)
META=dict(repo='demo-hotel-rector-salamanca',name='Hotel Rector',legal_name='HOTEL RESIDENCIA RECTOR S.A.',registry_ids=['CIF A37061728'],
 url='https://www.hotelrector.com/',domain='hotelrector.com',municipality='Salamanca',province='Salamanca',sector='hotel boutique de 14 habitaciones en una casa de 1930 del centro histórico de Salamanca',
 read_at='2026-10-30T07:22:18+01:00',created_at='2026-10-30T07:21:30+01:00',built_at='2026-10-30T07:35:00+01:00',audit_date='2026-10-30T06:53:00+01:00',
 rating=dict(value=4.9,coincide=['telefono','web'],date='2026-10-29T13:00:15+01:00',url='https://www.google.com/maps/place/Hotel+Rector/@40.9587517,-5.6657209,17z/data=!4m9!3m8!1s0xd3f266a8d000ae1:0xdec2c202d70b6b!5m2!4m1!1i2!8m2!3d40.9587517!4d-5.6657209!16s%2Fg%2F1tm0vg8j'),
 book=dict(mode='engine',url=RB['es'],note='página de reservas real de su web (reservar.html en es; EN/book.html en en/fr/de), HTTP 200 comprobado el 30/10/2026; el botón Reservar de su portada lleva a reservar.html.'),first_of_type=None)
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('Somos cinco, ¿tenéis habitación familiar?','K02'),('¿Tenéis garaje?','K03'),('Tengo coche eléctrico, ¿puedo cargarlo?','K04'),('¿Hay desayuno?','K05'),('¿Hay gimnasio?','K06'),('¿Dónde está el hotel?','K07'),('¿Cómo reservo?','K08'),('¿Podéis confirmarme disponibilidad para mañana?','K08'),('¿Qué historia tiene el edificio?','K09'),('¿Cuánto cuesta una noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('We are five, do you have a family room?','K02'),('Do you have a garage?','K03'),('I have an electric car, can I charge it?','K04'),('Is there breakfast?','K05'),('Is there a gym?','K06'),('Where is the hotel?','K07'),('How do I book?','K08'),('Can you confirm availability for tomorrow?','K08'),('What is the history of the building?','K09'),('How much is a night?',None),('Do you have a swimming pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Nous sommes cinq, avez-vous une chambre familiale ?','K02'),('Avez-vous un garage ?','K03'),("J'ai une voiture électrique, puis-je la recharger ?",'K04'),('Y a-t-il un petit-déjeuner ?','K05'),('Y a-t-il une salle de sport ?','K06'),("Où se trouve l'hôtel ?",'K07'),('Comment réserver ?','K08'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K08'),("Quelle est l'histoire du bâtiment ?",'K09'),('Combien coûte une nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Wir sind fünf, gibt es ein Familienzimmer?','K02'),('Haben Sie eine Garage?','K03'),('Ich habe ein Elektroauto, kann ich es laden?','K04'),('Gibt es Frühstück?','K05'),('Gibt es einen Fitnessraum?','K06'),('Wo liegt das Hotel?','K07'),('Wie kann ich buchen?','K08'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K08'),('Welche Geschichte hat das Gebäude?','K09'),('Was kostet eine Übernachtung?',None),('Haben Sie ein Schwimmbad?',None)]}
