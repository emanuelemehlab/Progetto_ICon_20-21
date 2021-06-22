%prova con liste 
%Open(X) :- member(X , s).
%sOpen(X,Ora,G) :- oraPalazzo(X,Ora),giorniPalazzo(X,G).


%membro in una lista
%member(T, [T | _]).
%member(T, [_ | L]) :- member(T, L).

%appartenenza delle citta nei continenti
e_nel_continente(san_paolo,america_sud).
e_nel_continente(amsterdam,europa).
e_nel_continente(buenos_aires,america_sud).
e_nel_continente(berlino,europa).
e_nel_continente(istanbul,eurasia).
e_nel_continente(londra,europa).
e_nel_continente(madrid,europa).
e_nel_continente(mosca,russia).
e_nel_continente(new_york,america).
e_nel_continente(parigi,europa).
e_nel_continente(tokyo,asia).


% emisferi
%boreale
boreale(asia ).
boreale(europa).
boreale(america).
boreale(africa_settentrionale).
boreale(africa_centrale).
boreale(russia).
%australe
australe( africa_meridionale).
australe(antartide).
australe(america_sud).
australe(oceania).
australe(sudest_asiatico).


%mesi estivi Boreali
mese_estivo_boreale(june).
mese_estivo_boreale(july).
mese_estivo_boreale(august).
%mesi primaverili boreali
mese_primaverile_boreale(march).
mese_primaverile_boreale(april).
mese_primaverile_boreale(may).
%mesi autunnali boreali
mese_autunnale_boreale(september).
mese_autunnale_boreale(october).
mese_autunnale_boreale(november).
%mesi invernali Boreali
mese_invernale_boreale(december).
mese_invernale_boreale(january).
mese_invernale_boreale(february).

%mesi estivi australi
mese_estivo_australe(december).
mese_estivo_australe(january).
mese_estivo_australe(february).
%mesi primaverili australi
mese_primaverile_australe(september).
mese_primaverile_australe(october).
mese_primaverile_australe(november).
%mesi autunnali australi
mese_autunnale_australe(march).
mese_autunnale_australe(april).
mese_autunnale_australe(may).
%mesi invernali australi
mese_invernale_australe(june).
mese_invernale_australe(july).
mese_invernale_australe(august).

%regole usate per capire la stagione in una città
estate(City , Mese , Giorno) :- eNelContinente(City,X) , estateBoreale(X , Mese , Giorno) .
estate(City , Mese , Giorno) :- eNelContinente(City , X) , estateAustrale(X , Mese , Giorno).

autunno(City , Mese , Giorno) :- eNelContinente(City,X) , autunnoBoreale(X , Mese , Giorno) .
autunno(City , Mese , Giorno) :- eNelContinente(City,X) , autunnoAustrale(X , Mese , Giorno) .

primavera(City , Mese , Giorno) :- eNelContinente(City,X) , primaveraBoreale(X , Mese , Giorno) .
primavera(City , Mese , Giorno) :- eNelContinente(City,X) , primaveraAustrale(X , Mese , Giorno) .

inverno(City , Mese , Giorno) :- eNelContinente(City,X) , invernoBoreale(X , Mese , Giorno) .
inverno(City , Mese , Giorno) :- eNelContinente(City,X) , invernoAustrale(X , Mese , Giorno) .

%stagioni boreali
estate_boreale(Continente ,Mese, Giorno) :- Giorno > 0 , Giorno < 31 ,
    meseEstivoBoreale(Mese) , boreale(Continente).

primavera_boreale(Continente , Mese , Giorno) :-  Giorno > 0 , Giorno < 31 ,
    mesePrimaverileBoreale(Mese) , boreale(Continente).

autunno_boreale(Continente , Mese , Giorno) :- Giorno > 0 , Giorno < 30 ,
    boreale(Continente) , meseAutunnaleBoreale(Mese) .

inverno_boreale(Continente , Mese , Giorno) :- Giorno > 0 , Giorno < 28 ,
    boreale(Continente) , meseInvernaleBoreale(Mese) .

% stagioni  australi
estate_australe(Continente  ,Mese, Giorno) :-  meseEstivoAustrale(Mese),
     Giorno > 0 , Giorno < 29 , australe(Continente).

primavera_australe(Continente , Mese , Giorno) :-  Giorno > 0 , Giorno < 31 ,
    australe(Continente) , mesePrimaverileAustrale(Mese).

autunno_australe(Continente , Mese , Giorno) :- Giorno > 0 , Giorno < 32 ,
    australe(Continente) ,meseAutunnaleAustrale(Mese).

inverno_australe(Continente , Mese , Giorno) :-  Giorno > 0 , Giorno < 32 ,
    australe(Continente) , meseInvernaleAustrale(Mese).



%stazioni
%stazioni san_paolo
station(san_paolo, estacao_agua_branca,3).
station(san_paolo, luz_station,5).
station(san_paolo, estacao_bras,14).
%stazioni amsterdam
station(amsterdam , central_station,6).
station(amsterdam , amsterdam_zuid,9).
station(amsterdam , haarlem,12).
%stazioni buenos Aires
station(buenos_aires , federico_lacroze,12).
station(buenos_aires , estacion_once,2).
station(buenos_aires , retiro_mitro,19).
%stazione berlino
station(berlino , berlin_friedrichstrabe_station,11).
station(berlino , berlin_alexanderplatz_bahnhof,12).
station(berlino , potsdamer_platz,19).
%stazioni istanbull
station(istanbull , halkai,19).
station(istanbull , yesilkoy,10).
station(istanbull , sirkeci_istasyon,11).
%stazioni londra
station(londra , kings_cross_station,16).
station(londra , paddington_station,10).
station(londra , liverpool_street_station,19).
%stazioni madrid
station(madrid , recoletos,1).
station(madrid , santa_eugenia,11).
station(madrid , estacion_de_atocha_cercanias,23).
%stazioni mosca
station(mosca , stazione_belorusskij,22).
station(mosca , yaroslavskiy_railway_tminal,1).
station(mosca , lningradskiy_railway_station,19).
%stazioni newYork
station(new_york , grand_central_terminal,1).
station(new_york , new_york_penn_station,19).
%stazioni parigi
station(parigi , musee_d_orsay,12).
station(parigi , gare_de_paris_lyon,11).
station(parigi , stazione_di_parigi_est,19).
%stazioni tokyo
station(tokyo , tokyo_station,1).
station(tokyo , shinagawa_station,10).
station(tokyo , harajuku_station,21).



%citta
city(san_paolo , america_sud, brasile, gmt-3 ).
city(amsterdam, europa, olanda, cest ).
city(buenos_aires, america_sud, argentina, gmt-3 ).
city(berlino, europa, germania, cest ).
city(istanbul, eurasia, turchia, gtm+3 ).
city(londra, europa, gran_bretagna, gtm+1  ).
city(madrid, europa, spagna, gtm+2 ).
city(mosca, asia, russia, gmt+3 ).
city(new_york, america, new_york, gmt-4 ).
city(parigi, europa, francia, cest ).
city(tokyo, asia, giappone, gmt+9 ).

%valute
currency(san_paolo , usd).
currency(amsterdam , eur).
currency(buenos_aires , ars).
currency(berlino , eur).
currency(istanbul , try).
currency(londra , gbp).
currency(madrid , eur).
currency(mosca , rub).
currency(new_york , usd).
currency(parigi , eur).
currency(tokyo , yen).



showplace(amsterdam , palazzo_reale , arte_antica , ven-dom , 10:00-17:00 , 7.50 ,1).
showplace( amsterdam , oude_kerk , arte_antica , lun-dom , 10:00-18:00 , 12.50,2).
showplace(amsterdam , denieuwe_kerk , arte_antica , lun-dom , 10:00-16:00 , 12.50,3).
showplace( amsterdam , blauwbrug , panorama , lun-dom , 00:00-24:00 , 0,4).
showplace(amsterdam , van_gogh_museum , museo , lun-ven , 10:00-18:00 , 15,5).
showplace( amsterdam , rijksmuseum , museo , lun-ven , 9:00-17:00 , 20,7).
showplace(amsterdam , piazza_dam , arte_antica , lun-dom , 00:00-24:00 , 0,8).
showplace( amsterdam , crociera_in_battello , panorama , lun-dom, 9.30-21:00, 23,10).
showplace( buenos_aires , parqu_tres_de_febrero , natura , lun-dom, 8:00-17:00 , 0 , 1).
showplace( buenos_aires , floralis_generica , natura , lun-dom, 9:00-19:00 , 300 , 6).
showplace( buenos_aires , planetario_galileo_galilei , scienza , mer-dom, 10:00-17:00 , 450,18 ).
showplace( buenos_aires , estadio_bombonera , sport , lun-dom, 10:00-18:00 , 260,16  ).
showplace( buenos_aires , buenos_aires_playa , natura , mar-dom, 10:00-20:00 , 0,10  ).
showplace( buenos_aires , ecoparque_ba , natura , mer-dom, 11:00-17:00 , 0 ,17 ).
showplace( buenos_aires , sarmiento_parque , natura , lun-dom, 8:00-20:00 , 335 ,21 ).
showplace( san_paolo , museum_de_arte , museo , mar-dom, 9:00-18:00, 48 ,4).
showplace( san_paolo , parco_zoologico , divertimento , lun-dom, 10:00-16:00, 35,10).
showplace( san_paolo , monumento_as_bandeiras , arte_antica , lun-dom, 00:00-24:00, 0 ,2).
showplace( san_paolo , sao_paulo_aquarium , divertimento , lun-dom, 10:00-18:00, 30 ,19).
showplace( san_paolo , itau_cultura , museo , mar-dom, 10:00-20:00, 20 ,11).
showplace( san_paolo , monumento_indipendenza , arte_antica , lun-dom, 00:00-24:00, 0,17 ).
showplace( san_paolo , jaragua_state_park , divertimento , mar-dom, 9:00-19:00, 150 ,29).
showplace( new_york , central_park , natura , lun-dom, 00:00-24:00, 0 ,12 ).
showplace( new_york , statua_della_liberta , panorama , lun-dom, 8.30-16:00, 21 ,23).
showplace( new_york , empire_state_building , panorama , lun-dom, 13:00-22:00, 44 ,2 ).
showplace( new_york , time_square , panorama , lun-dom, 00:00-24:00, 0 ,26 ).
showplace( new_york , museum_of_modern_art , arte_moderna , lun-dom, 10.30-17.30, 18 ,16 ).
showplace( new_york , metropolitan_museum , museo , mer-dom, 00:00-24:00, 0 ,27 ).
showplace( new_york , one_world_trade_center , panorama , lun-dom, 9:00-22:00, 0 ,11 ).
showplace( new_york , broadway , panorama , lun-dom, 00:00-24:00, 0 ,18 ).
showplace( new_york , bryant_park , natura , lun-dom, 7:00-22:00, 36 ,4 ).
showplace( new_york , top_of_the_rock , panorama , lun-dom, 13:00-21:00, 0 ,8 ).
showplace(tokyo, skytree, panorama, lun-dom, 10:00-20:00, 2.060, 2).
showplace(tokyo, tokyo_tower, panorama, lun-dom, 10:00-20:00, 820, 3).
showplace(tokyo, palazzo_imperiale, arte_antica, mar-sab, 9:00-11:15/13:30-14:30, 1600,4).
showplace(tokyo, mount_takao, panorama, lun - dom, 9.30-16.30, 420, 5).
showplace(tokyo, national_museum, arte_antica, mar-dom, 9.30-17:00, 620, 12).
showplace(tokyo, tempio_senso-ji, religione , lun-dom, 6:00-17:00, 0, 24).
showplace(tokyo, santuario_meiji, religione , lun-dom, 5:10-17:50, 500, 19).
showplace(istanbul, basilica_santa_sofia, religione, lun-dom, 8:00-19:00, 135,12).
showplace(istanbul, moschea_blu, religione, lun-dom, 9:00-19:00, 0,1).
showplace(istanbul, palazzo_topkapi, arte_antica , lun-dom, 8:00-19:00, 72,8).
showplace(istanbul, museo_di_archeologia, scienza , mer-lun, 9:00-19:00, 30,26).
showplace(istanbul, ponte_di_galata, panorama, lun-dom, 9:00-20:00, 25,23).
showplace(istanbul, cisterna_di_yerebatan, religione, lun-dom, 9:00-17:30, 20,15).
showplace(istanbul, chiesa_di_chora, religione, lun-dom, 9:00-19:00, 45,17).
showplace(istanbul, moschea_di_solimano_il_magnifico, religione, lun-dom, 9:00-17:30, 0,28).
showplace(istanbul, torre_di_galata, panorama, lun-dom, 9:00-20:00, 25,21).
showplace(mosca, cattedrale_di_san_basilio, cattedrale, lun-dom, 9:00-19:00, 700,2).
showplace(mosca, teatro_bolshoi, arte_moderna , lun-mer-ven, 11:00-12:00, 1.300,3).
showplace(mosca, planetarium, scienza , lun-dom, 10:00-22:00, 1000,23).
showplace(mosca, museo_delle_belle_arti_pushkin, arte_moderna, mar-dom, 10:00-18:00, 350,21).
showplace(mosca, cattedrale_di_cristo_salvatore, cattedrale, lun-dom, 10:00-17:00, 0,15).
showplace(mosca, parco_gorky, natura, lun-dom, 00:00-24:00, 0,25).
showplace(mosca, galleria_tretyakov, arte_moderna , mar-dom, 10:00-20:00, 500,27).
showplace(parigi, torre_eiffel, panorama, lun-dom, 9:00-24:00, 26.10,2).
showplace(parigi, arco_di_trionfo , panorama, lun-dom, 00:00-19:00, 0,3).
showplace(parigi, louvre , museo, lun-dom, 9:00-24:00, 8.50,4).
showplace(parigi, museo_d_orsay, museo, mar-dom, 9:30-18:00, 14,5).
showplace(parigi, disneyland_paris, divertimento, lun-dom, 10:00-20:00, 80,17).
showplace(parigi, parco_dei_principi , sport, lun-dom, 10:00-18:00, 27,18).
showplace(parigi, museo_d_arte_moderna, museo , mar-dom, 10:00-18:00, 0,23).
showplace(londra, big_ben , arte_antica , lun-dom, 10:00-18:00, 25.50,1 ).
showplace(londra, tower_bridge , panorama, lun-dom, 10:00-17:30, 20 ,2).
showplace(londra, london_eye , panorama, lun-dom, 11:00-18:00, 27.00 ,3).
showplace(londra, british_museum , arte_antica , lun-dom, 10:00-17:30, 0,18).
showplace(londra, tower_of_london , panorama, lun-dom, 10:00-18:00, 10 ,21).
showplace(londra, wembley_stadium , sport , lun-sab, 10:00-17:00, 19 ,22).
showplace(londra, wimbledon_greyhound_stadium , sport , lun-dom, 10:00-18:00, 12 ,28).
showplace(berlino, porta_di_brandeburgo, panorama , lun-dom, 10:00-22:00, 0 ,1).
showplace(berlino, reichstag, arte_antica, lun-dom, 8:00-24:00, 0 ,22).
showplace(berlino, east_side_gallery, arte_antica , lun-dom, 10:00-19:00, 12.50 ,2).
showplace(berlino, pergamonmuseum, arte_antica, lun-dom, 10:00-18:00, 18 ,3).
showplace(berlino, torre_della_televisione, panorama, lun-dom, 9:00-23:30, 14 ,13).
showplace(berlino, castello_di_charlottenburg, arte_antica , lun-dom, 10:00-18:00, 12 ,15).
showplace(berlino, neus_museum, arte_moderna, lun-dom , 10:00-18:00, 12 ,17).
showplace(berlino, alt_nationalgalerie, arte_antica , mar-dom, 10:00-18:00, 10,20 ).
showplace(madrid, museo_del_prado, museo , lun-sab, 18:00-20:00, 0 ,12).
showplace(madrid, cattedrale_almudena, cattedrale , lun-dom, 9:00-20:30, 1,2 ).
showplace(madrid, palazzo_di_cristallo, arte_moderna, lun-dom, 10:00-18:00, 0,3 ).
showplace(madrid, zoo_di_madrid, divertimento, lun-dom, 11:00-19:00, 23 ,5).
showplace(madrid, museo_stadio_santiago_bernabeu, museo, lun-sab, 10:00-19:30, 25,14 ).
showplace(madrid, museo_sorolla, museo , mar-sab, 9:30-20:00, 3 ,24).

% limiti orari Amsterdam-------------------------------------------------------------------------------
lim_ora(amsterdam , palazzo_reale , Ora) :- Ora > 9.59 , Ora < 17.00 .
lim_ora(amsterdam , oude_kerk, Ora) :- Ora > 9.59 ,Ora < 24.00 .
lim_ora(amsterdam , denieuwe_kerk , Ora) :- Ora > 9.59 ,Ora < 16.00 .
lim_ora(amsterdam , blauwbrug, Ora) :- Ora > 00.00 ,Ora < 18.00 .
lim_ora(amsterdam , van_gogh_museum, Ora) :- Ora > 9.59 , Ora < 19.30 .
lim_ora(amsterdam , rijksmuseum , Ora) :- Ora > 8.59 , Ora < 17.00 .
lim_ora(amsterdam , piazza_dam, Ora) :- Ora > 00.00 , Ora < 24.00 .
lim_ora(amsterdam , crociera_in_battello, Ora) :- Ora > 8.29 , Ora < 21.00 .
lim_ora(new_york , central_park , Ora) :- Ora > 00.00 , Ora < 24.00 .
lim_ora(new_york , statua_della_libertà , Ora) :- Ora > 7.29 , Ora < 21.00 .
lim_ora(new_york , empire_state_building , Ora) :- Ora > 12.59 , Ora < 22.00 .
lim_ora(new_york , time_square , Ora) :- Ora > 00.00 , Ora < 24.00 .
lim_ora(new_york , museum_of_modern_art , Ora) :- Ora > 9.29 , Ora < 17.30 .
lim_ora(new_york , metropolitan_museum , Ora) :- Ora > 00.00 , Ora < 24.00 .
lim_ora(new_york , one_world_trade_center , Ora) :- Ora > 8.59 , Ora < 23.00 .
lim_ora(new_york , broadway , Ora) :- Ora > 00.00 , Ora < 24.00 .
lim_ora(new_york , bryant_park , Ora) :- Ora > 6.59 , Ora < 22.00 .
lim_ora(new_york , top_of_the_rock , Ora) :- Ora > 12.59 , Ora < 21.00 .
lim_ora(san_paolo , museum_de_arte, Ora) :- Ora > 8.29 , Ora < 18.00 .
lim_ora(san_paolo , parco_zoologico, Ora) :- Ora > 9.59 , Ora < 16.00 .
lim_ora(san_paolo , monumento_as_bandeiras, Ora) :- Ora > 00.00 , Ora < 24.00 .
lim_ora(san_paolo , sao_paulo_aquarium, Ora) :- Ora > 9.59 , Ora < 18.00 .
lim_ora(san_paolo , itau_cultura, Ora) :- Ora > 9.59 , Ora < 20.00 .
lim_ora(san_paolo , monumento_indipendenza, Ora) :- Ora > 00.00 , Ora < 24.00 .
lim_ora(san_paolo , jaragua_state_park, Ora) :- Ora > 8.59 , Ora < 19.00 .
lim_ora(buenos_aires , parqu_tres_de_febrero, Ora) :- Ora > 7.59 , Ora < 17.00 .
lim_ora(buenos_aires , floralis_generica, Ora) :- Ora > 8.59 , Ora < 19.00 .
lim_ora(buenos_aires , planetario, Ora) :- Ora > 9.59 , Ora < 17.00 .
lim_ora(buenos_aires , estadio_bombonera, Ora) :- Ora > 9.59 , Ora < 18.00 .
lim_ora(buenos_aires , buenos_aires_playa, Ora) :- Ora > 9.59 , Ora < 20.00 .
lim_ora(buenos_aires , ecoparque_ba, Ora) :- Ora > 10.59 , Ora < 17.00 .
lim_ora(buenos_aires , sarmiento_parque, Ora) :- Ora > 7.59 , Ora < 20.00 .
lim_ora(tokyo , skytree , Ora) :- Ora > 9.59 , Ora < 20.00 .
lim_ora(tokyo , tokyo_tower , Ora) :- Ora > 9.59 , Ora < 20.00 .
lim_ora(tokyo , palazzo_imperiale , Ora) :- Ora > 8.59 , Ora < 23.00 .
lim_ora(tokyo , palazzo_imperiale , Ora) :- Ora > 13.29 , Ora < 14.30 .
lim_ora(tokyo , mount_takao , Ora) :- Ora > 9.29 , Ora < 16.00 .
lim_ora(tokyo , national_museum , Ora) :- Ora > 9.29 , Ora < 17.00 .
lim_ora(tokyo , tempio_senso_ji , Ora) :- Ora > 5.59 , Ora < 17.00 .
lim_ora(tokyo , santuario_meiji , Ora) :- Ora > 5.09 , Ora < 17.50 .
lim_ora(istanbul , basilica_santa_sofia , Ora) :- Ora > 7.59 , Ora < 18.00 .
lim_ora(istanbul , moschea_blu , Ora) :- Ora > 8.59 , Ora < 19.00 .
lim_ora(istanbul , palazzo_topkapi , Ora) :- Ora > 7.59 , Ora < 19.00 .
lim_ora(istanbul , museo_di_archeologia , Ora) :- Ora > 8.59 , Ora < 19.00 .
lim_ora(istanbul , ponte_di_galata , Ora) :- Ora > 8.59 , Ora < 20.00 .
lim_ora(istanbul , cisterna_di_yerebatan , Ora) :- Ora > 8.59 , Ora < 17.30 .
lim_ora(istanbul , chiesa_di_chora , Ora) :- Ora > 8.59 , Ora < 19.00 .
lim_ora(istanbul , moschea_di_solimano_il_magnifico , Ora) :- Ora > 8.59 , Ora < 17.30 .
lim_ora(istanbul , torre_di_galata , Ora) :- Ora > 8.59 , Ora < 20.00 .
lim_ora(mosca , cattedrale_di_san_basilio , Ora) :- Ora > 8.59 , Ora < 19.00 .
lim_ora(mosca , teatro_bolshoi , Ora) :- Ora > 10.59 , Ora < 12.00 .
lim_ora(mosca , planetarium , Ora) :- Ora > 9.59 , Ora < 22.00 .
lim_ora(mosca , museo_delle_belle_arti_pushkin , Ora) :- Ora > 9.59 , Ora < 18.00 .
lim_ora(mosca , cattedrale_di_cristo_salvatore , Ora) :- Ora > 9.59 , Ora < 17.00 .
lim_ora(mosca , parco_gorky , Ora) :- Ora > 00.00 , Ora < 24.00 .
lim_ora(mosca , galleria_tretyakov , Ora) :- Ora > 9.59 , Ora < 20.00 .
lim_ora(parigi , torre_eiffel , Ora) :- Ora > 8.59 , Ora < 24.00 .
lim_ora(parigi , arco_di_trionfo , Ora) :- Ora > 0.00 , Ora < 19.00 .
lim_ora(parigi , louvre  , Ora) :- Ora > 8.59 , Ora < 24.00 .
lim_ora(parigi , disneyland_paris , Ora) :- Ora > 9.59 , Ora < 17.30 .
lim_ora(parigi , museo_d_orsay , Ora) :- Ora > 5.59 , Ora < 22.30 .
lim_ora(parigi , parco_dei_principi  , Ora) :- Ora > 9.59 , Ora < 18.00 .
lim_ora(parigi , museo_d_arte_moderna , Ora) :- Ora > 9.59 , Ora < 18.00 .
lim_ora(londra , big_ben  , Ora) :- Ora > 9.59 , Ora < 18.00 .
lim_ora(londra , tower_bridge  , Ora) :- Ora > 9.59 , Ora < 17.30 .
lim_ora(londra , london_eye  , Ora) :- Ora > 10.59 , Ora < 18.00 .
lim_ora(londra , british_museum  , Ora) :- Ora > 9.59 , Ora < 17.30 .
lim_ora(londra , tower_of_london  , Ora) :- Ora > 9.59 , Ora < 18.00 .
lim_ora(londra , buckingham_palace  , Ora) :- Ora > 8.59 , Ora < 19.00 .
lim_ora(londra , national_gallery  , Ora) :- Ora > 9.59 , Ora < 18.00 .
lim_ora(berlino , porta_di_brandeburgo  , Ora) :- Ora > 9.59 , Ora < 22.00 .
lim_ora(berlino , reichstag  , Ora) :- Ora > 7.59 , Ora < 24.00 .
lim_ora(berlino , east_side_gallery  , Ora) :- Ora > 9.59 , Ora < 19.00 .
lim_ora(berlino , pergamonmuseum  , Ora) :- Ora > 9.59 , Ora < 18.00 .
lim_ora(berlino , torre_della_televisione   , Ora) :- Ora > 8.59 , Ora < 23.30 .
lim_ora(berlino , castello_di_charlottenburg  , Ora) :- Ora > 9.59 , Ora < 18.00 .
lim_ora(berlino , neus_museum  , Ora) :- Ora > 9.59 , Ora < 18.00 .
lim_ora(berlino , alt_nationalgalerie  , Ora) :- Ora > 9.59 , Ora < 18.00 .
lim_ora(madrid , museo_del_prado   , Ora) :- Ora > 17.59 , Ora < 20.00 .
lim_ora(madrid , cattedrale_almudena   , Ora) :- Ora > 8.59 , Ora < 20.30 .
lim_ora(madrid , palazzo_di_cristallo   , Ora) :- Ora > 9.59 , Ora < 18.00 .
lim_ora(madrid , zoo_di_madrid   , Ora) :- Ora > 10.59 , Ora < 19.00 .
lim_ora(madrid , stadio_santiago_bernabeu   , Ora) :- Ora > 9.59 , Ora < 19.30 .
lim_ora(madrid , museo_sorolla   , Ora) :- Ora > 9.29 , Ora < 20.00 .

%--------------------------------------------------------------------------------------------------------

% giorni di apertura  Amsterdam--------------------------------------------------------------------
lim_giorno(amsterdam , piazza_dam , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(amsterdam , rijksmuseum , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(amsterdam , van_gogh_museum , Giorno) :- Giorno > 0 ,Giorno < 6 .
lim_giorno(amsterdam , blauwbrug , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(amsterdam , denieuwe_kerk , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(amsterdam , oude_kerk , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(amsterdam , palazzo_reale , Giorno) :- Giorno > 4 , Giorno < 8 .
lim_giorno(amsterdam , crociera_in_battello , Giorno) :- Giorno > 0 , Giorno < 7 .
lim_giorno(buenos_aires , parqu_tres_de_febrero, Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(buenos_aires , floralis_generica, Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(buenos_aires , planetario, Giorno) :- Giorno > 2 , Giorno < 8 .
lim_giorno(buenos_aires , estadio_bombonera, Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(buenos_aires , buenos_aires_playa, Giorno) :- Giorno > 1 , Giorno < 8 .
lim_giorno(buenos_aires , ecoparque_ba, Giorno) :- Giorno > 2 , Giorno < 8 .
lim_giorno(buenos_aires , sarmiento_parque, Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(san_paolo , museum_de_arte, Giorno) :- Giorno > 1 , Giorno < 8 .
lim_giorno(san_paolo , parco_zoologico, Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(san_paolo , monumento_as_bandeiras, Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(san_paolo , sao_paulo_aquarium, Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(san_paolo , itau_cultura, Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(san_paolo , monumento_indipendenza, Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(san_paolo , jaragua_state_park, Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(new_york , central_park, Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(new_york , statua_della_libertà, Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(new_york , empire_state_building, Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(new_york , time_square, Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(new_york , museum_of_modern_art, Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(new_york , metropolitan_museum, Giorno) :- Giorno > 2 , Giorno < 8 .
lim_giorno(new_york , one_world_trade_center, Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(new_york , broadway, Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(new_york , bryant_park, Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(new_york , top_of_the_rock, Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(tokyo , skytree , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(tokyo , tokyo_tower  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(tokyo , palazzo_imperiale  , Giorno) :- Giorno > 1 , Giorno < 7 .
lim_giorno(tokyo , mount_takao  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(tokyo , national_museum  , Giorno) :- Giorno > 1 , Giorno < 8 .
lim_giorno(tokyo , tempio_senso_ji  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(tokyo , santuario_meiji , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(tokyo , santuario_meiji , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(istanbull , basilica_santa_sofia  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(istanbull , moschea_blu  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(istanbull , palazzo_topkapi  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(istanbull , museo_di_archeologia  , Giorno) :- Giorno > 2 , Giorno < 8 .
lim_giorno(istanbull , ponte_di_galata  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(istanbull , cisterna_di_yerebatan  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(istanbull , chiesa_di_chora  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(istanbull , moschea_di_solimano_il_magnifico  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(istanbull , torre_di_galata  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(mosca , cattedrale_di_san_basilio , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(mosca , teatro_bolshoi , Giorno) :- Giorno > 0 , Giorno < 2 .
lim_giorno(mosca , teatro_bolshoi , Giorno) :- Giorno > 2 , Giorno < 4 .
lim_giorno(mosca , teatro_bolshoi , Giorno) :- Giorno > 4 , Giorno < 6 .
lim_giorno(mosca , planetarium , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(mosca , museo_delle_belle_arti_pushkin , Giorno) :- Giorno > 1 , Giorno < 8 .
lim_giorno(mosca , cattedrale_di_cristo_salvatore , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(mosca , parco_gorky , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(mosca , galleria_tretyakov , Giorno) :- Giorno > 1 , Giorno < 8 .
lim_giorno(parigi , torre_eiffel , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(parigi , arco_di_trionfo , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(parigi , louvre  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(parigi , disneyland_paris , Giorno) :- Giorno > 1 , Giorno < 8 .
lim_giorno(parigi , museo_d_orsa  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(parigi , parco_dei_principi  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(parigi , museo_d_arte_moderna , Giorno) :- Giorno > 1 , Giorno < 8 .
lim_giorno(londra , big_ben  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(londra , tower_bridge  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(londra , london_eye  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(londra , british_museum  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(londra , tower_of_london  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(londra , buckingham_palace  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(londra , national_gallery  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(berlino , porta_di_brandeburgo  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(berlino , reichstag  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(berlino , east_side_galler   , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(berlino , pergamonmuseu   , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(berlino , torre_della_televisione   , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(berlino , castello_di_charlottenburg  , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(berlino , neus_museum   , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(berlino , alt_nationalgalerie , Giorno) :- Giorno > 1 , Giorno < 8 .
lim_giorno(madrid , museo_del_prado, Giorno) :- Giorno > 0 , Giorno < 7 .
lim_giorno(madrid , cattedrale_almudena , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(madrid , palazzo_di_cristallo , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(madrid , zoo_di_madrid , Giorno) :- Giorno > 0 , Giorno < 8 .
lim_giorno(madrid , stadio_santiago_bernabeu , Giorno) :- Giorno > 0 , Giorno < 7 .
lim_giorno(madrid , museo_sorolla , Giorno) :- Giorno > 1 , Giorno < 7 .


%--------------------------------------------------------------------------------------------------------


% verifica del passaporto
non_serveIl_passaporto(City,ContPart) :- eNelContinente(City,ContPart) .


% vedere se un posto è aperto
is_open(Citta,Posto,Giorno,Ora) :- lim_ora(Citta , Posto ,Ora) ,
    lim_giorno(Citta , Posto , Giorno) .
%--------------------------------------------------------------------
